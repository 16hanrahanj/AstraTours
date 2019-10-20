import sqlite3
chosen = False #starts while loop
while chosen == False:
    hotelChoice = input("What hotel would you like to visit\n")
    if hotelChoice == ("hotel eris"):
        con = sqlite3.connect('Main Data Base.db')
        c=con.cursor()
        c.execute("SELECT `Hotel Name` FROM Hotels WHERE `Hotel Name` = 'hotel eris'" )#fetches info from data base
        print("this hotel has been rated 4")
        chosen = True #exits loop
    elif hotelChoice == ("hotel dysnomia"):
        con = sqlite3.connect('Main Data Base.db')
        c=con.cursor()
        c.execute("SELECT Hotel Name FROM Hotels WHERE `Hotel Name` = 'hotel dysnomia'")#fetches info from data base
        print("this hotel has been rated 4.5")
        chosen = True #exits loop
    else:
        chosen = False #restarts loop
    
    



