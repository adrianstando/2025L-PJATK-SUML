CREATE DATABASE user_db;
GRANT ALL PRIVILEGES ON DATABASE user_db TO "admin";

\connect user_db;

CREATE TABLE people (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100),
	surname VARCHAR(100),
	position VARCHAR(50),
    salary DECIMAL(10, 2)
);

INSERT INTO people (name, surname, position, salary) VALUES
('Jan', 'Kowalski', 'Manager', 15000.00),
('Krzysztof', 'Nowak', 'Developer', 10000.00);

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO "admin";
