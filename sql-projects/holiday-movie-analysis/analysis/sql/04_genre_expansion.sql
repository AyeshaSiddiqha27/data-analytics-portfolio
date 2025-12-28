WITH holiday_movies AS (
    SELECT *
    FROM base_holiday_movies
)

SELECT
    h.holiday_period,
    g.genres,
    COUNT(*) AS movie_count,
    ROUND(AVG(h.rating), 2) AS avg_rating,
    ROUND(AVG(h.revenue), 2) AS avg_revenue
FROM holiday_movies h
JOIN movie_genres g
    ON h.id = g.id
GROUP BY h.holiday_period, g.genres
HAVING COUNT(*) >= 10
ORDER BY h.holiday_period, avg_revenue DESC;
