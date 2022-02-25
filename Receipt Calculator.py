"""
Program name: Receipt generator
Author: Jacob Johnson
Description: 
This program gets user input for entering an item, how many they want to buy, and how much they cost
The program will aggregate all the data and save it to a file to be named by the user.
If the user spends over 100 dollars, a 10% discount will be added.
Other info will be added as more is known

have use name file
open file
write each line to file
close file
total everything
calculate stuff... work out tax and discounts
Print information and save to file.

Known bugs:
currently does not have exceptions built in for data entered incorrectly.
For example, if someone accidentally enters a string value
when the program expects an integer, the program throws an error and closes
"""
#function to concatenate user inputs
def receipt (item_name, item_quantity, item_price, total_price):
    item_info = str(item_name) + ", "+ \
    str(item_quantity) + ", $" + format(item_price, "2f") + \
    ", $" + format(total_price, ".2f")
    return item_info

r_list = [] #empty list to store receipt info.
##I used "r" because I don't believe in my ability to accurately spell receipt over and over again

totals= 0.0 #empty variable used to store total dollars spent by user
tax_rate = 0.08 #arbitrary tax rate

run_again = "yes" #variable that initiates the WHILE loop at line 12

r_file = input("What would you like to call the file where you're receipt will be saved? ") #get name of file
r_file += ".txt" #append .txt to end of file name.

write_file = open(r_file, "w") #opening the file that we want to write in

while run_again == "yes" or run_again == "y": #start loop
    item_name = input("Enter the name of your item: ") #user names the tool they bought
    item_quantity = int(input("Enter the number of items you want: ")) #user enters the number of items they bought
    item_price = float(input("Enter the cost of each item: $")) #user enters the number 
    total_price = item_price * item_quantity #calcualtes price of total number of items
    totals =+ total_price #adds the price to the cummulative price variable
    line_item = receipt(item_name, item_quantity, item_price, total_price) #adds all user input to a variable to be stored
    write_file.write(item_name + ", "+ str(item_quantity) + ", " + str(item_price) + ", "+ str(total_price))
    r_list.append(line_item) #adds receipt line to the list
    print("Name of item: " + item_name)
    print("Number of items: " + str(item_quantity))
    print("Cost per item: " + str(item_price))
    print("Total Cost: " + str(total_price))
    loop_var =input("Would you like to enter another item? Yes or No: ") #user input determines whether or not to continue adding items to r_
    if loop_var.lower() == "yes" or loop_var == "y" :
        run_again = "yes" #continues loop
        #print("Name of Item: " + str(item_name) + ", " + "Number of items purchased: " + str(item_quantity) + ", " \
        # "Price : $" + str(item_price) + ", " + "Extended Price : $" + str(total_price) )
    else:
        run_again = "anything but yes" #breaks while loop
        print("Total Sales: $" + str(totals))

if total_price > 100: #calculate and subtract 10% sale
    total_price = total_price- (total_price * 0.1)
    total_price = total_price + (total_price * tax_rate)
    print("Here is your total cost with a 10% discount for spending over $100: $" + str(total_price))
else:
    total_price = total_price + (total_price * tax_rate)
    print("The total cost of your order is: $" + str(total_price))
write_file.close()
