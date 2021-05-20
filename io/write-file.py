filename="c:\\Users\\mkyong\\projects\\python\\io\\file-new.txt"

# write to a file
# f = open(filename, 'w')
# f.write("test 1\n")
# f.write("test 2\n")
# f.close


# write to a file, with statement
with open(filename, 'w') as f:
    f.write("test 1\n")
    f.write("test 2\n")
    f.write("test 3\n")


# write multiple lines to a file
# data = ["test 1 \n", "test 2 \n", "test 3 \n"]
# with open(filename, 'w') as f:
#    f.writelines(data)


# working with two files
# source = filename
# target = 'file-modify.txt'
# with open(source, 'r') as input, open(target, 'w') as output:
#    lines = input.readlines()
#    output.writelines(lines[1:]) # skip the first line and write to output
    

# find and replace in a file
# with open(filename, 'r') as f:
#    lines = f.read()

#lines = lines.replace('test', 'hello')   # replace string

#with open(filename, 'w') as f:
#    f.write(lines)



# w+ reading and writing files
# with open(filename, 'w+') as f:
#    f.write("test 1\n")
#    f.write("test 2\n")
#    f.write("test 3\n")
#    f.seek(0)               # move to beginning of the file
#    lines = f.read()
#    print(lines)