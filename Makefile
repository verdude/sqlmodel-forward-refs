lint:
	black main.py
	isort main.py
	autoflake --remove-all-unused-imports --expand-star-imports -i main.py
	flake8 --config .flake8 main.py

check:
	mypy main.py

upgrade:
	pyupgrade --py310-plus main.py
