"""
PASS Keyword
    In Python, the pass keyword is a placeholder statement that does nothing. 

    It is used when a statement is syntactically required, but you don't want 
to add any code or functionality to it at the moment.

    The pass statement is often used as a temporary placeholder when you are 
writing code and need a valid statement syntactically, but you haven't yet 
implemented the logic or functionality. 
    
    It allows you to bypass the requirement of having a blank block and 
ensures that your code remains valid.

Common use cases of Pass keyword
 
    1.Empty Function or Class Definition  
    2. Placeholder in a Conditional Statement
    3. Placeholder in a Loop
"""
age = int(input("Enter your age:\n"))
if age > 18:
    pass

else:
    print("Sorry ! You are not eligible for voting!")
