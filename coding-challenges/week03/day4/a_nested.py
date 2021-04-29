# Using break/continue on a nested loops of days and weeks (which you take as user input),
# skip out on the even days of all odd weeks.

week = int(input("enter Week : "))
day = int(input("enter Day : "))

# using break

print("\nBreak Use Is start Here \n")

for x in range(1,week):
    for y in range(1,day):
        if x % 2 == 1 or y % 2 == 0:
            break
        print( "week", x, "day", y)


print("\nBreak Use Is End Here \n")

print("Continue Use Is start Here \n")

# using continue

for i in range(1,week):
    for j in range(1,day):
        if i % 2 == 1 or j % 2 == 0:
            continue
        print( "week", i, "day", j)

print("\nContinue Use Is End Here \n")



