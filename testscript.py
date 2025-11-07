import os

if os.name == 'nt':  # For Windows
    os.system('cls')
else:  # For macOS and Linux
    os.system('clear')

list = ['epstien', 'diddy', 'donald j pump', 'joe bidet', 'zohran mamadani', 'obama', 'stephen gobdflok hawking']
print(', '.join(list))

while True:
    remove_who = input("what person would you like to remove from the epstien list? To exit the loop, enter \"exit\". ")
    if remove_who == "exit":
        break
    elif len(list) == 0:
        break
    else:
        if remove_who in list:
            list.remove(remove_who)
            print(', '.join(list))
        else:
            print('vorp?')
            break