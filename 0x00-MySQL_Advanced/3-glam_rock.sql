-- Task Description: Write a SQL script to list all bands with Glam rock as their main style, ranked by their longevity

-- List bands with Glam rock as their main style, ranked by longevity
SELECT band_name,
       IF(split IS NULL, 0, (2022 - formed)) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC, band_name;

