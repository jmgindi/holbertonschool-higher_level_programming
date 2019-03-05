-- lists rows with name values score first, descending order by score
SELECT score, name FROM `second_table` WHERE name IS NOT NULL ORDER BY score DESC;
