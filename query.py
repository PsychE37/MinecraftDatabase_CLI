def select(cur,con):
    try:
        query = "Select points,level from Player"
        cur.execute(query)
        con.commit()
        input("Press any key to continue")
    except Exception as e:
        con.rollback()
        print("Failed: ",e)
        input("Press any key to continue")
    return

def project(cur,con):
    try:
        query = "Select name from Player where ((level*100) + points) < 2000"
        cur.execute(query)
        con.commit()
        input("Press any key to continue")
    except Exception as e:
        con.rollback()
        print("Failed: ",e)
        input("Press any key to continue")
    return

def aggregate(cur,con):
    try:
        query = "Select max(health) from Player"
        cur.execute(query)
        con.commit()
        input("Press any key to continue")
    except Exception as e:
        con.rollback()
        print("Failed: ",e)
        input("Press any key to continue")
    return

def search(cur,con):
    try:
        query = "Select name from Player where Instr(name,'pro')"
        cur.execute(query)
        con.commit()
        input("Press any key to continue")
    except Exception as e:
        con.rollback()
        print("Failed: ",e)
        input("Press any key to continue")
    return

def analysis(cur,con):
    try:
        query = "Select Block.id,D.player from Block Inner Join (Select Player,Block from Break) as D where D.Block = Block.id"
        cur.execute(query)
        con.commit()
        input("Press any key to continue")
    except Exception as e:
        con.rollback()
        print("Failed: ",e)
        input("Press any key to continue")
    return