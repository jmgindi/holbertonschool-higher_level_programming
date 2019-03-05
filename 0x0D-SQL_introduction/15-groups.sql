-- lists the number of records with each score
SELECT score, COUNT(*) AS number FROM `second_table` GROUP BY score DESC;
