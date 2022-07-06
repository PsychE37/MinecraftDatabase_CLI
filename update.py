def set_gamemode(cur,con):
    try:
        p = input("Enter Player name: ")
        value = int(input("Enter the new game mode: "))
        query = "update Player set gamemode = %d where name = %s ;" %(value,p)
        cur.execute(query)
        con.commit()
        print("Updated Gamemode")
        input("Press any key to continue")
    except Exception as e:
        con.rollback()
        print("Failed to update database: ",e)
        input("Press any key to continue")
    return

def set_exp(cur,con):
    try:
        p = input("Enter Player name: ")
        points = int(input("Enter the exp points: "))
        level = int(input("Enter the exp level: "))
        query = "update Player set points = %d,level = %d where name = %s ;" %(points,level,p)
        cur.execute(query)
        con.commit()
        print("Updated exp")
        input("Press any key to continue")
    except Exception as e:
        con.rollback()
        print("Failed to update database: ",e)
        input("Press any key to continue")
    return