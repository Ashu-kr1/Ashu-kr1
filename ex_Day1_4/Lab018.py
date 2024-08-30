# Escape Sequence
print("Hello world")
print("Hello \nworld") #\n newline
print("Hello \tworld") #\t tabline
print("Hello \b world") #\t backspace

# dir = 'C:\pramod\n.txt'
# dir = "C:\pramod\n.txt"
# Where this r concept will be used?
# Automation API, Web Automation, file_path = r concept
dir = r"C:\pramod\n.txt"
dir2 = r'C:\pramod\n.txt'
print(dir)
print(dir2)

file_path = "C:\\Users\\u1113127\\Downloads\\testpython.txt"

with open(file_path,'r') as file:
    content=file.read()
    print(content)
