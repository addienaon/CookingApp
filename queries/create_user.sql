--create etl user
CREATE USER etl WITH PASSWORD 'g3Twenty!';
--grant connect
GRANT CONNECT ON DATABASE "recipees" TO etl;
--grant table permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO etl;
