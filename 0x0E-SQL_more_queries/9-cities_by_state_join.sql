-- listing cities with thier state
SELECT `cities`.`id`, `cities`.`name`, `states`.`name`
FROM `cities`
JOIN INNER `states` ON `cities`.`state_id` = `states`.`id`
ORDER BY `cities`.`id`;
