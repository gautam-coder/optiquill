import openai
from time import sleep
import re
import json
import threading

openai.api_key = "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"
system_message='''
Hello there! As an AI language model, I'm here to help you with your questions and provide you with useful information. Whether you need a quick answer or are looking for something specific, just ask and I'll do my best to assist you and give a optimized keywords for Google search that you can use to find what you're looking for. And if you need a code snippet or programming help, just let me know and I'll try my best to provide you with a solution. So, what can I help you with today?"'''

def chatgpt(text):
    
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", 
      messages = [{'role':'assistant','content':text+system_message}]
    )
    parsed_response = json.loads(str(completion))
    message_content = parsed_response["choices"][0]["message"]["content"]
    return message_content
        
   
from tkinter import *

root = Tk()
root.geometry("500x250")
root.title("Chatbot")

chatbot_window = Text(root, bd=1, bg="lightblue", font=("Arial", 14), height=5, width=40)
chatbot_window.pack(padx=10, pady=10)

input_field = Entry(root, font=("Arial", 14), width=30)
input_field.pack(padx=10, pady=10)
def pypy(text):
    
    pyautogui.moveTo(304,65,1)
    pyautogui.click()
    sleep(2)
    #pyautogui.hotkey("ctrl","t")
    
    pyautogui.write(text)
    pyautogui.hotkey("enter")
    
def get_input():
    user_input = input_field.get()
    input_field.delete(0, END)
    chatbot_window.insert(END, "You: " + user_input + "\n")
    
    a=chatgpt(user_input)
    chatbot_window.insert(END, "Chatbot: {}\n".format(a))
    
        

send_button = Button(root, text="Send", command=get_input, font=("Arial", 10), width=8)
send_button.pack(padx=10, pady=10)

root.mainloop()

