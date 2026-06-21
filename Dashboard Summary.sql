SELECT

COUNT(*) total_records,

COUNT(
DISTINCT police_station
)

AS police_stations,

COUNT(
DISTINCT junction_name
)

AS junctions,

COUNT(
DISTINCT vehicle_type
)

AS vehicle_types

FROM violations;