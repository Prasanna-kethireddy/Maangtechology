#computing all the permutations of a string .....example: prassu rassup assupr ssupra supras etc..
def get_permutation(string,i=0):
    if i==len(string):
        print("".join(string))
    for j in range(i, len(string)):
        words=[c for c in string]
        words[i],words[j]=words[j],words[i]
        get_permutation(words,i+1)
string =str(input("Enter the word for permutations:"))
get_permutation(string)
 