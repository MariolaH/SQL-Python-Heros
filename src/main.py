from database.db_connection import execute_query

# execute_query('SELECT * FROM heroes')

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
        SELECT name 
        from heroes 
        
        """
    select_all_heroes = execute_query(query).fetchall()
    for count, value in enumerate(select_all_heroes):
        print(f'{count +1}: {value[0]}' '\v') 

# def heroes_info():
#     query = """ 
#         SELECT name, about_me, biography 
#         from heroes
          
        
#         """
#     select_all_heroes = execute_query(query).fetchall()
#     for count, value in enumerate(select_all_heroes):
#         print(f'{count +1}: {value[0]}' '\v') 


# select_all_heroes()

def begin():
    start = input("Hit ENTER to see a list of Heroes" '\v')
    if start == "":
        select_all_heroes()
begin()

def options():
    start = input("Select a Hero by ENTERING in their number to get more info about them: " '\v')
    if start == "1":
        print('Chill Women')
    elif start == "2":
        print('The Seer')
    elif start == "3":
        print('McMuscles')
    elif start == "4":
        print('The Hummingbird')
    elif start == "5":
        print('Mental Mary')
    else:
        print('Lieutenant Lidar')
options()    

# def Info():
#     start = input('\v'"Hit ENTER to see some more info about them")
    
# Info()

