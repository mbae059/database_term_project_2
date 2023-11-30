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