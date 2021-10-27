import os, sys

print(os.environ['HOME']) 
print(os.environ.get('HOME'))
print(os.getenv('HOME'))

# get a specified environment variable
# If the key does not exists, raise KeyError(key) from None
# print(os.environ['HOME'])

#try:  
#    os.environ['PYTHON_HOME']
#except KeyError: 
#    print('Please define the environment variable PYTHON_HOME')
#    sys.exit(1)

# if the key does not exist, it returns `None` or default value.
# print(os.getenv('HOME', '/home/work/python'))
# print(os.environ.get('HOME', '/home/work/python'))

#print everything
#for key, value in sorted(os.environ.items()):
#    print('{}: {}'.format(key, value))


#print everything, sorted
# for key, value in sorted(os.environ.items()):
#    print('{}: {}'.format(key, value))