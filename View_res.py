from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DB_Connect import DB_Connect
db_connect = DB_Connect()

class  View_form:
    def __init__(self):
        self.root = Tk()
        T_view = ttk.Treeview(self.root)
        T_view.pack()
        T_view.heading('#0',text='ID')
        T_view.configure(column=('#Name','#Gender','#Commend'))
        T_view.heading('#Name', text='Name')
        T_view.heading('#Gender', text='Gender')
        T_view.heading('#Commend', text='Commend')
        self._dbconnect = DB_Connect()
        cursor = self._dbconnect.view()
        for row in cursor:
            T_view.insert('','end','#{}'.format(row['ID']),text=row['ID'])
            T_view.set('#{}'.format(row['ID']),'#Name',row['Name'])
            T_view.set('#{}'.format(row['ID']), '#Gender', row['Gender'])
            T_view.set('#{}'.format(row['ID']), '#Commend', row['Commend'])


        self.root.mainloop()

