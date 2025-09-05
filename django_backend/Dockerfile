FROM	python:3.11-slim

ENV		PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1
WORKDIR /app
RUN		pip install --upgrade pip
COPY 	requirements.txt .
RUN		pip install -r requirements.txt
COPY	--chmod=755 ./scripts/entrypoint.sh /app/entrypoint.sh
COPY	manage.py .
COPY	./config /app/config
EXPOSE	8000
#COPY --chmod=777 "./scripts/entrypoint.sh" "./entrypoint.sh"
ENTRYPOINT ["/app/entrypoint.sh"]

