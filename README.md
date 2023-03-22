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


INSERT INTO
    heroes (name, about_me, biography)
VALUES
    (
        'Mrs Muscle',
        'Strongest women you have ever met.',
        'Mrs Muscle loves to work out 6 - 8 hours a day. For every meal she eats 50 grams of protein and 100 grams of carbs. .'
    );


INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (7, 8);


INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (7, 1);


INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (7, 5);


INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (3, 7, 2);


INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (7, 1, 1);        


INSERT INTO
    ability_types (name)
VALUES
    ('Mind Control');

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

    DISPLAY - SUPER HEROES NAME

    PROMPT - WHAT DO YOU WANT TO KNOW ABOUT THEM?

    LIST - about_me, biography, abilities, relationships

    DISPLAY - select: about_me, biography, abilities, relationships

    INPUT - NUMBER/NAME?

    DISPLAY - INFO

    INPUT - HEROS - RETURN TO MAIN SCREEN
