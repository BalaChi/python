
# by doing like above we hvae to close the file insted of this we can use below
# r+ is read and write
with open('test.txt',mode='w') as my_file: #-- stand way to read file
    text = my_file.write('(:') #it rewrites the content from index cursor 0 
    print(text)

# r+ - read,write -- over write the Index
# w - or py its a new file and write a new thing only what we wrote
# a -- append at last with existing not clearing any index

try:
    with open('./io\sad.txt',mode='r') as my_file1:
        # sad.txt test.txt
        # text1 = my_file1.write(':(')
        print(my_file1.read())
except FileNotFoundError as err:
    print("file dont exixt")
    raise err
except IOError as err1:
    print("io error")
    raise err1

