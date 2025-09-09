Bellow you can see all API endpoints available in the app. `http://localhost:8000/{api_endpoint}` will redirect you to the Browsable API, a UI like postman to interact with the API and see details about endpoint.

# Authentication Endpoints

- **POST** `/api/auth/register/` - Endpoint to register new users. The content to post must be:

	```JSON
		{
			"username": "",
			"password": ""
		}
	```
- **POST** `/api/auth/login/` - User authentication.
	```JSON
		{
			"csrfmiddlewaretoken": "",
			"next": "",
			"username": "",
			"password": ""
		}
	```
- **POST** `/api/auth/logout/` - User authentication exit
	```JSON
		{
			"csrfmiddlewaretoken": ""
		}
	```
 
 # User Management

- **GET** `/api/users/[?page_size=<int>]` (list with pagination) - Show all users registered in the app. By default 1 register per page and 10 registers per page maximum. To modifiy default one specify the number in get request.
- **GET** `/api/users/{id}/` - Obtain all details from one user.
- **PUT** `/api/users/{id}/` - Modify all details of a user.
	```JSON 
		{
			"id": 2,
			"username": "",
			"password": "",
			"created_tasks": [],
			"assigned_tasks": []
		}
	```
- **GET** `/api/users/me/` - Obtain your user details if you are logedin
 
# Task Management
- **GET** `/api/tasks/` (with filtering, search, pagination) - Show all tasks.
- **POST** `/api/tasks/` - Publish a new task
	```JSON
		{
			"tags": [],
			"title": "",
			"description": "",
			"status": null,
			"priority": null,
			"due_date": null,
			"estimated_hours": null,
			"actual_hours": null,
			"metadata": null,
			"is_archived": false,
			"parent_task": null,
			"assigned_to": []
		}
	```
- **GET** `/api/tasks/{id}/` - Obtain details of a task
- **PUT** `/api/tasks/{id}/` - Modify all details of a task
	```JSON
		{
			"tags": [],
			"title": "",
			"description": "",
			"status": null,
			"priority": null,
			"due_date": null,
			"estimated_hours": null,
			"actual_hours": null,
			"metadata": null,
			"is_archived": false,
			"parent_task": null,
			"assigned_to": []
		}
	```
- **PATCH** `/api/tasks/{id}/` - Modify some detail of a task
	```JSON
		{
			"tags": [],
			"title": "",
			"description": "",
			"status": null,
			"priority": null,
			"due_date": null,
			"estimated_hours": null,
			"actual_hours": null,
			"metadata": null,
			"is_archived": false,
			"parent_task": null,
			"assigned_to": []
		}
	```
- **DELETE** `/api/tasks/{id}/` - Delete a task

