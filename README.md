# Database Term Project

KBO baseball database system

Schema change proposal
--------
[Agent](#agent)

[Owner](#owner)

[User](#user)

# User
- admin
- player
- director
- owner
- agent
- general user

# Function
- to lazy to write this down. See PDF

# Database Schema
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

<a name="agent"></a>
Agent(agent_name, age, contact_info)
```
Subject : Field player_id should be deleted
Reason :
1. player_agent already has that information?
2. agent could manage multiple players and that data could not fit inside in single column
3. That data could be derived from Player Schema. The player has agent_id so the query could be made using sql
```
<a name="owner">Owner(**team_id**, owner_name, owner_age, budget)</a>
> team_id(Team) : on delete cascade
```
Subject : Field budget should be deleted
Reason :
1. It is much more suitable for Team Schema to have that information 
```

Team(team_name, **owner_id**, **director_id**, establishment_year)
> owner_id(Owner) : on delete set null (or cascade?)
> director_id(Director) : on delete set null

Director(director_name, director_year, **team_id**, income)
> team_id(Team) : on delete set null

<a name="user">User(user_id, user_name, user_password, **team_id**, user_type)</a>
> team_id(Team) : on delete set null

```
Subject : user type should be added
Reason :
1. admin, player, owner, agent should be able to login as well
```

Player_Agent(**player_id**, **agent_id**, team_id, contract_date, contract_term, budget)
> player_id(Player) : on delete no action
> agent_id(Agent) : on delete no action
```
Subject : If budget means 계약금, then it should be changed
Reason :
1. budget is not a suitable word
```

Player_Trade_Status(date, **team_id**, **player_id**, player_state)
> team_id(Team) : on delete no action
> player_id(Player) : on delete no action
```
Subject : This schema should be deleted if player could be traded only if agent is present
Reason :
1. If there player could be traded only when agent is present, then this schema servers the same purpose as Player_Agent?
```

Team_Award(**awards_id**, year, **team_id**)
> awards_id(Award) : on delete cascade
> team_id(Team) : on delete cascade

Individual_Award()
