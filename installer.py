from Tkinter import *
import Tkinter
import tkMessageBox

window = Tkinter.Tk()

window.title("Mac Installer")
window.geometry("300x300")

MSOffice = IntVar()
Pitt_Printing = IntVar()
Malwarebytes = IntVar()

box1 = Checkbutton(window, text = "Microsoft Office", variable = MSOffice, onvalue = 1, offvalue = 0)
box2 = Checkbutton(window, text = "Pitt ", variable = Pitt_Printing)
box3 = Checkbutton(window, text = "Malwarebytes", variable = Malwarebytes)

# ------ Below is just a demonstration/reference of how to check the values of the checkbuttons ------ #
def run():
    if MSOffice.get() == 1: 
        # install Office
# -----------------------------------------------------------------------------------------------------#        

run_button = Tkinter.Button(window, text = "Install", command = run)

box1.grid(sticky = "W", row = 0, column = 0)
box2.grid(sticky = "W", row = 1, column = 0)
box3.grid(sticky = "W", row = 2, column = 0)

run_button.grid(sticky = "W", row = 3, column = 0)

window.mainloop()







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
