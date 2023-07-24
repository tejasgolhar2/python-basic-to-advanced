#   Implement a while loop which gets continuously username
# from console by using input function and terminates when
# the input is equal to "test".

username = "test"

name = input("Enter username: ")

while name != username:
    name = input("Enter username: ")
