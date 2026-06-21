import pandas as pd
import numpy as np
from db import connect


print("Loading CSV...")

df = pd.read_csv(
    "../dataset/violations.csv",
    low_memory=False,
    dtype=str
)


# -----------------
# CLEAN COLUMNS
# -----------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
)


# -----------------
# KEEP ONLY NEEDED
# -----------------

cols = [

"vehicle_number",
"vehicle_type",
"violation_type",
"junction_name",
"police_station",
"latitude",
"longitude",
"created_datetime",
"validation_status",
"action_taken_timestamp"

]

for c in cols:

    if c not in df.columns:

        df[c] = None


df = df[cols]


# -----------------
# REMOVE nan VALUES
# -----------------

df = df.replace(
    [
        np.nan,
        "nan",
        "NaN",
        "NULL",
        "null",
        "",
        " "
    ],
    None
)


# -----------------
# DATETIME
# -----------------

for c in [

"created_datetime",
"action_taken_timestamp"

]:

    df[c] = pd.to_datetime(

        df[c],

        errors="coerce"

    )

    df[c] = (

        df[c]

        .dt.strftime(

            "%Y-%m-%d %H:%M:%S"

        )

    )

    df[c] = df[c].where(

        pd.notnull(df[c]),

        None

    )


# -----------------
# NUMERIC
# -----------------

for c in [

"latitude",
"longitude"

]:

    df[c] = pd.to_numeric(

        df[c],

        errors="coerce"

    )

    df[c] = df[c].where(

        pd.notnull(df[c]),

        None

    )


print("Connecting MySQL...")


conn = connect()

cursor = conn.cursor()


query = """

INSERT INTO violations(

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

)

VALUES(

%s,%s,%s,%s,%s,
%s,%s,%s,%s,%s

)

"""


success = 0
failed = 0


for row in df.itertuples(index=False):

    try:

        values = tuple(
            None
            if (
                str(v).lower() == "nan"
                or str(v).lower() == "nat"
            )
            else v
            for v in row
        )

        cursor.execute(
            query,
            values
        )

        success += 1

        if success % 1000 == 0:

            conn.commit()

            print(
                success,
                "imported"
            )

    except Exception as e:

        failed += 1

        print(
            "FAILED ROW:",
            values
        )

        print(
            e
        )


conn.commit()

cursor.close()

conn.close()


print("\nDONE")

print(
    "Imported:",
    success
)

print(
    "Failed:",
    failed
)