def attributes_keys(d):
    s = ''
    for key in d.keys():
        s = s + key + ', '
    
    if s[-2:] == ', ':
        return s[:-2]
    return s

def add_Player(cur,con):
    while(1):
        attributes = {}
        print('Enter the details of the Player:')
        attributes['name'] = input('Enter Player name: ')
        if len(attributes['name']) == 0:
            print('Error : No name entered')
            input('Press any key to continue.')
            return
        attributes['enderitems'] = int(input('Enter no.of enderitems: '))
        if attributes['enderitems'] < 0:
            print('Please enter an integer >= 0')
            input('Press any key to continue.')
            return
        attributes['gamemode'] = int(input('Enter gamemode: '))
        if attributes['gamemode'] < 0:
            print('Please enter an integer >= 0')
            input('Press any key to continue.')
            return
        attributes['advancement'] = input('Enter advancements: ')
        if len(attributes['name']) == 0:
            print('Error : No advancements entered')
            input('Press any key to continue.')
            return
        attributes['effects'] = int(input('Enter no.of effects: '))
        if attributes['effects'] < 0:
            print('Please enter an integer >= 0')
            input('Press any key to continue.')
            return
        attributes['points'] = int(input('Enter points: '))
        if attributes['points'] < 0:
            print('Please enter an integer >= 0')
            input('Press any key to continue.')
            return
        attributes['level'] = int(input('Enter level: '))
        if attributes['level'] < 0:
            print('Please enter an integer >= 0')
            input('Press any key to continue.')
            return
        attributes['health'] = int(input('Enter health: '))
        if attributes['health'] < 0:
            print('Please enter an integer >= 0')
            input('Press any key to continue.')
            return
        attributes['helmet'] = int(input('Enter helmet lvl: '))
        if attributes['helmet'] < 0:
            print('Please enter an integer >= 0')
            input('Press any key to continue.')
            return
        attributes['chestplate'] = int(input('Enter chestplate lvl: '))
        if attributes['chestplate'] < 0:
            print('Please enter an integer >= 0')
            input('Press any key to continue.')
            return
        attributes['leggings'] = int(input('Enter leggings lvl: '))
        if attributes['leggings'] < 0:
            print('Please enter an integer >= 0')
            input('Press any key to continue.')
            return
        attributes['boots'] = int(input('Enter boots lvl: '))
        if attributes['boots'] < 0:
            print('Please enter an integer >= 0')
            input('Press any key to continue.')
            return
        attributes['inventory'] = int(input('Enter inventory size: '))
        if attributes['inventory'] < 0:
            print('Please enter an integer >= 0')
            input('Press any key to continue.')
            return
        attributes['hunger'] = int(input('Enter hunger: '))
        if attributes['hunger'] < 0:
            print('Please enter an integer >= 0')
            input('Press any key to continue.')
            return
        query = f'INSERT INTO Minecraft.Player({attributes_keys(attributes)}) VALUES({attributes["name"]},"{attributes["enderitems"]}","{attributes["gamemode"]}","{attributes["advancement"]}","{attributes["effects"]}","{attributes["points"]}","{attributes["level"]}","{attributes["health"]}","{attributes["helmet"]}","{attributes["chestplate"]}","{attributes["leggings"]}","{attributes["boots"]}","{attributes["inventory"]}","{attributes["hunger"]}");'
        try:
            cur.execute(query)
            con.commit()
            print('New Player adsded to the database')
            input('Press any key to continue')
        except Exception as exception:
            print('Failed to insert Player into the database.')
            con.rollback()
            print(exception)
            input('Press any key to continue.')
            return 
        break

def add_Block(cur,con):
    while(1):
        attributes = {}
        print('Enter the details of the Block:')
        attributes['name'] = input('Enter Block name: ')
        if len(attributes['name']) == 0:
            print('Error : No name entered')
            input('Press any key to continue.')
            return
        attributes['id'] = input('Enter Block id: ')
        if len(attributes['id']) == 0:
            print('Error : No id entered')
            input('Press any key to continue.')
            return
        query = f'INSERT INTO Minecraft.Player({attributes_keys(attributes)}) VALUES({attributes["name"]},"{attributes["id"]}"); '
        try:
            cur.execute(query)
            con.commit()
            print('New Player adsded to the database')
            input('Press any key to continue')
        except Exception as exception:
            print('Failed to insert Player into the database.')
            con.rollback()
            print(exception)
            input('Press any key to continue.')
            return 
        break