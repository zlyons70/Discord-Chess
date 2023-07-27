def handle_response(message):
    p_message = message.lower()
    
    if p_message == "hello":
        return "Hello, how are you?"
    
    if p_message == "goodbye":
        return "Goodbye, it was nice talking to you."
    
    if p_message == "!help":
        return "help list"