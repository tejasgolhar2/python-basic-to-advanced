# program to declare class time having data member as hrs, min, sec. Write a
# constructor to accept data and use display function for two objects

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hrs = hours
        self.min = minutes
        self.sec = seconds

    def display(self):
        print(f"{self.hrs:02d}:{self.min:02d}:{self.sec:02d}")

# Creating two Time objects
time1 = Time(10, 30, 45)
time2 = Time(4, 15, 20)

# Displaying the time for each object
print("Time 1:")
time1.display()

print("\nTime 2:")
time2.display()
