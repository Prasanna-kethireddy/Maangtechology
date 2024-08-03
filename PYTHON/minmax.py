def find(num):
    max=num[0]
    n=len(num)
    for i in range(1,n):
        if num[i]>max:
            max=num[i]
    print('max value is ',max)
    
#for min 
    min=num[0]
    for i in range(1,n):
        if num[i]<min:
            min=num[i]
    print("min value is ",min)

f=input("Enter the numbers with space : ")
num=list(map(int,f.split()))
print(find(num))

# list=[12,1,3,4,5,22,89,100,34,27,85,36]
# list.sort()
# print(list)
# print("smallest value is ",list[0])
# print("largest value is ",list[-1])

# list=[12,1,3,4,5,22,89,100,34,27,85,36]
# print("smallest",min(list))
# print("largest",max(list))