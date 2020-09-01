from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DB_Connect import DB_Connect
from View_res   import View_form


# DB
dbConnect = DB_Connect()

root = Tk()
root.title("Ticket Reservation")
root.configure(background="#f0b27a")

# style=
style = ttk.Style()
style.theme_use('classic')
style.configure('TLabel',background= "#f0b27a" )
style.configure('TButton',background= "#f0b27a" )
style.configure('TRadiobutton',background= "#f0b27a" )

#   FullName
ttk.Label(root,text="Full Name: ").grid(row=0, column=0, padx=10, pady=10)
#   Name Entry
EntryFullName = ttk.Entry(root, width = 30, font=('Arial', 16))
EntryFullName.grid(row= 0 , column=1, columnspan=2, pady=10 )

#   Gender
ttk.Label(root,text="Gender: ").grid(row=1, column=0, padx=10, pady=10)
# Radio male
SpanGender= StringVar()
ttk.Radiobutton(root, variable=SpanGender,value="Male", text="Male").grid(row=1, column=1)
ttk.Radiobutton(root, variable=SpanGender,value="Female", text="Female").grid(row=1, column=2 )
#   command
ttk.Label(root,text="Commands: ").grid(row=2, column=0, padx=10, pady=10)
#   Text command
Text_command = Text(root, width=30, height= 15, font=('Arial',16))
Text_command.grid(row=2, column=1, columnspan=2,pady=10)

# Buttons
buSub = ttk.Button(root, text= "Submit")
buSub.grid(row = 3, column=3)
buView = ttk.Button(root, text= "View Res.")
buView.grid(row = 3, column=2)


def  BuSubData():           # func  submit Button
     #print("FUllName: {}".format(EntryFullName.get()))
     #print("Gender: {}".format(SpanGender.get()))
     #print("Command: {}".format(Text_command.get(1.0,'end')))
     msg = dbConnect.Add(EntryFullName.get(),SpanGender.get(),Text_command.get(1.0,'end'))
     messagebox.showinfo(title="Show info",message=msg)
     EntryFullName.delete(0,'end')
     Text_command.delete(1.0,'end')



def   BuViewDATA():
    #TODO: show orders
    view_form = View_form()


buSub.config(command = BuSubData)
buView.config(command = BuViewDATA)


root.mainloop()

