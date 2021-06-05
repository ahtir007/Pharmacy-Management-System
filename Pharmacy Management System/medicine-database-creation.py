import sqlite3
import random


conn = sqlite3.connect('medicine.sqlite')
cur = conn.cursor()
cur.executescript('''
CREATE TABLE IF NOT EXISTS Medicines (
     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    Name TEXT,
    Salt TEXT ,
    Company,
    Quantity INTEGER,
    Weight INTEGER,
    Rateper REAL,
    uses TEXT

);
CREATE TABLE IF NOT EXISTS Usess (
     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
     Name,
     Uses TEXT 
);
''')

class Populate:
    def __init__(self):

        self.medicine=["Panadol","Nims","Brufen","Sylanar"]
        self.salt=["paracetamol","loloprene", "ibobrufen","ointmention"]
        self.company=["P&G", "lolo", "pop", "pp"]
        self.Quantity=[200,250,200,260]
        self.weight=[20,40,100,500]
        self.rateper=[0.8,2,12,9]
        self.uses=["Fever","painkiller","cough","itching, reding, acnes"]

        
        for i in range (4):
            name=self.medicine[i]
            salt=self.salt[i]
            company=self.company[i]
            quantity=self.Quantity[i]
            weight=self.weight[i]
            rateper=self.rateper[i]
            uses=self.uses[i]
            
            cur.execute('INSERT INTO Medicines (Name, Salt,Company,Quantity,Weight,Rateper,uses)VALUES(?,?,?,?,?,?,?)',(name,salt,company,quantity,weight,rateper,uses))
            cur.execute('INSERT INTO Usess (Name, Uses)Values(?,?)',(name,uses))
            conn.commit()

          


def main():
    a=Populate()
main() 
          








    
