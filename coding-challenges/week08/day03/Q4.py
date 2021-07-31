input1=list(map(int,input("Enter the list = ").split()))
length=len(input1)
for i in range(length//2):
    input1[i],input1[length-1-i]=input1[length-1-i],input1[i]
print(input1)
