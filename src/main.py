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

def add():
    name = input("Please name your Hero ")
    about_me = input("Add an about me ")
    biography = input("Add a bio ")
    params = (name, about_me, biography)
    query = """ 
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        """
    execute_query(query, params)

def options():
    start = input("ENTER in a number to get more info about a Hero " '\v')
    query = """ 
        SELECT
        name, 
        about_me,
        biography
        FROM heroes
        WHERE id = %s 
        """
    select_hero = execute_query(query, (start, )).fetchone()
    print(f'Name: {select_hero[0]} \n \v About: {select_hero[1]} \n \v Bio:{select_hero[2]} \v')
    game = input("Had enough of these Heroes... ENTER...YES for the next task \n\v ENTER NO to see more Heroes and their info... ").capitalize()
    if game == "Yes":
        value = input('\vWhat would you like to do next?\n\v 1. Add a new hero?\n\v 2. Delete a Hero?\n\v 3. Change the name of a hero?\n\v Select a number?\n\v')
        if value == '1':
            add()
            # quit()
    elif game == "No":
        select_all_heroes()
        options()            
options()




# def update()
#     update a characters name

# def abilities():
#     add abilites to heroes when their name is selected


# def delete():
#     start = input("Select a hero to delete: " '\v')
#     query = """"
#         Delete FROM heros where id = %s 
#         """
#     select_hero = execute_query(query, (start, ))
#     print(f'Name: {start} has been removed') 
# delete()