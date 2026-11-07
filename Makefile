.PHONY: up down logs helm-lint
up:
	docker compose up --build
down:
	docker compose down
logs:
	docker compose logs -f
helm-lint:
	helm lint deploy/helm/brightcart
