import streamlit as st
import json
from generate import GenerateEmail, evaluate_prompts, generate_new_emails
import os


# --- CONFIG ---
st.set_page_config(page_title="AI Email Editor", page_icon="📧", layout="wide")
client = GenerateEmail(model=os.getenv("DEPLOYMENT_NAME"))
def get_emails(action,number_of_emails):
    
    emails ={}
    new_emails = json.loads(generate_new_emails(action,number_of_emails))
    for record in new_emails:
        email_id = record.get('id')
        emails[email_id] = record

    return emails

        
# --- INITIAL EMAIL FETCH (Compact) ---
st.session_state.setdefault("emails", {})
st.session_state.setdefault("emails_initialized", False)

if not st.session_state.emails_initialized:
    for action in ["lengthen", "shorten", "change tone"]:
        st.session_state.emails[action] = get_emails(action, 25)
    st.session_state.emails_initialized = True








# --- UI HEADER ---
st.title("📧 AI Email Editing Tool")
st.write("Select an email record by ID and use AI to refine it.")

if not st.session_state.emails:
    st.warning("No emails found in your JSONL file.")
    st.stop()

# --- ID NAVIGATION BAR ---

email_type = st.sidebar.selectbox("📂 Select Email Type", options=list(st.session_state.emails.keys()))
selected_id = st.sidebar.selectbox("📂 Select Email ID", options=st.session_state.emails[email_type].keys())
metric_type = st.sidebar.selectbox("📂 Select Evaluation Metric", options=["faithfulness","completeness","relevance","conciseness","precision_recall"], index=0)

# Find the selected email
selected_email = st.session_state.emails[email_type][selected_id]
if not selected_email:
    st.error(f"No email found with ID {selected_id}.")
    st.stop()

# --- DISPLAY SELECTED EMAIL ---
st.markdown(f"### ✉️ Email ID: `{selected_id}`")
st.markdown(f"**From:** {selected_email.get('sender', '(unknown)')}")
st.markdown(f"**Subject:** {selected_email.get('subject', '(no subject)')}")

# --- TRACK AI CONTEXT ---
current_context = (selected_id, email_type)
if ("selected_context" not in st.session_state) or st.session_state.selected_context != current_context:
    st.session_state.ai_result = ""       # Reset AI result only when email/type changes
    st.session_state.selected_context = current_context

# --- TRACK METRIC CONTEXT ---
# Reset metric evaluation box only when metric type changes
if "metric_type" in locals():  # only if metric selectbox exists
    if ("metric_context" not in st.session_state) or st.session_state.metric_context != metric_type:
        st.session_state.metric_result = ""  # Clear evaluation box
        st.session_state.metric_context = metric_type
selected_email = st.session_state.emails[email_type][selected_id]

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

ai_edit_button = st.button(f"{email_type.capitalize()} with AI")
if ai_edit_button:
    edit_email_with_ai(email_type,email_text)


if st.session_state.ai_result:
    st.text_area(
        "Result",
        value=st.session_state.ai_result,
        height=250,
    )
if st.session_state.ai_result:
    ai_evaluate_button = st.button(f"Evaluate with AI on {metric_type}")
    if ai_evaluate_button:
        evaluate_email_with_ai(metric_type,email_text,email_type)
if st.session_state.metric_result:
    rating_info = json.loads(st.session_state.metric_result)
    st.text_area(
        "Evaluation Result",
        value=f"Rating: {rating_info.get("rating")}\nExplanation: {rating_info.get("explanation")}",
        height=150,
    )
    