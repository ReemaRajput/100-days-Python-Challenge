with open('myfile.txt', 'r' ) as f:
          print(type(f))
        
          f.seek (19) #move to the 19th bytes in the file
        
          print(f.tell()) #tell you the current position in the byte
          data = f.read(7) # read the next 5 bytes
          print(data)
          
with open('myfile2.txt','w') as x:
    x.write("Reema Rajput")
    x.truncate(5) #allow only first 5 letters.
