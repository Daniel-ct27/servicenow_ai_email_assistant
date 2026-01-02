import streamlit as st
import json
from generate import GenerateEmail, evaluate_prompts
import os


# --- CONFIG ---
st.set_page_config(page_title="AI Email Editor", page_icon="📧", layout="wide")
client = GenerateEmail(model=os.getenv("DEPLOYMENT_NAME"))
def get_emails(file_path):
    with open(file_path, 'r',encoding="utf-8") as f:   
        emails = {}
        for line in f.readlines():
            email_record = json.loads(line)
            email_id = email_record.get('id')
            emails[email_id] = email_record

    return emails

email_options = {"lengthen":get_emails('./datasets/lengthen.jsonl'),
                "shorten":get_emails('./datasets/shorten.jsonl'),
                "change tone": get_emails('./datasets/tone.jsonl')}


# --- UI HEADER ---
st.title("📧 AI Email Editing Tool")
st.write("Select an email record by ID and use AI to refine it.")

if not email_options:
    st.warning("No emails found in your JSONL file.")
    st.stop()

# --- ID NAVIGATION BAR ---

email_type = st.sidebar.selectbox("📂 Select Email Type", options=list(email_options.keys()), index=0)
selected_id = st.sidebar.selectbox("📂 Select Email ID", options=email_options.get(email_type).keys(), index=0)
metric_type = st.sidebar.selectbox("📂 Select Evaluation Metric", options=["faithfulness","completeness","relevance","conciseness","precision_recall"], index=0)

# Find the selected email
selected_email = email_options.get(email_type).get(selected_id)
if not selected_email:
    st.error(f"No email found with ID {selected_id}.")
    st.stop()

# --- DISPLAY SELECTED EMAIL ---
st.markdown(f"### ✉️ Email ID: `{selected_id}`")
st.markdown(f"**From:** {selected_email.get('sender', '(unknown)')}")
st.markdown(f"**Subject:** {selected_email.get('subject', '(no subject)')}")

# ---- state init ----
if "ai_result" not in st.session_state:
    st.session_state.ai_result = ""
if "metric_result" not in st.session_state:
    st.session_state.metric_result = ""

if "prev_context" not in st.session_state:
    st.session_state.prev_context = (selected_id, email_type)

if "prev_metric_context" not in st.session_state:
    st.session_state.prev_metric_context = (selected_id, metric_type)

# ---- reset when context changes ----
current_context = (selected_id, email_type)
current_metric_context = (selected_id, metric_type)

if st.session_state.prev_context != current_context:
    st.session_state.ai_result = ""
    st.session_state.prev_context = current_context

if st.session_state.prev_metric_context != current_metric_context:
    st.session_state.metric_result = ""
    st.session_state.prev_metric_context = current_metric_context

email_text = st.text_area(
    "Email Content",
    value=selected_email.get("content", ""),
    height=250,
    key=f"email_text_{selected_id}",
)

def openai_client_call(action,email):
    #make api call to openai to edit email depending on action
    return client.generate(action,email)[0].message.content
    
    

def edit_email_with_ai(action,email):
    #changes state of the result text area
    st.session_state.ai_result = openai_client_call(action,email)
    
def evaluate_email_with_ai(metric,selected_email,email_type):
    #changes state of the result text area
    if not st.session_state.ai_result:
        st.warning("Please generate an edited email first before evaluation.")
        return
    st.session_state.metric_result = evaluate_prompts(metric_type,st.session_state.ai_result,selected_email,email_type)

ai_edit_button = st.button(f"{email_type.capitalize()} with AI",on_click=edit_email_with_ai,args=(email_type,email_text,))


if st.session_state.ai_result:
    st.text_area(
        "Result",
        value=st.session_state.ai_result,
        height=250,
    )
if st.session_state.ai_result:
    ai_evaluate_button = st.button(f"Evaluate with AI on {metric_type}",on_click=evaluate_email_with_ai,args=(metric_type,selected_email,email_type))
if st.session_state.metric_result:
    rating_info = json.loads(st.session_state.metric_result)
    st.text_area(
        "Evaluation Result",
        value=f"Rating: {rating_info.get("rating")}\nExplanation: {rating_info.get("explanation")}",
        height=150,
    )
    