# Code to Encrypt the given message

def encrypt(v_msg,v_shift):
    res = ""
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for char in v_msg:
        if char in alpha:
            index = alpha.index(char)
            if index <= 25 - v_shift:
                res = res + alpha[index+v_shift]
            else:
                res = res + alpha[26 - index - v_shift ]
        else:
            if char == " ":
                res = res + " "
            else:
                res = res + char
    return res

message = input("Enter the message to be encrypted: ").upper()
shift = int(input("Shift number = "))
print(encrypt(message,shift))