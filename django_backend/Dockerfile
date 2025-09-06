FROM	python:3.11-slim

ENV		PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1
WORKDIR /app
COPY	. /app/
RUN		pip install --upgrade pip && pip install -r requirements.txt
EXPOSE	8000
#COPY --chmod=777 "./scripts/entrypoint.sh" "./entrypoint.sh"
CMD ["bash", "/app/scripts/entrypoint.sh"]

