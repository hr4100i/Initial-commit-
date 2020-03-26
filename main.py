username = input("Enter your user ID\n")
password = input("Enter your password\n")
file = open("StudentVoters.txt", "r")
for line in file:
    if line.split(",")[0] == username and line.split(",")[1] == password:
        print("Welcome %s" % username)
    else:
        print("Username or password invalid")
file.close()

# OR ALTERNATIVELY SOMETHING LIKE THIS:
username = input("Enter your user ID")
password = input("Enter your password")
with open("StudentVoters.txt", "r") as file:
    for line in file:
        if (username + "," +password + "\n") in file.readlines()
            print("Welcome %s" % username)
        else:
        print("Username or password invalid")



