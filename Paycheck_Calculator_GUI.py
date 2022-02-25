"""
Program # 6
Jacob Johnson
This program will use a GUI window to collect data from the user
to calculate their wages and save them to a file.

When the program is started the user will enter the name of the file where their information will be saved
as well as where it will be saved. 

The data will be used to calculate user pay based on hours worked and their hourly rate
The program will take overtime into account and adjust hourly rate by x1.5 if necessary
The program will save the collected and calculated data to a file to be named by the user
"""

from tkinter import * #imports needed elements for GUI
from tkinter import filedialog #imports file dialog
import os #imports operating system support for GUI components


# function to calculate wages for regular AND overtime
def paycheck():
    first_name = str(f_name.get())
    last_name = str(l_name.get())
    worked_hours = float(hours.get())
    pay_rate = float(rate.get())
    if worked_hours <= 40: #if employee works 40 or fewer hours
        wage = format(worked_hours * pay_rate, ".2f")
    elif worked_hours > 40: # if employee works more than 40 hours
        wage = format(((worked_hours-40)*pay_rate*1.5)+pay_rate*40, ".2f")
    content.configure(text = "$" + wage)
    new_file.write(first_name + ", " + last_name + ", " + str(worked_hours) + " hours worked , $" + str(pay_rate) + " per hour, $" + str(wage) + " total pay\n") #writes data to file
    hours.delete(0, END)
    rate.delete(0, END)
    return wage

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
    f_name.delete(0, END) #Clears the contents of the first name textbox
    l_name.delete(0, END) #Clears the contents of the last name textbox
    
"""
Below is the main program.
First the program window is created,
next the GUI objects in the window are defined,
and last there is code that runs when the window is initialized and started.
"""

#Creates and sizes program main window

window = Tk() #Creates the GIU Window object and names it

window.title("Wage Calculator") #Creates a title for the GUI window

window.geometry("800x400") #Specifies the window size

#Create labels

#Label to display content in list form

content = Label(window, text = "Intentionally Blank" ,relief = SUNKEN, width = 20, height = 10, wraplength = 100, anchor = NW, justify = LEFT)

content.grid(column = 0, row = 10) #label position

#label for first name
f_name = Label(window, text = "Enter First Name" ,relief = SUNKEN, width = 36, justify =RIGHT)
f_name.grid(column = 0, row = 3)#label position

#label for last name
l_name = Label(window, text= "Enter Last Name", relief = SUNKEN, width = 36, justify =RIGHT)
l_name.grid(column = 0, row = 4)#label position

#label for hours
hours= Label(window, text = "Enter Hours Worked", relief = SUNKEN, width = 36, justify =RIGHT)
hours.grid(column = 0, row = 5)#label position

#label for rate
rate = Label(window, text= "Enter Rate of Pay", relief = SUNKEN, width = 36, justify =RIGHT)
rate.grid(column = 0, row = 6)#label position

#Create Textboxes

#Textbox to collect employee first name
f_name = Entry(window, width = 20)

#Textbox to collect employees last name
l_name = Entry(window, width = 20)

#Textbox to collect hours worked
hours = Entry(window, width = 20)

#Textbox to collect pay rate
rate = Entry(window, width = 20)

#Textbox positions
f_name.grid(column = 10, row = 3)
l_name.grid(column = 10, row = 4)
hours.grid(column = 10, row = 5)
rate.grid(column = 10, row = 6)


#Create Command Buttons

#Button to calculate wages
btn_calculate = Button(window, text = "Calculate Pay", command = paycheck)
btn_calculate.grid(column = 10, row = 7)

#Button to exit program and close the file
btn_exit = Button(window, text = "Close", command = kill)
btn_exit.grid(column = 10, row = 8)

#Button to clear names
btn_clear_names = Button(window, text = "Clear Names", command = clear_names)
btn_clear_names.grid(column = 40, row = 3)


"""
After the window is cerated and mainloop is called, this code executes once the window objects are created.
The window is created, the focus is set to a textbox,
and the file save function is called.
"""

#Sets focus on the first name text box
f_name.focus() #Creates a file after window is opened, by calling the FileSave function
window.after(1,file_save) #The after method runs 1 millisecond after the window is created

"""
This starts the program by invoking the main window's main loop above.
"""

window.mainloop()
