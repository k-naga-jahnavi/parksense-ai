SELECT

junction_name,

COUNT(*) score,

ROUND(
AVG(latitude),
6
)

latitude,

ROUND(
AVG(longitude),
6
)

longitude,

"DIRECT ACTION"

AS recommendation

FROM violations

GROUP BY junction_name

ORDER BY score DESC

LIMIT 10;