from db import connect


# -------------------------
# Common SQL Executor
# -------------------------

def execute(query):

    conn = connect()

    cursor = conn.cursor(
        dictionary=True
    )

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()

    conn.close()

    return result


# -------------------------
# Dashboard Summary
# -------------------------

def summary():

    query = """

    SELECT

    COUNT(*) total_records,

    COUNT(
        DISTINCT police_station
    ) police_stations,

    COUNT(
        DISTINCT junction_name
    ) junctions,

    COUNT(
        DISTINCT vehicle_type
    ) vehicle_types

    FROM violations

    """

    return execute(
        query
    )


# -------------------------
# Hotspot Table
# -------------------------

def hotspots():

    query = """

    SELECT

    junction_name,

    AVG(
        latitude
    ) latitude,

    AVG(
        longitude
    ) longitude,

    COUNT(*) violations

    FROM violations

    WHERE

    junction_name IS NOT NULL

    GROUP BY
    junction_name

    ORDER BY
    violations DESC

    LIMIT 20

    """

    return execute(
        query
    )


# -------------------------
# Geo Heat Points
# -------------------------

def geo():

    query = """

    SELECT

    latitude,

    longitude,

    COUNT(*) count

    FROM violations

    WHERE

    latitude IS NOT NULL

    AND

    longitude IS NOT NULL

    GROUP BY

    latitude,
    longitude

    ORDER BY

    count DESC

    LIMIT 3000

    """

    return execute(
        query
    )


# -------------------------
# Hourly Congestion
# -------------------------

def hourly():

    query = """

    SELECT

    HOUR(
        created_datetime
    ) hour,

    COUNT(*) total

    FROM violations

    WHERE

    created_datetime
    IS NOT NULL

    GROUP BY
    hour

    ORDER BY
    hour

    """

    return execute(
        query
    )


# -------------------------
# Vehicle Analytics
# -------------------------

def vehicles():

    query = """

    SELECT

    vehicle_type,

    COUNT(*) total

    FROM violations

    WHERE

    vehicle_type IS NOT NULL

    GROUP BY
    vehicle_type

    ORDER BY
    total DESC

    LIMIT 15

    """

    return execute(
        query
    )


# -------------------------
# Violation Analytics
# -------------------------

def violations():

    query = """

    SELECT

    violation_type,

    COUNT(*) total

    FROM violations

    WHERE

    violation_type IS NOT NULL

    GROUP BY
    violation_type

    ORDER BY
    total DESC

    LIMIT 15

    """

    return execute(
        query
    )


# -------------------------
# Police Station Ranking
# -------------------------

def stations():

    query = """

    SELECT

    police_station,

    COUNT(*) total

    FROM violations

    WHERE

    police_station IS NOT NULL

    GROUP BY
    police_station

    ORDER BY
    total DESC

    LIMIT 15

    """

    return execute(
        query
    )


# -------------------------
# Validation Status
# -------------------------

def validation():

    query = """

    SELECT

    validation_status,

    COUNT(*) total

    FROM violations

    WHERE

    validation_status IS NOT NULL

    GROUP BY
    validation_status

    ORDER BY
    total DESC

    """

    return execute(
        query
    )


# -------------------------
# Average Response Time
# -------------------------

def response_time():

    query = """

    SELECT

    ROUND(

    AVG(

    TIMESTAMPDIFF(

    MINUTE,

    created_datetime,

    action_taken_timestamp

    )

    ),

    2

    )

    avg_minutes

    FROM violations

    WHERE

    created_datetime
    IS NOT NULL

    AND

    action_taken_timestamp
    IS NOT NULL

    """

    return execute(
        query
    )


# -------------------------
# Top Locations
# -------------------------

def locations():

    query = """

    SELECT

    location,

    COUNT(*) total

    FROM violations

    WHERE

    location IS NOT NULL

    GROUP BY
    location

    ORDER BY
    total DESC

    LIMIT 15

    """

    return execute(
        query
    )