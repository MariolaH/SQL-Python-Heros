from database.db_connection import execute_query
import os

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


def select_all_heroes():
    query = """ 
        SELECT id, name 
        FROM heroes
        ORDER BY id ASC;
        
        """
    name = execute_query(query).fetchall()
    for count, x in name:
        print(f'ID {count}: {x}' '\v')              

def options_menu():
    os.system('clear')
    value = input('\vWhat would you like to do next?\n\v 1. Add a new hero?\n\v 2. Delete a Hero?\n\v 3. Change the name of a hero?\n\v Select a number?\n\v')
    if value == '1':
        add()
        options_menu()
    elif value == '2':
        os.system('clear')
        delete()
    elif value == '3':
        os.system('clear')
        options_menu()

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

def delete():
    select_all_heroes()
    start = input("Select the number of the Hero you would like to delete: " '\v')
    query = """
        Delete FROM heroes where id = %s
        """
    delete_query = execute_query(query, (start, ))
    print(f'Name: {start} has been removed')
    next = input('Do you want to delete another Hero? Yes or No  ').capitalize()
    if next == 'Yes':
        delete()
    elif next == 'No':
        begin()
        options()


def options():
    os.system('clear')
    select_all_heroes()
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
        os.system('clear') 
        options_menu()   
    else:
        game == "No"
        select_all_heroes()
        begin()
options()





# def update()
#     update a characters name

# def abilities():
#     add abilites to heroes when their name is selected

