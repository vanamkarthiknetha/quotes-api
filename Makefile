.PHONY: up down test logs shell tunnel

up:
	docker compose up --build -d

down:
	docker compose down

test:
	docker compose run --rm api pytest -v

logs:
	docker compose logs -f api

shell:
	docker compose exec api bash

tunnel:
	docker compose --profile tunnel up --build -d
	@echo "Waiting for the public tunnel URL..."
	@for i in $$(seq 1 30); do \
		url=$$(docker compose logs tunnel 2>/dev/null | grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com' | head -1); \
		if [ -n "$$url" ]; then echo "Public URL: $$url"; exit 0; fi; \
		sleep 1; \
	done; \
	echo "Tunnel URL not ready yet. Check: docker compose logs tunnel"; \
	exit 1
