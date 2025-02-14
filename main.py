import os
from groq import Groq  # 修正拼写错误
from dotenv import load_dotenv

load_dotenv()  # 加载环境变量

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("欢迎使用Groq聊天助手（输入'quit'退出）")

while True:
    user_input = input("\n你的问题：")
    
    if user_input.lower() == "quit":
        print("再见！")
        break
        
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": user_input}],  # 修正字典语法
            model="mixtral-8x7b-32768",
        )
        print("\n回答：\n" + response.choices[0].message.content)
        
    except Exception as e:
        print(f"出错：{str(e)}")