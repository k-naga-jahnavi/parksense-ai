SELECT

junction_name,

COUNT(*)

AS violations,

ROUND(
AVG(latitude),
6
)

latitude,

ROUND(
AVG(longitude),
6
)

longitude

FROM violations

GROUP BY junction_name

ORDER BY violations DESC

LIMIT 20;