SELECT

latitude,

longitude,

COUNT(*)

AS count

FROM violations

WHERE

latitude IS NOT NULL

AND

longitude IS NOT NULL

GROUP BY

latitude,
longitude

ORDER BY count DESC

LIMIT 500;