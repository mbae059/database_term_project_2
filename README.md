# Database Term Project

KBO baseball database system

Schema change proposal
--------

Schema
------------

# User
- admin
- player
- director
- owner
- agent
- general user
- team

# Function
- to lazy to write this down. See PDF

# Database Schema
> Database Schema will be changed as it is not determined yet.
> This is the abstract version and should be used to see the overall flow

> Every Schema PK is the default id that is given when creating the schema

> Some field in the schema will be **BOLD** which means that it is FK.<br>

> FK explanation<br>
> field(schema) : on delete ...

Player(player_name, team_name, **team_id**, position, uniform_number, birth, income, agent_id)
> team_id(Team) : on delete set null.

```
Deprecated
Though the generator still exists, it will no longer be used
Player_record(**player_id**, start_date, end_date, **team_id**)
> player_id(Player) : on delete no action
> team_id(Team) : on delete no action
```
Agent(agent_name, age, contact_info)

Owner(**team_id**, owner_name, owner_age, budget)
> team_id(Team) : on delete cascade

Team(team_name, **owner_id**, **director_id**, establishment_year)
> owner_id(Owner) : on delete set null (or cascade?)
> director_id(Director) : on delete set null

Director(director_name, director_year, **team_id**, income)
> team_id(Team) : on delete set null

Client(client_name, client_password, **team_id**, client_type)
> team_id(Team) : on delete set null

```
list of client_type
admin
player
director
owner
agent
general_user
GM (general_manager)
```
Player_Agent(**player_id**, **agent_id**, team_id, contract_date, contract_term, contract_payment)
> player_id(Player) : on delete no action
> agent_id(Agent) : on delete no action

Team_Award(**awards_id**, year, **team_id**)
> awards_id(Award) : on delete cascade
> team_id(Team) : on delete cascade

Individual_Award(**awards_id**, year, **player_id**)
> awards_id(Award) : on delete cascade
> player_id(Player) : on delete cascade

Awards(awards_name)

Baseball_Records(**team1_id**, **team2_id**, **baseball_stadium_id**, score)
> team1_id(Team) : on delete cascade
> team2_id(Team) : on delete cascade
> baseball_stadium_id(Baseball_Stadium) : on delete no action

Baseball_Stadium(location, area, capacity)
