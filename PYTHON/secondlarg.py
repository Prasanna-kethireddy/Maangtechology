# list=[12,89,23,45,64,90,120,4,2,6]
# list.sort()
# print("second largest is ",list[-2])

def second(numbers):
    uniques=list(set(numbers))
    if len(uniques)<2:
        return None
    uniques.sort(reverse=True)
    return uniques[1]
input=input("enter the numbers with space: ")
numbers=list(map(int,input.split()))
print(second(numbers))
