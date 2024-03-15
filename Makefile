SHELL=/usr/bin/env bash

.PHONY: install lint check upgrade run all

run:
	python main.py

install:
	if [[ -z $$VIRTUAL_ENV ]]; then echo activate venv; exit 1; fi
	pip install -r requirements.txt

lint:
	black main.py
	isort main.py
	autoflake --remove-all-unused-imports --expand-star-imports -i main.py
	flake8 --config .flake8 main.py

check:
	mypy main.py

upgrade:
	-pyupgrade --py310-plus main.py

all: install check upgrade lint run
