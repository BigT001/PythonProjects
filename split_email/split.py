#collect emial from user
#split the email using the @. The first part will be the username and the second part is the doman.

def split():
    print("Welcome to email spliter!" "\n")
   # print("")

    input_email = input("Enter your email address: ")

    components = input_email.split("@")

    if len(components) == 2:
        username, rest = components
        domain, extension = rest.split(".", 1)

        print("username :", username)
        print("domain: ", domain)
        print("extension: ", extension)
        print("")

    else:
        print("Invalid email address format. please try again.")

while True:
     split()