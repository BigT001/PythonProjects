#collect emial from user
#split the email using the @. The first part will be the username and the second part is the doman.

def split():
    print("Welcome to email spliter!" "\n")

    input_email = input("Enter your email address (or type 'Exit' to end): ")

    if input_email.lower() == 'exit':
        return True

    components = input_email.split("@")

    if len(components) == 2:
        username, rest = components
        domain, extension = rest.split(".", 1)

        print("username :", username)
        print("domain: ", domain)
        print("extension: ", extension)
        print("")
        return False

    else:
        print("Invalid email address format. please try again or type 'exit' to end.")
        return False

while True:
     should_exit = split()
     if should_exit:
         print("Exiting splitter...")
         break

     user_input = input("Do you want to split another email? (yes/no): ")
     if user_input.lower() != "yes":
         confirm_exit = input("Are you sure you want to exit spliter?...(yes/no)")

         if confirm_exit.lower() == "yes":
            print("Exiting splitter...")
            break