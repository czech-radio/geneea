init:
	pip install -e ".[test,docs,lint]"

test:
	pytest -v -s