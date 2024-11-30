SELECT p.name, m.mode_name, s.score, s.created_at
FROM scores s
JOIN players p ON s.player_id = p.id
JOIN modes m ON s.mode_id = m.id
ORDER BY s.score DESC;