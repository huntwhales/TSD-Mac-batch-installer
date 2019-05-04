from Tkinter import *
import Tkinter
import tkMessageBox

installer_window = Tkinter.Tk()

installer_window.title("Mac Installer")
installer_window.geometry("300x300")

MSOffice = IntVar()
Pitt_Printing = IntVar()
Malwarebytes = IntVar()

# ------ Below is just a demonstration/reference of how to check the values of the checkbuttons ------ #
def run():
    if MSOffice.get() == 1: 
        # install Office
        print("blah") # just so it runs
# -----------------------------------------------------------------------------------------------------#  
def select_all_standard():
	if (MSOffice.get() + Pitt_Printing.get() + Malwarebytes.get()) >= 1:
		MSOffice.set(0)
		Pitt_Printing.set(0)
		Malwarebytes.set(0)
	else:
		MSOffice.set(1)
		Pitt_Printing.set(1)
		Malwarebytes.set(1)

standard_programs_label = Label(installer_window, text = "Standard Pitt software", font = "TKDefaultFont 18 bold")
box1 = Checkbutton(installer_window, text = "Microsoft Office", variable = MSOffice, onvalue = 1, offvalue = 0)
box2 = Checkbutton(installer_window, text = "Pitt ", variable = Pitt_Printing)
box3 = Checkbutton(installer_window, text = "Malwarebytes", variable = Malwarebytes)
select_all_standard_button = Tkinter.Button(installer_window, text = "Select/deselect all", command = select_all_standard)
run_button = Tkinter.Button(installer_window, text = "Install", command = run)

standard_programs_label.grid(sticky = "W", row = 0, column = 0)
box1.grid(sticky = "W", row = 1, column = 0)
box2.grid(sticky = "W", row = 2, column = 0)
box3.grid(sticky = "W", row = 3, column = 0)
select_all_standard_button.grid(sticky = "W", row = 4, column = 0)
run_button.grid(sticky = "W", row = 5, column = 0)

installer_window.mainloop()







# ------- REFERENCE -------- #
# from Tkinter import *
# import tkMessageBox
# import Tkinter

# top = Tkinter.Tk()
# CheckVar1 = IntVar()
# CheckVar2 = IntVar()
# C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
#                  onvalue = 1, offvalue = 0, height=5, \
#                  width = 20)
# C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
#                  onvalue = 1, offvalue = 0, height=5, \
#                  width = 20)
# C1.pack()
# C2.pack()
# top.mainloop()
