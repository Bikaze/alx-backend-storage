-- This script creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Update users' average scores with the calculated weighted averages directly
    UPDATE users u
    JOIN (
        SELECT 
            c.user_id,
            SUM(c.score * p.weight) / SUM(p.weight) AS weighted_average
        FROM 
            corrections c
        JOIN 
            projects p ON c.project_id = p.id
        GROUP BY 
            c.user_id
    ) AS weighted_scores ON u.id = weighted_scores.user_id
    SET 
        u.average_score = weighted_scores.weighted_average;
END$$

DELIMITER ;
