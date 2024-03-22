-- Task Description: Write a SQL script to create a stored procedure ComputeAverageWeightedScoreForUsers that computes and stores the average weighted score for all students.

-- Create stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id_var INT;
    DECLARE avg_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE weighted_sum FLOAT;

    -- Cursor declaration
    DECLARE user_cursor CURSOR FOR
        SELECT id FROM users;

    -- Declare NOT FOUND handler
    DECLARE CONTINUE HANDLER FOR NOT FOUND
        SET user_id_var = NULL;

    -- Open cursor
    OPEN user_cursor;

    -- Loop through each user
    user_loop: LOOP
        -- Fetch user_id from cursor
        FETCH user_cursor INTO user_id_var;

        -- Exit loop if no more users
        IF user_id_var IS NULL THEN
            LEAVE user_loop;
        END IF;

        -- Compute total weight for projects
        SELECT SUM(weight) INTO total_weight
        FROM projects;

        -- Compute weighted sum of scores
        SELECT SUM(score * weight) INTO weighted_sum
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id_var;

        -- Compute average weighted score
        IF total_weight > 0 THEN
            SET avg_score = weighted_sum / total_weight;
        ELSE
            SET avg_score = 0;
        END IF;

        -- Update average_score for the user
        UPDATE users
        SET average_score = avg_score
        WHERE id = user_id_var;
    END LOOP;

    -- Close cursor
    CLOSE user_cursor;
END //
DELIMITER ;

