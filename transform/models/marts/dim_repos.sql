SELECT
	repo_id,
	repo_name,
	min(event_date) AS start_date,
	lead(start_date) OVER (PARTITION BY repo_id ORDER BY start_date ASC) AS end_date
FROM {{ ref("stg_gharchive") }}
GROUP BY 1, 2