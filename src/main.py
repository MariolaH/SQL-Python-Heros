from database.db_connection import execute_query

def logo():
    print("""

 ____  ____  ________  _______      ___   ________   ______   
|_   ||   _||_   __  ||_   __ \   .'   `.|_   __  |.' ____ \  
  | |__| |    | |_ \_|  | |__) | /  .-.  \ | |_ \_|| (___ \_| 
  |  __  |    |  _| _   |  __ /  | |   | | |  _| _  _.____`.  
 _| |  | |_  _| |__/ | _| |  \ \_\  `-'  /_| |__/ || \____) | 
|____||____||________||____| |___|`.___.'|________| \______.' 
                                                              
        HELLO! WELCOME TO THE SUPERHERO DATABASE
""")
logo()

# def select_all_heroes():
#     query = """ 
#         SELECT name 
#         from heroes 
        
#         """
#     select_all_heroes = execute_query(query).fetchall()
#     for count, value in enumerate(select_all_heroes):
#         print(f'{count +1}: {value[0]}' '\v') 

def select_all_heroes():
    query = """ 
        SELECT id, name 
        FROM heroes
        ORDER BY id ASC;
        
        """
    name = execute_query(query).fetchall()
    for count, x in name:
        print(f'ID {count}: {x}' '\v')              

# def heroes_info():
#     query = """ 
#         SELECT name, about_me, biography, name.ability_types
#         from heroes
#         join ability_types
#             on heroes.id = ability_types.id  
#         """
#     heroes_info = execute_query(query).fetchall()
#     for count, value in enumerate(heroes_info):
#         print(f'{count +1}: {value[0]}' '\v') 


# select_all_heroes()

def begin():
    start = input("Hit ENTER to see a list of Heroes" '\v')
    if start == "":
        select_all_heroes()
begin()


def options():
    start = input("Select a Hero by ENTERING in their number to get more info about them: " '\v')
    query = """ 
        SELECT
        name, 
        about_me,
        biography
        FROM heroes
        WHERE id = %s 
        """
    select_hero = execute_query(query, (start, )).fetchone()
    print(f'Name: {select_hero[0]} \n \v About: {select_hero[1]} \n \v Bio:{select_hero[2]}')
    game = input("HAD ENOUGH").capitalize()
    if game == "Yes":
        quit()
    elif game == "No":
        select_all_heroes()
        options()            
options()


# delete()
# def delete():
#     start = input("Select a hero to delete: " '\v')
#     query = """"
#         Delete FROM heros where id = %s 
#         """
#     select_hero = execute_query(query, (start, ))
#     print(f'Name: {start} has been removed') 
