install:
	@sudo apt-get install -y libpq-dev

db-shell:
	@docker exec -it psql-db psql -U everardo.sanchezh psql-db

start:
	@docker compose -f ./utils/docker/compose.yml up -d
	@uv run uvicorn main:app --reload