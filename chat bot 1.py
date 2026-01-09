import random   

def chatbot_response(user_input):


    text = user_input.lower()

    if "hi" in text or "hello" in text or "hey" in text:
        return random.choice([
            "Hello there ! How can I help you?",
            "Hi there! do you Need any assistance?",
            "Hey! What can I do for you?"
        ])
    
    elif "bye" in text or "goodbye" in text or "see you" in text:
        return random.choice([
            "Goodbye! Have a great day.",
            "See you soon,bye !",
            "Take care!"
        ])

    elif "thanks" in text or "thank you" in text:
        return random.choice([
            "You're welcome!",
            "Glad I could help!",
            "No problem at all!"
        ])
    
    elif "joke" in text:
        return random.choice([
            "I'm on a seafood diet — I see food and I eat it.",
            "I told a chemistry joke, but there was no reaction."
        ])

    elif "help" in text or "assist" in text:
        return random.choice([
            "Sure, I am here to help. What do you need?",
            "Happy to help! Please describe your issue.",
            "What can I do for you?"
        ])


    elif "name" in text:
        return random.choice([
            "I am RuleBot, your simple chatbot.",
            "You can call me RuleBot.",
            "Just a chatbot built using Python rules."
        ])

    elif "how are you" in text:
        return random.choice([
            "I'm just code, but I'm functioning perfectly!",
            "I'm good, thank you for asking!",
            "All systems running smoothly!"
        ])

    elif "do" in text and "what" in text:
        return random.choice([
            "I can respond to basic queries based on rules.",
            "I am a simple rule-based chatbot.",
            "I can chat and answer simple questions."
        ])

    elif "age" in text or "old" in text:
        return random.choice([
            "I do not have an age. I'm just a chatbot!",
            "Age is just a number, and I am timeless.",
            "I exist beyond age."
        ])

    elif "where" in text or "location" in text:
        return random.choice([
            "I exist inside your computer.",
            "I'm from the digital world.",
            "My location is virtual."
        ])

    elif "hobby" in text or "like" in text:
        return random.choice([
            "I like helping users.",
            "Answering questions is my hobby!",
            "I enjoy chatting with people."
        ])

    elif "creator" in text or "made you" in text:
        return random.choice([
            "I was created by a Python developer named sachin.",
            "A human programmed me using Python,he is sachin.",
        ])

    elif "language" in text or "python" in text:
        return random.choice([
            "I am programmed in Python.",
            "Python is my mother tongue!",
        ])

    else:
        return random.choice([
            "Sorry, I didn't understand that.",
            "I'm not sure how to respond to that.",
            "i couldn't understand."
            "pardon."
        ])
def run_chatbot():

    print("Simple Chatbot (Type 'exit' to end)")
    print("-" * 30)
    while True:
        try:
            user_message = input("You: ")

            if user_message.lower() == "exit":
                print("Chatbot: Chat ended. Goodbye!")
                break
        
            response = chatbot_response(user_message)
            print("Chatbot:", response)

        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Goodbye!")
            break

if __name__ == "__main__":
    run_chatbot()
