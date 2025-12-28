WITH holiday_movies AS (
    SELECT *
    FROM base_holiday_movies
)

SELECT
    holiday_period,
    COUNT(*) AS movie_count,
    ROUND(AVG(rating), 2) AS avg_rating,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM holiday_movies
GROUP BY holiday_period;
