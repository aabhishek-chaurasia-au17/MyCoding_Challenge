# Take a name, age and whether user has diabetes as user input and tell them from when can they start taking vaccines 
# for COVID-19. [Hint: you can refer to the news for the timelines for each age group]

name = input("Enter your name : ")
age = int(input("Enter your age : "))
disease = input("Do you have diabetes type yes Or no : ")


if age >= 45:
    print( name , "you can take vaccines your eligible")

elif age < 45 and disease == "yes":
        print(name, "your eligible for vaccine")
        print("Because you have diabetes")

elif age > 45 or (age >= 18 and disease == "no"):
        print("you Can Take Vaccines in May") 

else:
    print("Wait until further notice \n now you are not eligible")       
