# py-mlops

py -m venv venv
venv\Scripts\activate
pip install pandas
pip install pytest
pip freeze
pip freeze > requeriments.txt
pytest .\test_request.py
pytest -vv  .\test_request.py
git add