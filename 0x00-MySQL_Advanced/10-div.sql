-- This script creates a function SafeDiv that divides (and returns)
-- the first by the second number or returns 0 if the second number is equal to 0.
-- The function is created in the database holberton and the name of the function is SafeDiv.
-- The function takes two arguments: a and b (both are float).
-- The function returns a float.
-- The function is created with the following SQL statement:

DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END$$
DELIMITER ;
