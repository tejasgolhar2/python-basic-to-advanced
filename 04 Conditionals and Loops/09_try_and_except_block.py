# IMPLEMENTATION OF TRY AND EXCEPT

print("Wel-Come to the Mortgage Eligibility Calculator")

try:  # below lines will be checked that will cause error or not
    salary = int(input("Enter your salary:\n$ "))

except:  # the below lines gives the resoltion of error by re-entry of data or necesarry logic changes
         # different exception blocks depending upon the type of error can be defined this block
    print("Please enter valid format")
    salary = int(input("Enter your salary:\n$ "))

else:  # the below code is subjected to execution when the try ans except blocks are surpassed
    rate = 0

    if salary >= 2000:
        print("You are eligible to get mortgage")

        score = int(input("Enter yout Credit Score : \n"))
        
        pwd = input("Are you a Person With Disablity ? Y/N \n")

        if score >= 800:
            rate = 4
            if pwd == "Y":
                rate -= 2
                print(f"Interest Rate on mortgage {rate}%")
            else:
                print(f"Interest Rate on mortgage {rate}%")
        elif (score >= 650) and (score <= 799):  #  <<<<<<--------   USE OF LOGICAL AND
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

finally:  # this is the sure block that will get executed after the else then whatever be the status of the results
    print("Thank You for using our calculator")
