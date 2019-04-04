
clean:
	find . -name '__pycache__' -exec rm -fr {} +

test:
	pytest

coverage-application: 
	pytest -x --cov=estimark/application tests/application/ \
	--cov-report term-missing -s

coverage-infrastructure: 
	pytest -x --cov=estimark/infrastructure tests/infrastructure/ \
	--cov-report term-missing -s

coverage: 
	pytest -x --cov=estimark tests/ --cov-report term-missing -s

bundle:
	pyinstaller estimark.spec

run:
	ESTIMARK_MODE=DEV; python -m estimark $(ARGS)