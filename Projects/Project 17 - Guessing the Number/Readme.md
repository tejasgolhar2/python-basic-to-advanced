# Guessing the Number

## Instruction


Create a program will generate a random number unknown to the user between upper and lower bond that user provided. The user needs to guess what that number is. If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear. 


> `Your program should ask for upper and lower bound from the user initially.` 

>   `Calculate chances of user based on upper and lower bounds.` 

>    `Based on calculated number of chances ask input from user for guessing the number.` 

> `If the guessed number is greater than the generated number then print - "You guessed too high", otherwise print - "You guessed too low". And finally if the numbers match print - "Congratulations you did it in"`

Output can be like this:

```
Enter Lower bound: 1
Enter Upper bound: 7

    You've only  3  chances to guess the integer!

Guess a number: 4
You Guessed too high!
Guess a number: 1
You guessed too small!
Guess a number: 2
Congratulations you did it in  3  try

The number is 2
    Better Luck Next time!

```

# Hint

- Log function from math module to calculate chances. (math.log(upper - lower + 1, 2))



# Solution

[https://replit.com/@AppMillers/Project-17-Guessing-the-Number-Solution](https://replit.com/@AppMillers/Project-17-Guessing-the-Number-Solution)