-- Database: recipees

-- DROP DATABASE IF EXISTS recipees;

CREATE DATABASE recipees
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

COMMENT ON DATABASE recipees
    IS 'Storing ingredients to check against what''s in the fridge to suggest recipees based off what I have. ';