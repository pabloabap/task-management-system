FROM	python:3.13.7
WORKDIR /app
RUN		pip install --upgrade pip
COPY 	requirements.txt .
RUN		pip install -r requirements.txt
COPY	manage.py .
COPY	./config /app/config
EXPOSE	8000
#COPY --chmod=777 "./scripts/entrypoint.sh" "./entrypoint.sh"
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

