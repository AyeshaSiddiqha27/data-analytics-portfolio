WITH classified AS (
    SELECT
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
        END AS holiday_period,
        rating,
        revenue
    FROM movie_genres
    WHERE release_date IS NOT NULL
)

SELECT
    holiday_period,
    COUNT(*) AS movie_count,
    ROUND(AVG(rating), 2) AS avg_rating,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM classified
GROUP BY holiday_period;
