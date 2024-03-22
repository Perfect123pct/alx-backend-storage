-- Task Description: Write a SQL script to rank the country origins of bands based on the number of fans

-- Rank country origins of bands based on number of fans
SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

