SELECT *
FROM Table1 
INNER JOIN Table2
    ON Condition
INNER JOIN Table3
    ON Condition;

SELECT name
FROM heroes
INNER JOIN abilities_types
    ON hereos.id = abilities_types.id
INNER JOIN     