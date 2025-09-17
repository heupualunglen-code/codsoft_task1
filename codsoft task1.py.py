import re

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Pattern matching using regular expressions
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', user_input):
        return "Hey there, curious soul! What brings you to my digital lair?"

    elif re.search(r'\bhow are you\b|\bhow was your day\b', user_input):
        return "I'm 100% electric and 0% emotional, but thanks for asking! How about you?"

    elif re.search(r'\bwhat is your name\b|\bwho are you\b', user_input):
        return "I'm Bytey McBotface, your semi-sentient sidekick. Catchy, right?"

    elif re.search(r'\bweather\b', user_input):
        return "I’d love to tell you the weather, but I left my satellite in my other codebase."

    elif re.search(r'\bjoke\b|\bfunny\b', user_input):
        return "Why did the computer go to therapy? It had too many unresolved issues."

    elif re.search(r'\bbye\b|\bexit\b|\bquit\b', user_input):
        return "Logging off with style. Catch you in the next simulation!"

    else:
        return "Hmm... I don't quite compute that. Try asking me something else or teach me a new trick!"

print("🤖 Chatbot Activated! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    if "bye" in user_input.lower():
        break