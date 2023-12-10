CREATE TABLE player (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    position VARCHAR(255),
    birth DATE
);

CREATE TABLE team (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    establishment_year INT
);
CREATE TABLE belongs_to (
    id SERIAL PRIMARY KEY,
    player_id INT,
    team_id INT,
    start_date DATE,
    uniform_number INT,
    contract_term INT,
    contract_payment INT,

    foreign key (player_id) references player(id) on delete cascade,
    foreign key (team_id) references team(id) on delete cascade
);
CREATE TABLE owner (
    id SERIAL PRIMARY KEY,
    name VARCHAR(25),
    age INT,
    budget INT
);
CREATE TABLE owns (
    id SERIAL PRIMARY KEY,
    owner_id INT,
    team_id INT,

    foreign key (owner_id) references owner(id) on delete cascade,
    foreign key (team_id) references team(id) on delete cascade
);
CREATE TABLE director (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    start_date DATE
);

CREATE TABLE directs (
    id SERIAL PRIMARY KEY,
    director_id INT,
    team_id INT,
    contract_term INT,
    start_date DATE,
    contract_payment INT,

    foreign key (director_id) references director(id) on delete cascade,
    foreign key (team_id) references team(id) on delete cascade
);
CREATE TABLE awards (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);
CREATE TABLE player_won (
    id SERIAL PRIMARY KEY,
    player_id INT,
    awards_id INT,

    foreign key (player_id) references player(id) on delete cascade,
    foreign key (awards_id) references awards(id) on delete cascade
);
CREATE TABLE team_won (
    id SERIAL PRIMARY KEY,
    team_id INT,
    awards_id INT,

    foreign key (team_id) references team(id) on delete cascade,
    foreign key (awards_id) references awards(id) on delete cascade
);
CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    password VARCHAR(255),
    team_id INT,
    client_type VARCHAR(255),

    foreign key (team_id) references team(id) on delete cascade
);

