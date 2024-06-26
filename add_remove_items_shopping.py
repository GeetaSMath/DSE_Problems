shopping_list = ["milk", "eggs", "bread", "butter"]

def add_items(shopping_list,item):
            shopping_list.append(item)
            return shopping_list
#
def remove_items(shopping_list,item):
    try:
        if item not in shopping_list:
            raise ValueError ("items is not in cart")
        else:
            shopping_list.remove(item)
        return shopping_list
    except ValueError as e:
        print(e)
    return shopping_list

add_items_cart=add_items(shopping_list,"orange")
print(add_items_cart)
remove_items_cart=remove_items(shopping_list,"orange")
print(remove_items_cart)
