-- list all records of scores and names second_table

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
