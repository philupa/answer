    -- 1. Find the overall number of points the member with id 321 has scored in all games played.
SELECT SUM(points)
FROM member_game_instance
WHERE member_id = 321;
    
    -- 2. How many games have been played during weekends?  
SELECT COUNT(game_id)
FROM game_instance
WHERE DATEPART(dw, start_datetime)>5

    -- 3. How many games of conquest have been played during weekends?
SELECT COUNT(game_id)
FROM game_instance
WHERE DATEPART(dw, start_datetime)>5 AND game_id = 5

    -- 4. Find the number of times the member with id 321 has played any game and output the number of times, the alias and the first name of the member.  
SELECT COUNT(game_instance_id), alias, first_name
FROM member_game_instance
JOIN member ON member.id = member_game_instance.member_id
WHERE member_id = 321
GROUP BY alias, first_name;

    -- 5. Find the member with the most points scored overall and output the member_id, alias  and number of points as score.  
SELECT TOP 1 SUM(points) AS total_points, alias, first_name
FROM member_game_instance
JOIN member ON member.id = member_game_instance.member_id
GROUP BY alias, first_name
ORDER BY total_points DESC;

    -- 6. Find the members' aliases, first_names and dates of birth that have played  ‘Conquest’, for the 5 youngest players (most recent date of birth).  
SELECT TOP 5 alias, first_name, date_of_birth
FROM member_game_instance
JOIN member ON member.id = member_game_instance.member_id
JOIN game_instance on game_instance.id = member_game_instance.game_instance_id
WHERE game_instance.game_id = 5
ORDER BY date_of_birth DESC;

    -- 7. Find the first 20 players with the highest accuracy in the game ‘Capture the Flag’. 
SELECT TOP 20 accuracy, alias, first_name
FROM member_game_instance
JOIN member ON member.id = member_game_instance.member_id
JOIN game_instance on game_instance.id = member_game_instance.game_instance_id
WHERE game_instance.game_id = 2
ORDER BY accuracy DESC;

    -- 8. How many games have been played on each day of the week?
SELECT COUNT(game_id), DATENAME(dw, start_datetime)
FROM game_instance
GROUP BY DATENAME(dw, start_datetime), DATEPART(dw, start_datetime)
ORDER BY DATEPART(dw, start_datetime);

    -- 9.  Find the average accuracy of all players in the game ‘King of the Hill’.
SELECT AVG(accuracy), game_id
FROM member_game_instance
JOIN game_instance on game_instance.id = member_game_instance.game_instance_id
WHERE game_instance.game_id = 1
GROUP BY game_id;

    -- 10. Order all games by popularity (number of times played) and output the game id,  name and number of times played. 
SELECT game_id, game_name, COUNT(game_instance.id) AS number_of_times_played
FROM member_game_instance
JOIN game_instance on game_instance.id = member_game_instance.game_instance_id
JOIN game on game.id = game_instance.game_id
GROUP BY game_id, game_name
ORDER BY number_of_times_played DESC;