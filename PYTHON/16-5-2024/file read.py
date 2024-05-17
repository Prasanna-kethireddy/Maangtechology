
# fo = open("16-5-2024/file.txt", "r")
# text = fo.read()
# print (text)


# fo.close()


fo=open("foo.txt","w+")
fo.write("This is a rat race")
fo.seek(10,0)
data=fo.read(3)
fo.seek(10,0)
fo.write('cat')
fo.seek(0,0)
data=fo.read()
print (data)
fo.close()