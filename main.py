import pymysql as sql

from insert import *
from update import *
from delete import *
from query import *

def Insert():
    while(1):
        print("1 - Insert a new player")
        print("2 - Insert a new block")
        print("3 - Back")
        inp = int(input("Enter choice:"))
        if (inp == 1):
            add_Player(cur,con)
        elif (inp == 2):
            add_Block(cur,con)
        elif (inp == 3):
            break
        else:
            print("Please enter the number corresponding to your request")                

def Delete():
    while(1):
        print("1 - Delete a player")
        print("2 - Delete a block")
        print("3 - Delete an NPC")    
        print("4 - Back")
        inp = int(input("Enter choice:"))
        if (inp == 1):
            delete_player(cur,con)
        elif (inp == 2):
            delete_block(cur,con)
        elif (inp == 3):
            delete_NPC(cur,con)
        elif (inp == 4):
            break
        else:
            print("Please enter the number corresponding to your request")

def Update():
    while(1):
        print("1 - Update a players exp")
        print("2 - Update a players gamemode")
        print("3 - Back")
        inp = int(input("Enter choice:"))
        if (inp == 1):
            set_exp(cur,con)
        elif (inp == 2):
            set_gamemode(cur,con)
        elif (inp == 3):
            break
        else:
            print("Please enter the number corresponding to your request")

def Query():
    while(1):
        print("1 - Get the experience data of all players")
        print("2 - Get all player names with exp less than 2000")
        print("3 - Find the max health among all players")
        print("4 - Search for player with name containing the string 'pro'")
        print("5 - Get a list of players and block ids of blocks broken by them")
        print("6 - Back")
        inp = int(input("Enter choice:"))
        if (inp == 1):
            select(cur,con)
        elif (inp == 2):
            project(cur,con)
        elif (inp == 3):
            aggregate(cur,con)
        elif (inp == 4):
            search(cur,con)
        elif (inp == 5):
            analysis(cur,con)
        elif (inp == 6):
            break
        else:
            print("Please enter the number corresponding to your request")


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("                       Minecraft Database                           ")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
while (1):
    # try:
        con = sql.connect(
            host='localhost',
            user='root',
            password="password",
            db='Minecraft',
        )
        cur = con.cursor()
        while(1):
                print("1 - Insert")
                print("2 - Delete")
                print("3 - Update")
                print("4 - Other queries")
                print("5 - Back")                
                print("6 - Quit")
                inp = int(input("Enter choice:"))
                if (inp == 1):
                    Insert()
                elif (inp == 2):
                    Delete()
                elif (inp == 3):
                    Update()
                elif (inp == 4):
                    Query()
                elif (inp == 5):
                    break
                elif (inp == 6):
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print("                 Thank you, please compile again                    ")
                    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                    raise SystemExit
                else:
                    print("Please enter the number corresponding to your request")                
            
    # except:
        print("Connection Refused: Please check the pymysql.connect parameters and try again")
        inp = input("Press any key to exit")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("                 Thank you, please compile again                    ")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        break