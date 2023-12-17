#reading a file-r
x= open('myfile.txt','r')
text = x.read()
print(text)
x.close()

#w-write or create a new file 
f = open('myfile2.txt','w')
f.write("You are amazing")
f.close()

# a- append in a file 
f = open('myfile2.txt','a')
f.write("You are amazing")
f.close()

# With statement - you don't have to close the statement 
with open ('myfile.txt','a') as f:
    f.write('I am adding new stuff to the old one')
