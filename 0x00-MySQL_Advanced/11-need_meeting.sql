-- Creates a view need_meeting that meets these requirements:
   -- view need_meeting should return all students name when:
   -- There scores are under (strict) 80
   
CREATE VIEW need_meeting AS SELECT name from students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH));
