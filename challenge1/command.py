
def hello(message):
    cisco = "cisco"
    team = {
        "eidhne":"message 1",
        "emy":"message2",
        "oisin":"message3",
        "ronan":"message4"
    }
    # challenge 1.1: returns the message "hello, cisco!"
    # challenge 1.2: if message after hello > 0, return "hello, cisco!"
    # challenge 1.3: reply to ceo chuck robbins
    if(len(message) == 0): # Challenge 1.1
         message = "Hello, cisco!"
    # Challenge 1.3
    elif(message.lower() == "chuck robbins"):
        message = "Hello, cisco's favourite ceo "+message+"!"
    elif(len(message) > 0): # Challenge 1.2
        message = "Hello, "+message+"!"
    # challenge 1.4
    for i in team:
        if (message.lower() in team):
            message = team[message]
    #Challenge 1.5
    # elif(len(message) == len(cisco)): 
	#     if(sorted(message.lower()) == sorted(cisco.lower())):
	#     	message = "Hello, Cisco in Disguise!"
            
    


    # message = "hello, cisco!"
    # return message
    # no need for any input checks as input does not matter

    

    return message
