CREATE TABLE violations(

id INT AUTO_INCREMENT PRIMARY KEY,

vehicle_number VARCHAR(50),

vehicle_type VARCHAR(50),

violation_type VARCHAR(150),

junction_name VARCHAR(255),

police_station VARCHAR(255),

latitude DECIMAL(10,6),

longitude DECIMAL(10,6),

created_datetime DATETIME,

validation_status VARCHAR(100),

action_taken_timestamp DATETIME

);