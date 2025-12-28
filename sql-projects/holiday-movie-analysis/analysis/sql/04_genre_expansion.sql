WITH holiday_flag AS (
    SELECT
        id AS movie_id,
        title,
        rating,
        revenue,
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
)

SELECT
    h.holiday_period,
    g.genres,
    COUNT(*) AS movie_count,
    ROUND(AVG(h.rating), 2) AS avg_rating,
    ROUND(AVG(h.revenue), 2) AS avg_revenue
FROM holiday_flag h
JOIN movie_genres g
    ON h.movie_id = g.id
GROUP BY h.holiday_period, g.genres
HAVING COUNT(*) >= 10
ORDER BY
    h.holiday_period,
    avg_revenue DESC,
    avg_rating DESC;
