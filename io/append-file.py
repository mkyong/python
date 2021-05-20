filename="c:\\Users\\mkyong\\projects\\python\\io\\file-new.txt"

# append to a file
with open(filename, 'a') as f:
    f.write("a new line")
    f.readlines()

# read and append to a file, a+  
# with open(filename, 'a+') as f:
#    f.seek(0)                      # a+ file pointer at end, move to beginning
#    lines = f.readlines()
#    f.write("\n" + str(len(lines))) # append number of lines to a file       