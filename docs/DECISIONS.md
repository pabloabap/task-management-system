# Features completed and why
- Set up docker infrastructure from scratch, create `docker-compose-yml` and verify all containers communicate properly:
Without infrastructure the project can't work so my first step was to configure correctly the infrastructure. Starting by running
a single django container, adding PostgreSQL migrating the database to it to start running. Next I setting up Redis and Celery for the next steps.
- Django project structure, model and migration: Once infrastructure was ready I continued with this step as is crucial to have a project structure and a data model working garantee a good performance of the rest of the solution. I followed the sugestion of test subject but I decided to also include `api` folder inside `apps` folder  to have
all api logics grouped.
- Complete authentication system: Crucial to interact with the solution and log users interactions. The user can register, login and logout but refresh wasn't implemented as we implement BaseAuthentication, not TokenAuthentication.
- CRUD endpoints: All User Management and Task Management endpoints are implemented, go to [API_DOCUMENTATION](./API_DOCUMENTATION.md) to see details. Task Operations weren't implemented because a lack of time.
- Basic frontend UI: `/tasks` and `/tasks/{int:id}` has a very humble HTML to see a list of tasks and task deatails.

# Features skipped and why
Because of lack of time I couldn't implement:
- Basic API and frontend tests.
- Celery tasks and scheduled jobs.
- Filteringn and search API functionalities
- Frontend forms to create tasks.
- Kafka and Flask microservices.
- Performance optimizations.
- Deep testing.

This lack of time was mainly caused by an unknowledge of the technologies that push me to speend a lot of time investigating about their user.


# Time allocation breakdown
Most of my time was dedicated to understand Django and Django Rest Framework. It is my first time using these frameworks and I had to learn the bases from scratch, mainly from 
official docummentations. Having said this I tried to follow the deployment timeline suggestion with the final result of:
- Day 1 (Friday 5): Set up Dockerfile for Django and create a docker-compose.yml with PostgresSQL and Redis services available.
- Day 2 (Saturday 6): Add Celery to docker-compose.yml and test the complete infrastructure. Understand Django MVT (Model View Template) architecture and first steps with it:
creating `tasks` model, views, urls and templates, understanging `settings.py` file and making my first migrations.
- Day 3 (Sunday 7): Build the other models required and understand Django Rest Framework. This day I didn't do a commit because there weren't any real progression at the project but a understanding of the framework (serializationS, views, viewsets, pagination, filtering, routing among others)
- Day 4 (Monday 8): I cleaned testing files created the day before to understand how to build the API's. Inside `apps/api` I built aathentication, user management and part of task management APIs endpoints.
- Day 5 (Tuesday 9): Project revision, documentation, latests features progression on task management API and Celery first implementation `send_task_notification`. This notification alert all users about task changes.

# Technical challenges faced
- Set up docker infrastructure from scratch, create `docker-compose-yml` and verify all containers communicate properly: I was focus on build light and solid infrastructure.
Some of the decission that I took were use the same base image for Djanfo and Celery with a different entrypoint command as the base of both is Python and some libraries. A part from that I switched the docker image `python:3.13.7` to `python:3.11-slim` to reduce timmings on image construction, moving from 90.7s to 32.9s and from 1.16GB image to 183MB.


Important to user CSRF cookie when submit  login from culr command to accept login.


Almost all the project technologies were new for me. The most important challenges I found were to understand de usage and features of each framework and how to integrate them in a solution.

# Trade-offs made
To test Celery notifications via email without linking it with a real SMTP server **mailhog** service where added as microservice. Mailhog is a local SMTP server that intercept all email communications and show them in a ficticious mailbox. All generated emails can be visualized in `http://localhost:8025`.
I thought it is a good enhancement as all users of the team can test this functionality without sharing personal credentials and lowering their personal email reputantion sending junk emails.

Last day I priotirize the implementation of a Celery task than complete all API functionalities to demonstrate that I handeled all the types of tasks of mandatory part.

# What you would add with more time
I really miss to build a complete and usable solution. Basically finish all API endpoints, implement Celery automations and implement good frontend.

# Justification for using Django templates for the frontend
It is very usefull to use templates to render HTML pages on the fly with some dynamic fieds or areas of the page. Also they can be recycled and combined on demand.
