SELECT 
    date,
    repo_id,
    user AS user_id
FROM {{ ref("stg_gharchive") }}
WHERE event_type = 'Watch'