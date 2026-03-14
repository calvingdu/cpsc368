CREATE TABLE anes_2020 (
    id_2020 NUMBER(10) PRIMARY KEY,
    lib_con_scale VARCHAR2(30),
    democrat_thermometer NUMBER(5,1),
    republican_thermometer NUMBER(5,1),
    youtube_use VARCHAR2(3),
    election_year NUMBER(4) NOT NULL
)

CREATE TABLE anes_2024 (
    id_2024 NUMBER(10) PRIMARY KEY,
    id_2020 NUMBER(10),
    lib_con_scale VARCHAR2(30),
    democrat_thermometer NUMBER(5,1),
    republican_thermometer NUMBER(5,1),
    youtube_use VARCHAR2(3),
    election_year NUMBER(4) NOT NULL
)