"""
Exam Program 2
Jacob Johnson
This program will use a GUI window to collect data from the user to create a receipt

The receipt will contain the name of an item, the quantity of an item, and the price of the item.
The program will calculate the total with tax and display the total.
The program will allow the user to create a file to store the contents of the receipt


"""

from tkinter import * #imports needed elements for GUI
from tkinter import filedialog #imports file dialog
import os #imports operating system support for GUI components
import receiptclass 

main_var = receiptclass.SalesReceipt()

# function to deal with the receipt

def add_receipt():
    main_var.itemName = str(item.get())
    main_var.itemQty = int(quant.get())
    main_var.itemPrice = float(price.get())
    main_var.ExtPrice()
    new_file.write(main_var.itemName + ", " + str(main_var.itemQty) + ", $" + str(format(main_var.itemPrice, ".2f") + "\n")) #writes data to file
    main_var.AddItem()
    content.configure(text = "Total price for Item: $ {0:.2f} \n Total Tax {1:.2f} \n Total Sales {2:.2f}".format(main_var.SaleTotal(), main_var.SalesTax(), main_var.FinalSaleAmt()))
    item.delete(0, END)
    quant.delete(0, END)
    price.delete(0, END)


#save file function
def file_save():
    window.filename = filedialog.asksaveasfilename(parent=window,
                                                       initialdir=os.getcwd(),
                                                       title="Please create a file name for your new file ",
                                                       filetypes = (("Text Files", "*.txt"), ("All Files", "*.*")))
    fileContents = window.filename + ".txt"
    global new_file
    new_file = open(fileContents, "w")
    content.configure(text = fileContents)

#close program function
def kill():
    new_file.close()
    window.destroy()

#clear names function
def clear_names():
    item.delete(0, END) #Clears the contents of the item textbox
    quant.delete(0, END) #Clears the contents of the item quantity textbox
    price.delete(0, END) #Clears the contents of the item price textbox
    
"""
Below is the main program.
First the program window is created,
next the GUI objects in the window are defined,
and last there is code that runs when the window is initialized and started.
"""

#Creates and sizes program main window

window = Tk() #Creates the GIU Window object and names it

window.title("Receipt Generator") #Creates a title for the GUI window

window.geometry("600x400") #Specifies the window size

#Create labels

#Label to display content in list form

content = Label(window, text = "Intentionally Blank" ,relief = SUNKEN, width = 40, height = 10, anchor = NW, justify = LEFT)

content.grid(column = 0, row = 10) #label position

#label for item name
item = Label(window, text = "Enter Item Name" , width = 24, justify =RIGHT)
item.grid(column = 0, row = 3)# item label position

#label for item quantity
quant = Label(window, text= "Enter Item Quantity", width = 24, justify =RIGHT)
quant.grid(column = 0, row = 4)# quantity label position

#label for hours
price= Label(window, text = "Enter Price of Item", width = 24, justify =RIGHT)
price.grid(column = 0, row = 5)# price label position

#label for total price


#label for total tax


#label for total sale



#Create Textboxes

#Textbox to collect item name
item = Entry(window, width = 20)

#Textbox to collect item quantity
quant = Entry(window, width = 20)

#Textbox to collect item price
price = Entry(window, width = 20)


#Textbox positions
item.grid(column = 10, row = 3)
quant.grid(column = 10, row = 4)
price.grid(column = 10, row = 5)


#Create Command Buttons

#Button to calculate wages
btn_calculate = Button(window, text = "Add to Receipt", command = add_receipt)
btn_calculate.grid(column = 10, row = 7)

#Button to exit program and close the file
btn_exit = Button(window, text = "Close Program", command = kill)
btn_exit.grid(column = 10, row = 8)

#Button to clear names
btn_clear = Button(window, text = " Clear Entries ", width = 20, height = 1, command = clear_names)
btn_clear.grid(column = 10, row = 1)


"""
After the window is cerated and mainloop is called, this code executes once the window objects are created.
The window is created, the focus is set to a textbox,
and the file save function is called.
"""

#Sets focus on the first name text box
item.focus() #Creates a file after window is opened, by calling the FileSave function
window.after(1,file_save) #The after method runs 1 millisecond after the window is created

"""
This starts the program by invoking the main window's main loop above.
"""

window.mainloop()


