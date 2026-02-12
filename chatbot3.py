import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime, date


def get_response(msg):
    msg = msg.lower()

    if any(greet in msg for greet in ["hello", "hi", "hey"]):
        return "Hello! 👋 How can I help you today?"

    if "your name" in msg:
        return "I'm ChatX — your intelligent chat assistant 🤖."

    if "how are you" in msg:
        return "I’m doing great! Thanks for asking 😊"

    if "time" in msg:
        return "⏰ Current time: " + datetime.now().strftime("%H:%M:%S")

    if "date" in msg:
        return "📅 Today's date: " + str(date.today())

    if "weather" in msg:
        return "🌤️ The weather looks nice today!"
    elif  "what is ai" in msg:
        return "AI means Artificial Intelligence — making machines think like humans."

    elif "what is python" in msg:
        return "Python is a programming language used for web, AI, automation and more."

    elif  "what is machine learning" in msg:
        return "Machine learning helps computers learn from data and improve automatically."

    elif  "what is cloud computing" in msg:
        return "Cloud computing allows users to use services like storage & servers over the internet."

    elif "what is cybersecurity" in msg:
        return "Cybersecurity protects systems and data against cyber attacks."

    if "python" in msg:
        return "🐍 Python is a powerful programming language for AI and apps."

    if any(bye in msg for bye in ["bye", "exit"]):
        return "Goodbye! Have a great day 😊"

    return "Hmm... I didn’t understand that. Try something else 🤔"



def add_message(sender, message, color):
    chatbox.config(state=tk.NORMAL)
    
    chatbox.insert(tk.END, f"{sender}: ", ("sender",))
    chatbox.insert(tk.END, message + "\n\n", ("msg", color))
    
    chatbox.tag_config("sender", foreground="yellow", font=("Arial", 10, "bold"))
    chatbox.tag_config("msg", font=("Arial", 12))
    chatbox.tag_config("user", foreground="#00eaff")
    chatbox.tag_config("bot", foreground="#00ff7f")

    chatbox.config(state=tk.DISABLED)
    chatbox.yview(tk.END)



def send_message():
    txt = entry.get().strip()
    if txt == "":
        return

    add_message("You", txt, "user")
    entry.delete(0, tk.END)

    
    root.after(300, bot_typing, txt)


def bot_typing(user_msg):
    add_message("Bot", "Typing...", "bot")
    root.update()
    time.sleep(0.4)

    
    chatbox.config(state=tk.NORMAL)
    chatbox.delete("end-3l", "end-1l")
    chatbox.config(state=tk.DISABLED)

    
    response = get_response(user_msg)
    add_message("Bot", response, "bot")



def clear_chat():
    chatbox.config(state=tk.NORMAL)
    chatbox.delete(1.0, tk.END)
    chatbox.config(state=tk.DISABLED)



def quick_reply(text):
    entry.delete(0, tk.END)
    entry.insert(0, text)
    send_message()



root = tk.Tk()
root.title("ChatX - Smart Chatbot")
root.geometry("580x650")
root.configure(bg="#0a0f24")

title = tk.Label(root, text="🤖 ChatX - Advanced Python Chatbot", font=("Arial", 20, "bold"), fg="white", bg="#0a0f24")
title.pack(pady=10)


chatbox = tk.Text(root, width=70, height=25, bg="#3d445e", fg="white", wrap=tk.WORD, padx=10, pady=10)
chatbox.pack(padx=15, pady=10)
chatbox.config(state=tk.DISABLED)

frame = tk.Frame(root, bg="#0a0f24")
frame.pack(pady=5)

entry = tk.Entry(frame, width=40, font=("Arial", 14))
entry.grid(row=0, column=0, padx=10)

send_btn = tk.Button(frame, text="Send", font=("Arial", 14), bg="#0078ff", fg="white", command=send_message)
send_btn.grid(row=0, column=1)

clr_btn = tk.Button(frame, text="Clear Chat", font=("Arial", 12), bg="#444", fg="white", command=clear_chat)
clr_btn.grid(row=0, column=2, padx=10)


quick_frame = tk.Frame(root, bg="#0a0f24")
quick_frame.pack(pady=15)

ttk.Button(quick_frame, text="Hello", width=12, command=lambda: quick_reply("Hello")).grid(row=0, column=0, padx=5)
ttk.Button(quick_frame, text="Time?", width=12, command=lambda: quick_reply("What is the time?")).grid(row=0, column=1, padx=5)
ttk.Button(quick_frame, text="Weather", width=12, command=lambda: quick_reply("Tell me weather")).grid(row=0, column=2, padx=5)

root.mainloop()