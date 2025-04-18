.PHONY: install activate run_app

install:
	echo "Definining the poetry configs..."
	poetry config --list | grep -q 'virtualenvs.in-project = true' || poetry config virtualenvs.in-project true

	echo "Installing the dependencies..."
	poetry install --quiet

	@echo "Install git"
	@if [ ! -d .git ]; then \
		echo "Initializing Git repository..."; \
		git init; \
	else \
		echo "Git already initialized."; \
	fi

	echo "Installing pre-commit..."
	pre-commit clean
	pre-commit autoupdate
	pre-commit install

	@echo "Activate your venv, run: eval \$$(poetry env activate)"

activate:
	eval $(poetry env activate)

run_app:
	echo "Running the app. Access it at http://localhost:8501/"
	streamlit run app.py