#List
#List - Collections of items(Duplicate is allowed)
my_list = [1,2,3,2]
my_list2 = [1,True,"Pramod",12.26]

print(my_list)
print(my_list2)

print(my_list2[1])
print(my_list[3])

# print(my_list[10])  # list index out of range - exception

#Indexing
print("elemement at index - 0 is = ", my_list[0])
print("elemement at index - 1 is = ", my_list[1])
print("elemement at index - 2 is = ", my_list[2])

print(my_list)
for element in my_list:
    print(element)

for i in range(1,10):
    print(i,end="_")

list=list(range(1,11))
print(list)

#append()
# Append object to the end of the list.
my_list.append(11)
my_list2.append(5)

print(my_list)
print(my_list2)

#extend

my_list.extend([7,8])
print(my_list)

my_list2.extend([10])
print(len(my_list2))

#insert

# my_list2.index(1,"ashu")
# print(my_list2)

my_list.insert(1, "Dutta")
print(my_list)
print(len(my_list))

my_list2.insert(1,"Ashu")
print(my_list2)
#print(len(my_list2))

my_list[1]="Amit"
print(my_list)

my_list2.insert(-1,"Lucky")
print(my_list2)

#remove
my_list2.remove("Lucky")
print(my_list2)

# my_list.replace()
print(" --------------------------")
print(" --------------------------")

my_list2_list = my_list2.copy()
print(my_list2_list)

# Clear
#rint(my_list2_list.clear())



name = "Pramod"
name=name.upper()
print(name)

# For Loop
l1=[1,24,4]
l2=[31,43,32]
print(l1+l2)