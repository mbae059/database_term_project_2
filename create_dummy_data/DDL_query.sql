CREATE TABLE Player (
    player_id SERIAL PRIMARY KEY,
    player_name VARCHAR(10),
    team_name VARCHAR(10),
    team_id INT,
    position VARCHAR(10),
    uniform_number INT,
    birth DATE,
    income INT,
    agent_id INT
);

CREATE TABLE Player_Record (
    record_id SERIAL PRIMARY KEY,
    player_id INT,
    start_date DATE,
    end_date DATE,
    team_id INT  
);
CREATE TABLE Agent (
    agent_id SERIAL PRIMARY KEY,
    agent_name VARCHAR(25),
    age INT,
    contact_info VARCHAR(20)
);
CREATE TABLE Owner (
    owner_id SERIAL PRIMARY KEY,
    team_id INT,
    owner_name VARCHAR(25),
    owner_age INT,
    budget INT
);
CREATE TABLE Team (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(25),
    owner_id INT,
    director_id INT,
    establishment_year INT
);
CREATE TABLE Director (
    director_id SERIAL PRIMARY KEY,
    director_name VARCHAR(25),
    director_year INT,
    team_id INT,
    income INT
);

CREATE TABLE Client (
    client_id SERIAL PRIMARY KEY,
    client_name VARCHAR(20),
    client_password VARCHAR(25),
    team_id INT,
    client_type VARCHAR(20)
);
CREATE TABLE Player_Agent (
    player_agent_id SERIAL PRIMARY KEY,
    player_id INT,
    agent_id INT,
    team_id INT,
    contract_date DATE,
    contract_term INT,
    contract_payment INT
);
CREATE TABLE Team_Award (
    team_award_id SERIAL PRIMARY KEY,
    awards_id INT,
    year INT,
    team_id INT
);
CREATE TABLE Individual_Award (
    individual_award_id SERIAL PRIMARY KEY,
    awards_id INT,
    year INT,
    player_id INT
);
CREATE TABLE Awards (
    awards_id SERIAL PRIMARY KEY,
    awards_name VARCHAR(255)
);
CREATE TABLE Baseball_Records (
    baseball_records_id SERIAL PRIMARY KEY,
    team1_id INT,
    team2_id INT,
    baseball_stadium_id INT,
    score VARCHAR(10)
);
CREATE TABLE Baseball_Stadium (
    baseball_stadium_id SERIAL PRIMARY KEY,
    location VARCHAR(255),
    area INT,
    capacity INT
);

