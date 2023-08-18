# FastAPI + SqlAlchemy + alembic

This template is an initial up and go template. 


### Run the application without docker

Create Python virtual environment and activate it (Unix OS)
```sh
python3 -m venv venv
source ./venv/bin/activate
```
Install all the dependencies
```
pip install -r requirements.txt
```
Run the application with the command ``uvicorn app.main:app --reload``