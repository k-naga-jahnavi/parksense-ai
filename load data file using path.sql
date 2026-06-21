USE parksense_ai;

LOAD DATA LOCAL INFILE
'C:/Users/ASUS/OneDrive/Desktop/ParkSense_AI/dataset/violations.csv'

INTO TABLE violations

FIELDS TERMINATED BY ','

ENCLOSED BY '"'

LINES TERMINATED BY '\n'

IGNORE 1 ROWS

(
vehicle_number,
vehicle_type,
violation_type,
junction_name,
police_station,
latitude,
longitude,
created_datetime,
validation_status,
action_taken_timestamp
);