
def Item_view():

    print("---------------   View Item   -----------------------")

    with open ("item_list.txt","r") as file_reader:
      products = file_reader.readlines()
      for index,singal_product in  enumerate(products,start = 1):
          name = singal_product.split(",")
          print(f"Item_index : {index}")
          print(f" Name : {name[0]} \n Quality : {name[1]} \n Price ($) : {name[2]}")

def Add_item():
    
    print("---------------   Add Item   -----------------------")
    print(" fill the form ")
    try:
        with open ("item_list.txt",'x') :
            pass
    except Exception as e:
        pass

    item_name = input(" Item_Name : ")
    item_quality = input(" Item_quality : ")
    item_price = input(" Item_price : ")


    with open ("item_list.txt",'a') as file_writer :
        file_writer.write(f"{item_name},{ item_quality},{item_price}, \n")

    print("Congulation your item add in our gerosary Store")

def Search_items ():
    print("---------------   Search Item   -----------------------")
    Item_Name = input("Enter item Name : ")
    lop = False
    with open ("item_list.txt","r") as file_reader:
      products = file_reader.readlines()
      for singal_product in  products:
          name = singal_product.split(",")
          if  Item_Name ==  name[0]:
            lop = True
            print(f" Name : {name[0]} \n Quality : {name[1]} \n Price ($) : {name[2]}")
      if   lop != True:
          print("item is not found")

def Purchase_item():
    Item_view()
    print("---------------   Purchase Item   -----------------------")
    lop = True
    item_list = []
    while lop:
        name_item = input("Enter item name : ")
        with open ("item_list.txt","r") as file_reader :
            data_file  = file_reader.readlines()
            for data in data_file:
                data  = data.split(",") 
                if data[0].lower() == name_item:
                    item_list.append(data[2])
                    print(item_list)
            user_input = input("You want purchase someting more? : ")
            if user_input.lower() == "y":
                    lop = True
            else:
                    lop = False 
    
    bill = 0
    for item in item_list:
            bill = bill + int(item)
    print(f"Your Bill is {bill}$")
    card_details = input("Enter your card Number : ")
    print("Thank you for shopping with us!")  

def Edit_item(): 
            Item_view()
            print("---------------   Edit Item   -----------------------")
            index = int(input("Enter Item_index : "))
            print(" fill the form ")
            item_name = input(" Item_Name : ")
            item_quality = input(" Item_quality : ")
            item_price = input(" Item_price : ")
            with open ("item_list.txt") as file:
                lines =  file.readlines()
                del lines[index-1]
                with open ("item_list.txt","w") as file_write:
                     for line in lines:
                        file_write.write(line) 
                with open ("item_list.txt","a") as file_append:
                     file_append.write(f"{item_name},{item_quality},{item_price},\n")
            
def Exit():
           print("---------   Thanks for visiting us   -----------")
           exit()




print("---------------   Welcome to our Gerosary Store   -----------------------")
while True:
        print(" Please Chose What you want : ")
        print(  " 1- view items  \n" 
                " 2- add item for sale  \n" 
                " 3- purchase item  \n" 
                " 4- Search item   \n" 
                " 5- Edit Item \n" 
                " 6- Exist"
                )

        user_choise = int(input("Enter Your choice : "))
        if user_choise == 1:
            Item_view()
        elif user_choise == 2:
            Add_item()
        elif user_choise == 3:
            Purchase_item()
        elif user_choise == 4:
            Search_items ()
        elif user_choise == 5:
            Edit_item()
        elif user_choise == 6:
             Exit()
