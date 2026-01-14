#file handing
f=open("file")
print(f.read())
f.close()

t=open("file2","a")
t.close()
f.write("more content")
with open("file2") ad t:
print(f.read(4))
