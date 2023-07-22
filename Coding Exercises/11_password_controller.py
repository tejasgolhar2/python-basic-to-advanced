'''
    Create a function which takes string password as a parameter and 
    checks the length of password. If the length longer than 8 character 
    it returns True otherwise returns False.

'''
def password_controller(pass_w):
    if len(pass_w)>8:
        return True
    else:
        return False

val = input("")
result = password_controller(val)
print(result)