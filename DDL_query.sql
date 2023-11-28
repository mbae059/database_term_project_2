create database db_trade; 
use db_trade; 

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
    phone_number VARCHAR(20),
    FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE SET NULL
);
CREATE TABLE Player_Record (
    record_id INT PRIMARY KEY,
    player_id INT,
    start_date VARCHAR(15),
    end_date VARCHAR(15),
    team_id INT,
    FOREIGN KEY (player_id) REFERENCES Player(player_id) ON DELETE NO ACTION,
    FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE NO ACTION
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
FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE CASCADE
);
CREATE TABLE Team (
    team_id INT PRIMARY KEY,
    team_name VARCHAR(10),
    owner_id INT,
    director_id INT,
    establishment_year INT,
    FOREIGN KEY (owner_id) REFERENCES Owner(owner_id) ON DELETE SET NULL,
    FOREIGN KEY (director_id) REFERENCES Director(director_id) ON DELETE SET NULL
);
CREATE TABLE Director (
    director_id INT PRIMARY KEY,
    director_name VARCHAR(10),
    director_year INT,
    team_id INT,
    income INT,
    FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE SET NULL
);
CREATE TABLE User (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(20),
    user_password VARCHAR(25),
    team_id INT,
    user_type VARCHAR(10),
    FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE SET NULL
);
CREATE TABLE Player_Agent (
    player_id INT,
    agent_id INT,
    team_id INT,
    contract_date VARCHAR(15),
    contract_term INT,
    contract_payment INT,
    FOREIGN KEY (player_id) REFERENCES Player(player_id) ON DELETE NO ACTION,
    FOREIGN KEY (agent_id) REFERENCES Agent(agent_id) ON DELETE NO ACTION
);
CREATE TABLE Team_Award (
    awards_id INT,
    year INT,
    team_id INT,
    FOREIGN KEY (awards_id) REFERENCES Awards(awards_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE CASCADE
);
CREATE TABLE Individual_Award (
    awards_id INT,
    year INT,
    player_id INT,
    FOREIGN KEY (awards_id) REFERENCES Awards(awards_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES Player(player_id) ON DELETE CASCADE
);
CREATE TABLE Awards (
    awards_id INT PRIMARY KEY,
    awards_name VARCHAR(255)
);
CREATE TABLE Baseball_Records (
    records_id INT PRIMARY KEY,
    team1_id INT,
    team2_id INT,
    baseball_stadium_id INT,
    score VARCHAR(10),
    FOREIGN KEY (team1_id) REFERENCES Team(team_id) ON DELETE CASCADE,
    FOREIGN KEY (team2_id) REFERENCES Team(team_id) ON DELETE CASCADE,
    FOREIGN KEY (baseball_stadium_id) REFERENCES Baseball_Stadium(baseball_stadium_id) ON DELETE NO ACTION
);
CREATE TABLE Baseball_Stadium (
    baseball_stadium_id INT PRIMARY KEY,
    location VARCHAR(30),
    area VARCHAR(20),
    capacity INT
);
