#Shopping cart system 
items=[]

def add_item(item_name,bill):
        items.append({
            "items_name":item_name,
            "bill":bill

        })
        print("Item Added Successfully")
        return
    

def total_bill():
    total=0
    for item in items:
        total+=item["bill"]
        print("Total Bill Is",total)

def remove_item(item_name):
    for item in items:
         if item["items_name"]==item_name:
              items.remove(item)
              print("Successfully deleted")
              return
         
    print("No items with this name")

def view_items():
     if not items:
          print("There is no item in the cart")
          return
     
     print("-------Items List------")
     for item in items:
          print(item["items_name"],"-",item["bill"])
    
    
while True:
     print("1 / add item")
     print("2/ total bill")
     print("3/ remove item")
     print("4/ exit")
     print("5/ view items")

     choice=input("Enter your choice")

     if choice=="4" or choice=="exit":
          print("Program Ended")
          break

     elif choice=="1" or choice=="add item":
          item_name=input("Enter your item name")
          bill=int(input("Enter your bill"))
          add_item(item_name,bill)
    
     elif choice=="2" or choice=="total bill":
          total_bill()


     elif choice=="3" or choice== "remove item":
          item_name=input("Enter item name you want to delete")

          remove_item(item_name)

     elif choice=="5" or choice=="view items":
          view_items()
     


