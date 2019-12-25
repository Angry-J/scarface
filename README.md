# Project Scarface

### Architecture  
- Postgres (RDB v12)
- Django Rest Framework (DRF)
- Dockerized

### Deployment
Dataloader (manage.py script)

### Development
TDD

REST API (DRF but maybe Flask)
- Self Documenting
- Paginated
- Read Only
- Authenticated
- Throttled
- Search
- Aggregates (countif, stats)
- Typed Views

Test Suite (pytest)
 - Coverage
 - Performance

Github Actions
- CI
- Coveralls
- Sentry
- Codacy
- Rollbar

Performance Monitor?  Just AWS tools? New Relic? Datadog? 

? CD: https://www.spinnaker.io


AWS:
Deployment pipeline (i.e. testing -> staging -> production)
Scaling (Fargate)


Target theoretical ReactJS frontend
- Maps
- Graphs
  - Time based
  - Value based

Some example queries:
 How many dogs named Butch are there? 
 What breeds are most often called butch?
 How long are most pets registered in the system?
 Most common/uncommon pet names?
 What zip codes have the most pit bulls? 



Development outline:
Get data into DB
Setup backups (for good practice the data won't really change)
Create Dockerized DRF instance
Hello world app that deploys to AWS environments <- this is more work than the actual app
Integration of services (i.e.  Coveralls, Sentry etc)
Write some scripts that explore the data and brainstorm insteresting queries
Document an API using Swagger
Implment endpoints using TDD
Add dog pictures from Wikipedia


Possible use a ReactJS dashboard template
