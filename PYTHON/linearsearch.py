def linear(array,x):
    n=len(array)
    for i in range(0,n):
        if array[i]==x:
            return 'element at index' , i
    return 'element not found' 
input=input("Enter the elements :")
array=list(map(int,input.split()))
x=67
result=linear(array,x)
print(result)   