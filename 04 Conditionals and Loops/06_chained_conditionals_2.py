print("Wel-Come to the Mortgage Eligibility Calculator")
salary = float(input("Enter yout salary in an integral format:\n$ "))

if salary>=2000:
    print("You are eligible to get mortgage")

    score = float(input("Enter yout Credit Score : \n"))
    if score>=800:
        print("Interest Rate on mortgage 4%")
    elif (score>=650)and(score<=799):
        print("Interest Rate on mortgage 6%")
    else:
        print("Interest Rate on mortgage 8%")


else:
    print("OOps! You are not eligible for mortgage")