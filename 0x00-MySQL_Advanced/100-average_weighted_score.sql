-- Task Description: Write a SQL script to create a stored procedure ComputeAverageWeightedScoreForUser that computes and stores the average weighted score for a student.

-- Create stored procedure ComputeAverageWeightedScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;
    DECLARE total_weight INT;
    DECLARE weighted_sum FLOAT;

    -- Compute total weight for projects
    SELECT SUM(weight) INTO total_weight
    FROM projects;

    -- Compute weighted sum of scores
    SELECT SUM(score * weight) INTO weighted_sum
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Compute average weighted score
    IF total_weight > 0 THEN
        SET avg_score = weighted_sum / total_weight;
    ELSE
        SET avg_score = 0;
    END IF;

    -- Update average_score for the user
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END //
DELIMITER ;

