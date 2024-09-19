a,b,c = (10,20,12)
print(a)
print(b)
print(c)

#Search in Tuple:
cities=("London","Paris","Los Angles","Tokyo")
print("Paris" in cities)
print("Delhi" in cities)

t = (12,34,56)
# t.append(12) # r: 'tuple' object has no attribute 'append'
print(t)
mylist = list(t)
mylist.append(12)
t=tuple(mylist)
print(f"after tuple is changed into the list and vice versa{t}")

tuplx = (12,65,61,43)
tuplx = tuplx+(54,)
print(tuplx)

ENv_API_urls =tuple(["abc.com/get","xyz.com/post","qwe.com/put"])
print(ENv_API_urls[2])