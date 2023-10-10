-- upload script: titanic_to_sql.py

-- #1 Count how many rows you have.

SELECT count(name) FROM titanic;
-- 887


-- #2 How many people survived?

SELECT SUM(survived) FROM titanic;
-- 342


-- #3 What passenger class has the largest population?
SELECT pclass, COUNT(pclass) FROM titanic
GROUP BY pclass
ORDER BY count
DESC
LIMIT 1;
-- 3rd Class