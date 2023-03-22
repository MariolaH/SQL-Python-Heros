from database.db_connection import execute_query

# execute_query('SELECT * FROM heroes')

def select_all_heroes():
    query = """ 
        SELECT name 
        from heroes 
        
        """
    select_all_heroes = execute_query(query).fetchall()
    for count, value in enumerate(select_all_heroes):
        print(f'{count +1}: {value[0]}') 

select_all_heroes()
