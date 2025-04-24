import os
import psycopg2 # biblioteka do łączenia się z bazą danych
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel # biblioteka do walidacji danych w Pythonie


app = FastAPI()
DATABASE_URL = f"postgresql://{os.environ['DB_USER']}:{os.environ.get['DB_PASSWORD']}@{os.environ.get['DB_ADDRESS']}:5432/{os.environ.get['DB_TABLE']}"


# Model danych wejściowych
class Person(BaseModel):
    name: str
    surname: str
    position: str
    salary: float


# Endpoint do wstawiania danych do bazy danych
@app.post("/people")
def create_entry(person: Person):
    name = person.name
    surname = person.surname
    position = person.position
    salary = person.salary
    
    # logika do wstawiania danych do bazy danych
    
    return {"message": "Person created successfully!"}


# aby dodać dane, wywołaj w konsoli:
# curl -X 'POST' 'http://localhost:8000/people' -H 'Content-Type: application/json' -d '{"name": "Jan","surname": "Kowalski","position": "Intern","salary": 3000.00}'


# Sprawdzanie, czy skrypt jest uruchamiany bezpośrednio
if __name__ == "__main__":
    # Uruchamianie aplikacji FastAPI za pomocą Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
