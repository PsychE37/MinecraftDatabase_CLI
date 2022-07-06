def delete_player(cur,con):
    try:
        p = input("Enter Player Name: ")
        query = "delete from Player where name = %s ;" %(p)
        cur.execute(query)
        con.commit()
        print("Deleted Player")
        input("Press any key to continue")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database: ",e)
        input("Press any key to continue")
    return

def delete_block(cur,con):
    try:
        id = int(input("Enter block id: "))
        query = "delete from block where id = %s ;" %(id)
        cur.execute(query)
        con.commit()
        print("Deleted block")
        input("Press any key to continue")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database: ",e)
        input("Press any key to continue")
    return

def delete_NPC(cur,con):
    try:
        NPC_id = int(input("Enter NPC id: "))
        query = "delete from NPCs where id = %s ;" %(NPC_id)
        cur.execute(query)
        con.commit()
        print("Deleted NPC")
        input("Press any key to continue")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database: ",e)
        input("Press any key to continue")
    return