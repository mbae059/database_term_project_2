CREATE TABLE Player (
    player_id INT PRIMARY KEY,
    player_name VARCHAR(10),
    team_name VARCHAR(10),
    team_id INT,
    position VARCHAR(10),
    uniform_number INT,
    birth VARCHAR(15),
    income INT,
    agent_id INT,
);

CREATE TABLE Player_Record (
    record_id INT PRIMARY KEY,
    player_id INT,
    start_date VARCHAR(15),
    end_date VARCHAR(15),
    team_id INT  
);
CREATE TABLE Agent (
    agent_id INT PRIMARY KEY,
    agent_name VARCHAR(10),
    age INT,
    contact_info VARCHAR(20)
);
CREATE TABLE Owner (
    owner_id INT PRIMARY KEY,
    team_id INT,
    owner_name VARCHAR(10),
    owner_age INT,
    budget INT
);
CREATE TABLE Team (
    team_id INT PRIMARY KEY,
    team_name VARCHAR(10),
    owner_id INT,
    director_id INT,
    establishment_year INT
);
CREATE TABLE Director (
    director_id INT PRIMARY KEY,
    director_name VARCHAR(10),
    director_year INT,
    team_id INT,
    income INT
);

CREATE TABLE Client (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(20),
    client_password VARCHAR(25),
    team_id INT,
    client_type VARCHAR(10)
);
CREATE TABLE Player_Agent (
    player_agent_id INT PRIMARY KEY,
    player_id INT,
    agent_id INT,
    team_id INT,
    contract_date VARCHAR(15),
    contract_term INT,
    contract_payment INT
);
CREATE TABLE Team_Award (
    team_award INT PRIMARY KEY
    awards_id INT,
    year INT,
    team_id INT
);
CREATE TABLE Individual_Award (
    individual_award INT PRIMARY KEY
    awards_id INT,
    year INT,
    player_id INT
);
CREATE TABLE Awards (
    awards_id INT PRIMARY KEY,
    awards_name VARCHAR(255)
);
CREATE TABLE Baseball_Records (
    baseball_records_id INT PRIMARY KEY,
    team1_id INT,
    team2_id INT,
    baseball_stadium_id INT,
    score VARCHAR(10)
);
CREATE TABLE Baseball_Stadium (
    baseball_stadium_id INT PRIMARY KEY,
    location VARCHAR(255),
    area VARCHAR(20),
    capacity INT
);

