SELECT

junction_name,

COUNT(*) violations,

CASE

WHEN COUNT(*)>10000

THEN "Critical"

WHEN COUNT(*)>5000

THEN "High"

WHEN COUNT(*)>1000

THEN "Medium"

ELSE "Low"

END

AS congestion_level

FROM violations

GROUP BY junction_name

ORDER BY violations DESC;