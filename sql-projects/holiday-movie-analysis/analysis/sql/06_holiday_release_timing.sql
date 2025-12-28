WITH holiday_window AS (
    SELECT
        title,
        rating,
        revenue,
        release_date,
        CASE
            WHEN strftime('%m', release_date) = '12'
                 AND CAST(strftime('%d', release_date) AS INTEGER) BETWEEN 15 AND 24
            THEN 'Early Holiday'
            WHEN (
                strftime('%m', release_date) = '12'
                AND CAST(strftime('%d', release_date) AS INTEGER) >= 25
            )
            OR (
                strftime('%m', release_date) = '01'
                AND CAST(strftime('%d', release_date) AS INTEGER) <= 5
            )
            THEN 'Late Holiday'
            ELSE NULL
        END AS holiday_window
    FROM movies
    WHERE release_date IS NOT NULL
),

filtered AS (
    SELECT *
    FROM holiday_window
    WHERE holiday_window IS NOT NULL
)

SELECT
    holiday_window,
    COUNT(*) AS movie_count,
    ROUND(AVG(rating), 2) AS avg_rating,
    ROUND(AVG(revenue), 2) AS avg_revenue,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM filtered
GROUP BY holiday_window
ORDER BY total_revenue DESC;
