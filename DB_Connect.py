import sqlite3


class   DB_Connect:
        def    __init__(self):
            self._db = sqlite3.connect("Reservation.db")
            self._db.row_factory=sqlite3.Row   # Alaw to editing in db
            self._db.execute("create table if not exists Ticket(ID integer primary key autoincrement,Name text,Gender text, Commend text )")
            self._db.commit()   # Add it inside the db


        def Add(self,Name,Gender, Commend):
            self._db.execute("insert into Ticket(Name,Gender,Commend) values(?,?,?)",(Name,Gender,Commend))
            self._db.commit()
            return " request is submitted "

        def view(self):
            cursor = self._db.execute("Select * from Ticket")
            return cursor