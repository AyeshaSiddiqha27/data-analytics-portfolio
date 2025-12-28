SELECT
    COUNT(*) AS total_movies,
    SUM(CASE WHEN release_date IS NULL THEN 1 ELSE 0 END) AS missing_release_date,
    SUM(CASE WHEN revenue IS NULL OR revenue = 0 THEN 1 ELSE 0 END) AS missing_or_zero_revenue,
    SUM(CASE WHEN rating IS NULL THEN 1 ELSE 0 END) AS missing_rating
FROM movie_genres;
