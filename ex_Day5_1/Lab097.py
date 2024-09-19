squares =[1,4,9,16,25]
#List is Mutable in nature
#Mutable - Change

squares[3]=65
print(squares)

## Tuple
#Collections of Items:
my_tuple=(1,4,5,6,7,8)
print(f"This is tuple {my_tuple}")

#my_tuple[3] = 64 # Immutable in nature
print(my_tuple)

shopping_list=["Bread","Butter","Egg"]
shopping_list[2]="milk"
print(shopping_list)

## Real World Project
#thetestingacademy,sdet.live
my_tuple = ("thetestingacademy","sdet.live")
#Conversion
my_api_list = list(my_tuple)
print(my_api_list)

#Conversion
my_api_list=tuple(my_api_list)
print(my_api_list)

#Real case,where we Tuples
API_URLS = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestingacademy.com")
print(API_URLS[0])
print(API_URLS[1])