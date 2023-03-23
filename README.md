```

OBJECTIVE

Create an interactive shell script with the help of python that helps superheroes stay in touch with their friends and keep track of supervillains through the terminal.

```

```
CRUD

C: CREATE: creating an entry
    SQL: INSERT

R: READ: getting access to the inputs or entries
    SQL: SELECT

U: UPDATE: operation that allows you to modify existing data
    SQL: UPDATE

D: DELETE: get rid of an entry 
    SQL: DELETE

```

```
INSERT

INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)

```

```

SELECT


SELECT column, another_table_column, …
FROM mytable
INNER JOIN another_table 
    ON mytable.id = another_table.id

EX. abilities type

SELECT name
FROM heroes
INNER JOIN abilities_types
    ON hereos.id = abilities_types.id

SELECT
name,
about_me,
biography
FROM heroes
JOIN
    ON

```    

```

UPDATE

EX. ability_ type
FROM Mind control to mind reader

UPDATE table_name
SET column1 = value1,
WHERE condition;

```

```

DELETE

EX. Hero - Mrs. Muscles

DELETE FROM table_name
WHERE condition;

```
```
FUNCTIONS:

START TERMINAL
    PROMPT - HELLO WELCOME TO THE SUPER HERO DATABASE
    
    LIST OF HEROS IS DISPLAYED

    PLEASE SELECT A SUPERHERO

    INPUT - NUMBER OF SUPERHERO

    DISPLAY - SUPER HEROES NAME, ABOUT_ME AND BIO

    PROMPT 1
        - CONTINUE WITH GETTING INFO ON HEROES
        - NEXT TASK?

    IF - CONTINUE WITH GETTING INFO ON HEROES
            AFTER INFO IS DISPLAYED, GO BACK TO PROMPT 1

    ELSE - NEXT TASK?
        1. ADD A NEW HERO
        2. DELETE A HERO
        3 UPDATE NAME OF A HERO
        4. RETURN TO STARTING POINT

        1-3 WILL LOOP BACK TO THE MAIN MENU DISPLAYING ELSE OPTIONS
