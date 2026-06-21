SELECT

vehicle_type,

COUNT(*)

AS total

FROM violations

GROUP BY vehicle_type

ORDER BY total DESC;