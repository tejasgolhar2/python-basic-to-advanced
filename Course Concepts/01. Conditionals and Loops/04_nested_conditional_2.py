print("Wel-Come to the Mortgage Eligibility Calculator")
salary = float(input("Enter yout salary in an integral format:\n$ "))
rate = 0

if salary >= 2000:
    print("You are eligible to get mortgage")

    score = float(input("Enter yout Credit Score : \n"))
    pwd = input("Are you a Person With Disablity ? Y/N \n")

    if score >= 800:
        rate = 4
        if pwd == "Y":
            rate -= 2
            print(f"Interest Rate on mortgage {rate}%")
        else:
            print(f"Interest Rate on mortgage {rate}%")
    elif (score >= 650) and (score <= 799):
        rate = 6
        if pwd == "Y":
            rate -= 2
            print(f"Interest Rate on mortgage {rate}%")
        else:
            print(f"Interest Rate on mortgage {rate}%")
    else:
        rate = 8
        if pwd == "Y":
            rate -= 2
            print(f"Interest Rate on mortgage {rate}%")
        else:
            print(f"Interest Rate on mortgage {rate}%")


else:
    print("OOps! You are not eligible for mortgage")
