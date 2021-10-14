string = "abce"
vowel = {"a":True, "e":True,"i":True,"o":True, "u":True}
count = 0

for i in range(len(string)):
    if string[i] in vowel:
        count = count + (len(string) - i)

print(count)


# abce
