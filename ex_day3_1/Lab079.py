my_shopping_list = ["bread","milk","butter"]
print(my_shopping_list[1])
print(len(my_shopping_list))

def bring_more_food(my_shopping_list):
    more_item = input("Enter the item\n")
    my_shopping_list.append(more_item)
    # my_list.remove(more_item)
    # my_list.insert(0, more_item)
    return my_shopping_list


l = bring_more_food(my_shopping_list)
print(l)