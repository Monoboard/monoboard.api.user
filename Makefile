lint:
	pylint --rcfile=.pylintrc ./src/ --init-hook='sys.path.extend(["./src/"])'
build:
	docker build -t <TODO: service name> .
