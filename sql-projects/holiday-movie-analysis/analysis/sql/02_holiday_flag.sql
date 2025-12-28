SELECT
    title,
    release_date,
    rating,
    revenue,
    genres,
    CASE
        WHEN (
            strftime('%m', release_date) = '12'
            AND CAST(strftime('%d', release_date) AS INTEGER) >= 15
        )
        OR (
            strftime('%m', release_date) = '01'
            AND CAST(strftime('%d', release_date) AS INTEGER) <= 5
        )
        THEN 'Holiday'
        ELSE 'Non-Holiday'
    END AS holiday_period
FROM movies
WHERE release_date IS NOT NULL;
