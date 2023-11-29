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
    owner_age INT
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
    Client_id INT PRIMARY KEY,
    Client_name VARCHAR(20),
    Client_password VARCHAR(25),
    team_id INT,
    Client_type VARCHAR(10)
);
CREATE TABLE Player_Agent (
    player_id INT,
    agent_id INT,
    team_id INT,
    contract_date VARCHAR(15),
    contract_term INT,
    contract_payment INT
);
CREATE TABLE Team_Award (
    awards_id INT,
    year INT,
    team_id INT
);
CREATE TABLE Individual_Award (
    awards_id INT,
    year INT,
    player_id INT
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
    score VARCHAR(10)
);
CREATE TABLE Baseball_Stadium (
    baseball_stadium_id INT PRIMARY KEY,
    location VARCHAR(30),
    area VARCHAR(20),
    capacity INT
);

ALTER TABLE Player
ADD CONSTRAINT fk_Player_reference_Team
FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE SET NULL;

ALTER TABLE Player_Record
ADD CONSTRAINT fk_Player_Record_reference_Player
FOREIGN KEY (player_id) REFERENCES Player(player_id) ON DELETE NO action,
ADD CONSTRAINT fk_Player_Record_reference_Team
FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE no action;

ALTER TABLE Owner
ADD CONSTRAINT fk_Player_Record_reference_Team
FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE CASCADE;

ALTER TABLE Team
ADD CONSTRAINT fk_Team_reference_Owner
FOREIGN KEY (owner_id) REFERENCES Owner(owner_id) ON DELETE SET NULL,
ADD CONSTRAINT fk_Team_reference_Director
FOREIGN KEY (director_id) REFERENCES Director(director_id) ON DELETE SET NULL;

ALTER TABLE Director
ADD CONSTRAINT fk_Director_reference_Team
FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE SET NULL;

ALTER TABLE Client
ADD CONSTRAINT fk_Client_reference_Team
FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE SET NULL;

ALTER TABLE Player_Agent
ADD CONSTRAINT fk_Player_Agent_reference_Player
FOREIGN KEY (player_id) REFERENCES Player(player_id) ON DELETE NO ACTION,
ADD CONSTRAINT fk_Player_Agent_reference_Agent
FOREIGN KEY (agent_id) REFERENCES Agent(agent_id) ON DELETE NO ACTION;

ALTER TABLE Team_Award
ADD CONSTRAINT fk_Team_Award_reference_Award
FOREIGN KEY (awards_id) REFERENCES Awards(awards_id) ON DELETE CASCADE,
ADD CONSTRAINT fk_Team_Award_reference_Team
FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE CASCADE;

ALTER TABLE Individual_Award
ADD CONSTRAINT fk_Individual_Award_reference_Award
FOREIGN KEY (awards_id) REFERENCES Awards(awards_id) ON DELETE CASCADE,
ADD CONSTRAINT fk_Individual_Award_reference_Player
FOREIGN KEY (player_id) REFERENCES Player(player_id) ON DELETE cascade;

ALTER TABLE Baseball_Records
ADD CONSTRAINT fk_Baseball_Records_reference_Team1
FOREIGN KEY (team1_id) REFERENCES Team(team_id) ON DELETE cascade,
ADD CONSTRAINT fk_Baseball_Records_reference_Team2
FOREIGN KEY (team2_id) REFERENCES Team(team_id) ON DELETE cascade,
ADD CONSTRAINT fk_Baseball_Records_reference_Baseball_Stadium
FOREIGN KEY (baseball_stadium_id) REFERENCES Baseball_Stadium(baseball_stadium_id) ON DELETE NO ACTION;