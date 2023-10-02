# Code to Encrypt the given message

def encrypt(v_msg,v_shift):
    res = ""
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for char in v_msg:
        if char in alpha:
            index = alpha.index(char)
            
            # Approach 1 - For Index number greater than 25
            if index <= 25 - v_shift:
                res = res + alpha[index+v_shift]
            else:
                res = res + alpha[26 - index - v_shift ]

            # Approach 2 - For index number greater than 25
            # while index>25:
            #     index = index - 26
            # res = res + alpha[index+v_shift]
        else:
            res = res + char
    print("The encrypted message is",res)

message = input("Enter the message to be encrypted: ").upper()
shift = int(input("Shift number = "))
encrypt(message,shift)