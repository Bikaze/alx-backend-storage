-- This script creates a stored procedure ComputeAverageWeightedScoreForUser 
-- that computes and store the average weighted score for a student.

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weight FLOAT;
    DECLARE weighted_score_sum FLOAT;

    -- Calculate the sum of weighted scores for the user
    SELECT SUM(c.score * p.weight) INTO weighted_score_sum
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculate the total weight of all projects the user has participated in
    SELECT SUM(p.weight) INTO total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Update the user's average score with the calculated weighted average
    UPDATE users
    SET average_score = (weighted_score_sum / total_weight)
    WHERE id = user_id;
END$$

DELIMITER ;
