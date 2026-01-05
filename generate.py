from openai import OpenAI
from dotenv import load_dotenv
import os
import yaml


load_dotenv()

with open("prompts.yaml", "r") as f:
    prompts = yaml.safe_load(f)

class GenerateEmail():    
    def __init__(self, model: str):
        # initialize client once and continually reuse to send prompts and receive response
        self.client = OpenAI(
            base_url=os.getenv("OPENAI_API_BASE"),
            api_key=os.getenv("OPENAI_API_KEY"),
        )
        self.deployment_name = model

    def _call_api(self, messages):
        # TODO: implement this function to call ChatCompletions
        #assume messages is a dict of the action and the email content

        
        response = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=messages,
        )
        return response.choices
        
    
    def get_prompt(self, prompt_name, prompt_type='user', **kwargs):
        #takes in a raw prompt name and the type and formats it in the proper way to sed to API
        #takes in user as prompt type by default
        template = prompts[prompt_name][prompt_type]
        return template.format(**kwargs)
    
    def send_prompt(self, user_prompt: str, system_msg="You are a helpful assistant for an AI Bootcamp working on email edits."):
        #sends the user prompt and system message to the API and returns the json like response
        #takes in a system message in case one is not passed in in the function call
        messages = [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_prompt}
        ]
        return self._call_api(messages)
    
    def generate(self, action: str, email:str) -> list:
        # TODO: implement your backend logic with this method. Skeleton code is provided below.
        args = {
            "selected_text": email
        }
        if action == "change tone":
            action = "change_tone"
            system_prompt = self.get_prompt(action, prompt_type='system', **args)
            user_prompt = self.get_prompt(action, **args)
            model_response = self.send_prompt(user_prompt + email, system_prompt)
            return model_response
        system_prompt = self.get_prompt(action, prompt_type='system', **args)
        user_prompt = self.get_prompt(action, **args)
        model_response = self.send_prompt(user_prompt + email, system_prompt)
        return model_response
        # elif action == "lengthen":
        #     args = {
        #         "selected_text": "This is a sample email content that needs to be lengthened. It is quite brief and could benefit from additional details and explanations to make it more comprehensive for the recipient."
        #     }
        #     system_prompt = self.get_prompt('shorten', prompt_type='system', **args)
        #     user_prompt = self.get_prompt('shorten', **args)
        #     model_response = self.send_prompt(user_prompt + email, system_prompt)
        #     return model_response
        # else:
        #     args = {
        #         "selected_text": "This is a sample email content that needs a change in tone. The current tone is quite formal and could be made more casual and friendly to better connect with the recipient."
        #     }
        #     system_prompt = self.get_prompt('shorten', prompt_type='system', **args)
        #     user_prompt = self.get_prompt('shorten', **args)
        #     model_response = self.send_prompt(user_prompt + email, system_prompt)
        #     return model_response
        

def evaluate_prompts(metric,edited_email,original_email,action):
    client = GenerateEmail(os.getenv("DEPLOYMENT_NAME"))
    args = {
        "original_email": original_email,
        "edited_email": edited_email,
        "action": action
    }
    prompts2 = yaml.safe_load(open("judge_prompts.yaml"))
    client2 = GenerateEmail(os.getenv("DEPLOYMENT_NAME_2"))
    result = client2.send_prompt(prompts2[metric]['user'].format(**args), prompts2[metric]['system'])
    return result[0].message.content

def generate_new_emails(email_type, number_of_emails):
    client = GenerateEmail(os.getenv("DEPLOYMENT_NAME_2"))
    prompts2 = yaml.safe_load(open("create_emails.yaml"))
    args = {
        "email_type": email_type,
        "number_of_emails": number_of_emails
    }
    result = client.send_prompt(prompts2['create_emails']['user'].format(**args), prompts2['create_emails']['system'])
    return(result[0].message.content)


