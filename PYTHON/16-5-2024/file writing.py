# f=open("16-5-2024/file.txt",'w')
# f.write("python is great language\n yeah its great !!\n")
# f.close()



# f=open("16-5-2024/file.txt",'wb')
# data=b"Hello world"
# f.write(data)
# f.close()



# f=open("16-5-2024/file.txt",'a')
# text="python is better than java"
# f.write(text)
# f.close()


f=open("16-5-2024/file.txt",'w+')
f.write("this is a cat race")
f.seek(10,0)
data=f.read(3)
f.seek(10,0)
f.write('cat')
f.close()