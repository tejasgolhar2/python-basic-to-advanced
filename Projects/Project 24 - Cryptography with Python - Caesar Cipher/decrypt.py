def decrypt(v_msg,v_shift):
    res = ""
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for char in v_msg:
        if char in alpha:
            index = alpha.index(char)
            while index>25:
                index =  index - 26
            res = res + alpha[index-v_shift]
        else:
            res = res + char
    print("The decrypted message is",res)


msg = input("Enter the message to be decrypted: ").upper()
shift = int(input("Enter the shift value used for encryption: "))
decrypt(msg,shift)