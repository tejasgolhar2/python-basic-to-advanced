def encrypt(e_msg,e_shift):
    res = ""
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for char in e_msg:
        if char in alpha:
            index = alpha.index(char)
            
            # Approach 1 - For Index number greater than 25
            if index <= 25 - e_shift:
                res = res + alpha[index+e_shift]
            else:
                res = res + alpha[26 - index - e_shift ]

            # Approach 2 - For index number greater than 25
            # while index>25:
            #     index = index - 26
            # res = res + alpha[index+v_shift]
        else:
            res = res + char
    return res

def decrypt(d_msg,d_shift):
    res1 = ""
    alpha1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for char in d_msg:
        if char in alpha1:
            index = alpha1.index(char)
            while index>25:
                index =  index - 26
            res1 = res1 + alpha1[index-d_shift]
        else:
            res1 = res1 + char
    return res1

flag = False
while not flag:
    choice = input("Enter 'E' to encypt or 'D' to decrypt\n")
    message = input("Enter the message: ").upper()
    shift = int(input("Enter the shift number: "))
    if choice=='E':
        encrypt_msg = encrypt(message,shift)
        print("Encrypted Message:",encrypt_msg)
    else:
        decrypt_msg = decrypt(message,shift)
        print("Decrypted Message:",decrypt_msg)
        
    cont = input("Enter 'Y' to continue or enter 'N' to exit\n")
    if cont=='N':
        flag=True
        print("Thank You for using the program")
