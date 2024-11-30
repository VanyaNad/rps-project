INSERT INTO scores (player_id, mode_id, score)
VALUES (%s, %s, %s)
ON CONFLICT (player_id, mode_id)
DO UPDATE SET score = EXCLUDED.score;
