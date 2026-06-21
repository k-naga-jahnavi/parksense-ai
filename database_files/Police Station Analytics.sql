SELECT

police_station,

COUNT(*)

AS total

FROM violations

GROUP BY police_station

ORDER BY total DESC

LIMIT 20;