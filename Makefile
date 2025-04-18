.PHONY: install activate run_app

install:
	echo "Definining the poetry configs..."
	poetry config virtualenvs.in-project true

	echo "Installing the dependencies..."
	poetry install --quiet

	echo "Installing pre-commit..."
	pre-commit install

activate:
	eval $(poetry env activate)

run_app:
	echo "Running the app. Access it at http://localhost:8501/"
	streamlit run app.py