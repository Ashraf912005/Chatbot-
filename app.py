import streamlit as st # type: ignore
import datetime
import time

# Title
st.title("🤖 AI Study Buddy - Rule Based Chatbot")

# Greeting based on Time
name = st.text_input("Enter your name:")
presenthour = datetime.datetime.now().hour

if 5 <= presenthour < 12:
    print(f"🌞 Good Morning {name}!")
elif 12 <= presenthour < 17:
    print(f"🌤️ Good Afternoon {name}!")
elif 17 <= presenthour < 20:
    print(f"🌆 Good Evening {name}!")
else:
    print(f"🌙 Hello {name}! Have a peaceful night 😊")


st.write("You can chat with me below 👇 (type 'bye' to stop)")

responses = {
    "hello": "Hi, Welcome how can I help you?",
    "how are you": "I am very fine, Thank you!",
    "who are you": "I am a smart AI Chatbot 😎",
    "motivate me": "Keep Going! Every bug you fix makes you a better developer! 💻🔥",
    "i am happy": "Great to hear that! 😄",
    "functions": "Functions are blocks of code defined and called to perform specific tasks.",
    "python": "Python is an object-oriented programming language developed by Guido van Rossum!",
    "longest word by letters": "Pneumonoultramicroscopicsilicovolcanoconiosis has 45 letters!",
    "oop": "OOP stands for Object-Oriented Programming. It uses objects to represent real-world things."
}

problem_solutions = {
    "study": "Don’t worry! Let’s make a timetable and break things into small tasks 💪",
    "exams": "Exam stress is normal — Take breaks & solve previous papers 🙌",
    "friend": "Talk to them politely. Communication solves most relationships ❤️",
    "family": "Share your feelings with someone close. You’re not alone 🙂",
    "health": "Health first! Please rest well and drink water 💧",
    "love": "Love hurts sometimes 💔 but better days are coming — trust the process 🌈",
    "money": "Try saving small amounts & look for part-time opportunities 💼"
}

def getResponseofbot(userquestion):
    userquestion = userquestion.lower().strip()

    if "bye" in userquestion:
        return "Goodbye! Take care! 👋😊"

    if "sad" in userquestion:
        return "It's okay to feel sad sometimes ❤️ Tell me, what happened?"

    for keyword in problem_solutions:
        if keyword in userquestion:
            return problem_solutions[keyword]

    if "happy" in userquestion:
        return "Yay! Keep smiling 😄✨"

    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]

    return "I don't know that yet 😅 but I am learning every day!"

# Chat message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input for chat
user_input = st.text_input("You:", key="input")

if st.button("Send"):
    if user_input:
        reply = getResponseofbot(user_input)
        st.session_state.messages.append(("You", user_input))
        time.sleep(1)
        st.session_state.messages.append(("Bot", reply))

# Display chat messages
for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**🧑 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")

