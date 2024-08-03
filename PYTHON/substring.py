string="hello python programming"
sub='python'
words=string.split(' ')
for i in words:
    if i==sub:
        print("sub string present")
        flag=1
        break
else:
    print("sub string is not present")