WITH genre_performance AS (
    SELECT
        CASE
            WHEN (
                strftime('%m', h.release_date) = '12'
                AND CAST(strftime('%d', h.release_date) AS INTEGER) >= 15
            )
            OR (
                strftime('%m', h.release_date) = '01'
                AND CAST(strftime('%d', h.release_date) AS INTEGER) <= 5
            )
            THEN 'Holiday'
            ELSE 'Non-Holiday'
        END AS holiday_period,
        g.genres,
        COUNT(*) AS movie_count,
        ROUND(AVG(h.revenue), 2) AS avg_revenue,
        ROUND(AVG(h.rating), 2) AS avg_rating
    FROM movies h
    JOIN movie_genres g
        ON h.id = g.id
    GROUP BY holiday_period, g.genres
    HAVING COUNT(*) >= 10
)

SELECT
    holiday_period,
    genres,
    movie_count,
    avg_rating,
    avg_revenue AS revenue_per_movie
FROM genre_performance
ORDER BY
    holiday_period,
    revenue_per_movie DESC;
