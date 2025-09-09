 # Task Management System
 ## Quick Start
 ```bash
 # SSH clone
 git clone git@github.com:pabloabap/task-management-system.git
 #HTTPS clone
 #git clone https://github.com/pabloabap/task-management-system.git
 cd task-management-system
 cp .env.sample .env
 docker-compose up
 ```
 `.env.sample` contain variables `DEFAULT_SUPERUSER_` which define the superuser registered by default in the app. Feel free to modify it or login with it to interact with the app/api.
 `.env` is a link to `.env.sample` just to work directly with the variables defined on sample file but feel free to create another `.env`.

 **¿Do you want to change something on the fly?**
Go to [docker_compose.yml](docker-compose.yml) and inside django service uncomment `volume`attribute and execute the following commands to restart containers from 0:
```bash
	docker compose down # add -v if you also want to remove the volume of the database
	docker compose up
```


