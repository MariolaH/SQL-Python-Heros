from database.db_connection import execute_query
import os

# 1
os.system('clear')
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

# 3
def select_all_heroes():
    query = """ 
        SELECT id, name 
        FROM heroes
        ORDER BY id ASC;
        
        """
    name = execute_query(query).fetchall()
    for count, x in name:
        print(f'ID {count}: {x}' '\v')              

# 5
def options_menu():
    os.system('clear')
    value = input('\vWhat would you like to do next?\n\v 1. Add a new hero?\n\v 2. Delete a Hero?\n\v 3. Change the name of a hero?\n\v 4. Hero Info?\n\v Select a number?\n\v')
    if value == '1':
        add()
        options_menu()
    elif value == '2':
        os.system('clear')
        delete()
    elif value == '3':
        os.system('clear')
        update()
        options_menu()
    elif value == '4':
        os.system('clear')
        begin()
        options()
# 2
def begin():
    start = input("Hit ENTER to see a list of Heroes" '\v')
    if start == "":
        select_all_heroes()
begin()


def add():
    name = input("Please name your Hero\v ")
    about_me = input("Add an about me\v ")
    biography = input("Add a bio\v ")
    params = (name, about_me, biography)
    query = """ 
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        """
    execute_query(query, params)
    # print(f'Congrats you created a new Hero named {name} ''\v')
    # main_menu = input('Press ENTER to return to main menu')
    # if main_menu == "":
    #     pass
    next = input('Do you want to create another Hero? Yes or No  ').capitalize()
    if next == 'Yes':
        add()
    elif next == 'No':
        options_menu()


def update():
    select_all_heroes()
    name = input("ENTER the Heroes number "'\v')
    change_name = input("What would you like to change the name to? "'\v')
    params = (change_name, name)
    query = """ 
        UPDATE heroes
        SET name = %s
        WHERE id = %s
        """
    execute_query(query, params)
    print(f'Heroes name has been changed to {change_name} ''\v')
    # main_menu = input('Press ENTER to return to main menu')
    # if main_menu == "":
    #     pass
    next = input('Do you want to update another Heros name ? Yes or No  ').capitalize()
    if next == 'Yes':
        os.system('clear')
        update()
    elif next == 'No':
        options_menu()


def delete():
    select_all_heroes()
    start = input("Select the number of the Hero you would like to delete: " '\v')
    query = """
        Delete FROM heroes where id = %s
        """
    delete_query = execute_query(query, (start, ))

    print(f""" {start} has been removed 

 _                                                
| |__   _   _   ___   ___   ___   ___   
| '_ \ | | | | / _ \ / _ \ / _ \ / _ \ 
| |_) || |_| ||  __/|  __/|  __/|  __/
|_.__/  \__, | \___| \___| \___| \___| 
        |___/                                     




""")

    next = input('Do you want to delete another Hero? Yes or No  ').capitalize()
    if next == 'Yes':
        delete()
    elif next == 'No':
        options_menu()

# 4
def options():
    os.system('clear')
    select_all_heroes()
    start = input("ENTER the number of the Hero you want to know more about " '\v')
    query = """ 
        SELECT
        name, 
        about_me,
        biography
        FROM heroes
        WHERE id = %s 
        """
    select_hero = execute_query(query, (start, )).fetchone()
    print(f'Name: {select_hero[0]}\v\nAbout: {select_hero[1]}\n\vBio:{select_hero[2]}\v')
    game = input("Had enough of these Heroes... TYPE: YES for the next task \n\vTYPE: NO to see more Heroes and their info... ").capitalize()
    if game == "Yes":
        os.system('clear') 
        options_menu()   
    else:
        game == "No"
        select_all_heroes()
        begin()
options()



# SELECT *
# FROM Table1 
# INNER JOIN Table2
#     ON Condition
# INNER JOIN Table3
#     ON Condition;

# def abilities():
#     add abilites to heroes when their name is selected

# %s operator lets you add a value into a Python string