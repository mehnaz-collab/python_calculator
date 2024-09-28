#define the menu of restron
menu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80,
    }
    
print("pizza:40\n pasta:50\n burger:60\n salad:70\n coffee:80")
print("welcome to mannnu reston")


order_total=0

item_1 = input("enter the name of item you want to order")
if item_1 in menu:
    order_total+= menu[item_1] #0 + 50
    print(f"your {item_1} has been added to your order")

else:
    print(f"ordered item {item_1} is not available yet")


if another_order =="yes":
    item_2=input("enter the nam of second item=")
    if item_2 in menu:
        order_total+= menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print("ordered {item_2} is not available! ")

print(f"the total amount of items is not available yet")