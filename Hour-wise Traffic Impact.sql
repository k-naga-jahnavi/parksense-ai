SELECT

HOUR(
created_datetime
)

AS hour,

COUNT(*)

AS violations

FROM violations

GROUP BY hour

ORDER BY hour;