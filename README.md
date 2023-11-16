# Database Term Project

KBO baseball database system

Schema change proposal
--------
[Agent : player_id](#Agent : player_id)

1. User
- admin
- player
- director
- owner
- agent
- general user

2. Function
- to lazy to write this down. See PDF


3. Database Schema
> Database Schema will be changed as it is not determined yet
> This is the abstract version and used to see the overall flow

> Every Schema PK is the default id that is given when creating the schema

> Some field in the schema will be **BOLD** which means that it is FK.<br>

> FK explanation<br>
> field(schema) : on delete ...

Player(player_name, team_name, **team_id**, position, uniform_number, birth, income, agent_id, phone_number)
> team_id(Team) : on delete set null.

Player_record(**player_id**, start_date, end_date, **team_id**)
> player_id(Player) : on delete no action
> team_id(Team) : on delete no action

<a name="Agent : player_id">
Agent(agent_name, age, contact_info)
