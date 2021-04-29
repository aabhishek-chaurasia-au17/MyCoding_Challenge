# Using break/continue on a nested loops of days and weeks (which you
# take as user input), encounter the scenario where we miss the first 2
# classes ever and still complete the syllabus one week before the end.

week = int(input("enter Week : "))
day = int(input("enter Day : "))

# using break

print("\nBreak Use Is start Here \n")

for x in range(1,week):
    for y in range(1,day):
        if x == 1 and y <= 2:
            break
        print( "week", x, "day", y)


print("\nBreak Use Is End Here \n")

print("Continue Use Is start Here \n")

# using continue

for i in range(1,week):
    for j in range(1,day):
        if i == 1 and j <= 2:
            continue
        print( "week", i, "day", j)

print("\nContinue Use Is End Here \n")