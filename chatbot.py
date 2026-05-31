import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import openai

ROLES = {
    "default":"you are a helpful assistant.",
    "ecommerce":(
        "you are a senior customer service agent for an electronics store."
        "you help customers with product questions,orders,and returns."
        "Always be peofessional and concise."
        "if you do not know the answer,say so honestly."
    ),
    "teacher":(
        "you are a patient python programming tutor."
        "explain concepts with simple examples."
        "when a student makes a mistake,guide them gently."
    ),
}
class Chatbot:
    def __init__(self,role:str="default"):
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY not found in environment variables.")    
        self.client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com"
        )
        self.system_prompt = ROLES.get(role, ROLES["default"])
        self.history = []
        self.role=role
    def estimate_tokens(self, messages:list) -> int:
        """Rough estimate:~1.3 tokens per character on average."""
        total_chars=sum(len(m["content"]) for m in messages)
        return int(total_chars * 1.3)
    def append_message(self,role:str,content:str):
        """Add a message to history."""
        self.history.append({"role": role, "content": content})
    def generate_response(self,user_input:str,max_turns:int=10,max_tokens:int=4000)-> str:
        self.append_message("user", user_input)
        max_messages = max_turns * 2
        recent = self.history[-max_messages:] if len(self.history) > max_messages else self.history[:]
        while len(recent)>=2 and self.estimate_tokens(recent) > max_tokens:
            recent = recent[2:]
        messages = [{"role": "system", "content": self.system_prompt}] + recent
        try:
            response = self.client.chat.completions.create(
                model="deepseek-v4-pro",
                messages=messages,
            )
            assistant_reply = response.choices[0].message.content
        except openai.APIConnectionError:
            self.history.pop() # undo the user message we just added
            return "网络连接错误，请稍后再试。"
        except openai.RateLimitError:      
            self.history.pop() # undo the user message we just added
            return "请求过于频繁，请稍后再试。"
        except openai.APIError as e: 
            self.history.pop() 
            return f"[错误]API返回错误:{e.status_code}"
        self.append_message("assistant", assistant_reply)
        return assistant_reply
    def clear_history(self):
        self.history=[]
        print("对话历史已清空")