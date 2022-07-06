The commands we can run are:
        1 - add_Player
        2 - add_Block
        3 - delete_player
        4 - delete_block
        5 - delete_NPC
        6 - set_exp
        7 - set_gamemode

Run the main.py file with `python3 main.py` and follow the user friendly interface. We can also
1) Get the experience data of all players
2) Get all player names with exp less than 2000
3) Find the max health among all players
4) Search for player with name containing the string 'pro'
5) Get a list of players and block ids of blocks broken by them

Their functions are suggestive from their names. They were all executed using sql queries with the help of execute command in pymysql.

You need to have locally running sql database.  Configure the sql connection in main.py accordingly.