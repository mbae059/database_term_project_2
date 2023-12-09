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
- general user

# Function
- to lazy to write this down. See PDF

# Database Schema
> Database Schema will be changed as it is not determined yet.
> This is the abstract version and should be used to see the overall flow

> Every Schema PK is the default id that is given when creating the schema

> Some field in the schema will be **BOLD** which means that it is FK.<br>

> FK explanation<br>
> field(schema) : on delete ...

player(id, name, position, birth)
> team_id(Team) : on delete set null.

team(id, name, establishment_year)

belongs_to(id, **player_id**, **team_id**, start_date, uniform_number, contract_term, contract_payment)
> player_id(player) : on delete set null
> team_id(team) : on delete set null

owner(id, name, age, budget)

owns(id, **owner_id**, **team_id**)
> owner_id(owner) : on delete set null
> team_id(team) : on delete set null

director(id, name, start_date) 
> start_date means what year did this director start directing baseball teams

directs(id, **director_id**, **team_id**, contract_term, start_date, contract_payment)
> director_id(director) : on delete set null
> team_id(team) : on delete set null

awards(id, name)

player_won(id, **player_id**, **awards_id**)
> player_id(player) : on delete cascade
> awards_id(awards) : on delete cascade

team_won(id, **team_id**, **awards_id)
> team_id(team) : on delete cascade
> awards_id(awards) : on delete cascade

client(id, name, password, **team_id**, client_type)
> team_id(Team) : on delete set null
> team_id indicates what team this client is part of or supports.
> 
```
list of client_type
admin
player
director
owner
general_user
```




