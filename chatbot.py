import random

# Define responses for the chatbot
responses = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm good, thanks!", "Feeling great!", "I'm doing well."],
    "travel": ["Sure, I can help you with that! What is your budget?", "Where would you like to travel?", "Tell me more about your travel interests."],
    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm still learning."]
}

def get_response(user_input):
    """
    Get a response from the chatbot based on the user input.
    """
    user_input = user_input.lower()

    for keyword, response_list in responses.items():
        if keyword in user_input:
            return random.choice(response_list)

    return random.choice(responses["default"])

def main():
    """
    Main function to run the chatbot.
    """
    print("Chatbot: Hi, I'm a Ntravel chatbot. How can I assist you?")
    
    collecting_travel_info = False
    budget = ""
    interest = ""
    destination = ""
    
    while True:
        user_input = input("You: ")
        
        if collecting_travel_info:
            if not budget:
                budget = user_input
                print("Chatbot: Great! What are your travel interests?")
            elif not interest:
                interest = user_input
                print("Chatbot: Sounds interesting! Where would you like to travel?")
            elif not destination:
                destination = user_input
                print(f"Chatbot: Awesome! I will help you plan your trip with a budget of {budget}, interest in {interest}, and destination {destination}.")
                break
        else:
            if user_input.lower() == "bye":
                print("Chatbot: Goodbye!")
                break
            elif "travel" in user_input.lower():
                collecting_travel_info = True
            
            response = get_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
