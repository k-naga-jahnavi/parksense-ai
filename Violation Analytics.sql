SELECT

violation_type,

COUNT(*)

AS total

FROM violations

GROUP BY violation_type

ORDER BY total DESC;