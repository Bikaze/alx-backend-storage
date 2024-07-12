-- This script creates a stored procedure ComputeAverageScoreForUser that computes
-- and store the average score for a student.

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN pid INT)
BEGIN
    DECLARE avg_score FLOAT;

    -- compute the average score
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = pid;

    -- update the user's average score
    UPDATE users
    SET average_score = avg_score
    WHERE id = pid;
END$$
DELIMITER ;
