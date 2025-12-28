WITH holiday_movies AS (
    SELECT *
    FROM base_holiday_movies
)

SELECT
    h.holiday_period,
    g.genres,
    COUNT(*) AS movie_count,
    ROUND(AVG(h.revenue), 2) AS revenue_per_movie,
    ROUND(AVG(h.rating), 2) AS avg_rating
FROM holiday_movies h
JOIN movie_genres g
    ON h.id = g.id
GROUP BY h.holiday_period, g.genres
HAVING COUNT(*) >= 10
ORDER BY h.holiday_period, revenue_per_movie DESC;
