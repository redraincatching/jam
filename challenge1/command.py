def hello(message):
    original_message = message
    team = {
        "eidhne":"message 1",
        "emy":"message 2",
        "oisin":"message 3",
        "ronan":"message 4"
    }
    # challenge 1.1: returns the message "hello, cisco!"
    # challenge 1.2: if message after hello > 0, return "hello, cisco!"
    # challenge 1.3: reply to ceo chuck robbins
    if(len(message) == 0): # Challenge 1.1
        message = "Hello, cisco!"
    # Challenge 1.3
    elif(message.lower() == "chuck robbins"):
        message = "Hello, cisco's favourite ceo "+message+"!"
    # challenge 1.5
    elif(sorted(message.lower()) == sorted("cisco")):
        message = "Hello, Cisco in Disguise!"
    # challenge 1.4
    for i in team:
        if (message.lower() in team):
            message = team[message]

    if(len(original_message) > 0 and message == original_message): # Challenge 1.2, this one checks last
        message = "Hello, "+original_message+"!"   

    # message = "hello, cisco!"
    # return message
    # no need for any input checks as input does not matter

    return message
