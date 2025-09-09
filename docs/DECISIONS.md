# Features completed and why
- Set up docker infrastructure from scratch, create `docker-compose-yml` and verify all containers communicate properly:
Without infrastructure the project can't work so my first step was to configure correctly the infrastructure. Starting by running
a single django container, adding PostgreSQL migrating the database to it to start running. Next I setting up Redis and Celery for the next steps.
- Django project structure, model and migration: Once infrastructure was ready I continued with this step as is crucial to have a project structure and a data model working garantee a good performance of the rest of the solution. I followed the sugestion of test subject but I decided to also include `api` folder inside `apps` folder  to have
all api logics grouped.
- Complete authentication system: Crucial to interact with the solution and log users interactions. The user can register, login and logout but refresh wasn't implemented as we implement BaseAuthentication, not TokenAuthentication.
- CRUD endpoints: All User Management endpoints are available. Task Management endpoints are almost implemented, go to [API_DOCUMENTATION](./API_DOCUMENTATION.md) to see which ones. The other ones weren't implemented because a lack of time.
- Basic frontend UI: '/tasks' and '/tasks/{int:id}' has a very humble HTML to see a list of tasks and task deatails.

# Features skipped and why



# Time allocation breakdown
Most of my time was dedicated to understand Django and Django Rest Framework. It is my first time using these frameworks and I had to learn the bases from scratch, mainly from 
official docummentations. Having said this I tried to follow the deployment timeline suggestion with the final result of:
- Day 1 (Friday 5): Set up Dockerfile for Django and create a docker-compose.yml with PostgresSQL and Redis services available.
- Day 2 (Saturday 6): Add Celery to docker-compose.yml and test the complete infrastructure. Understand Django MVT (Model View Template) architecture and first steps with it:
creating `tasks` model, views, urls and templates, understanging `settings.py` file and making my first migrations.
- Day 3 (Sunday 7): Build the other models required and understand Django Rest Framework. This day I didn't do a commit because there weren't any real progression at the project but a understanding of the framework (serializationS, views, viewsets, pagination, filtering, routing among others)
- Day 4 (Monday 8): I cleaned testing files created the day before to understand how to build the API's. Inside `apps/api` I built aathentication, user management and part of task management APIs endpoints.
- Day 5 (Tuesday 9): Project revision, documentation and latests features progression on task management API.

# Technical challenges faced
- Set up docker infrastructure from scratch, create `docker-compose-yml` and verify all containers communicate properly: I was focus on build light and solid infrastructure.
Some of the decission that I took were use the same base image for Djanfo and Celery with a different entrypoint command as the base of both is Python and some libraries. A part from that I switched the docker image `python:3.13.7` to `python:3.11-slim` to reduce timmings on image construction, moving from 90.7s to 32.9s and from 1.16GB image to 183MB.


# Trade-offs made
# What you would add with more time
# Justification for using Django templates for the frontend