lint:
	black main.py
	autoflake -i main.py
	isort main.py
	flake8 --config .flake8 main.py

check:
	mypy main.py

upgrade:
	pyupgrade main.py
