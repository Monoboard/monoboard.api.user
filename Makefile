lint:
	black --config black.toml src/
build:
	docker build -t petrushynskyi/monoboard.api.user .
publish:
	docker push petrushynskyi/monoboard.api.user:latest
