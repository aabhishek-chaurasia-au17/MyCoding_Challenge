'''
Q - 3) https://leetcode.com/problems/flipping-an-image/
'''


def Reverse(peti):
    for j in range(len(peti)) :
        if peti[j]=="0":
            peti[j]=1
        else:
            peti[j]=0
    peti.reverse()
    return peti


image=list(map(list,input("Enter the list = ").split()))
for i in range(len(image)):
    image[i]=Reverse(image[i])
print(image)

