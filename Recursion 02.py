# Recursive 02

def main():
    #By passing the argument 5 to the message
    # Function we are telling it to display the
    # message five times:
    message(5)


def message(times):
    if times > 0:
        print("This is a recursive function")
        message(times - 1)



#call the main function
main()
