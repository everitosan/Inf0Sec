import os
import psycopg2
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# Db connection
conn = psycopg2.connect(
  host=os.getenv("POSTGRES_HOST"),
  port=os.getenv("POSTGRES_PORT"),
  database=os.getenv("POSTGRES_DB"),
  user=os.getenv("POSTGRES_USER"),
  password=os.getenv("POSTGRES_PASSWORD")
)

cursor = conn.cursor()

@app.get("/search")
def search(name: str):
  query = f"SELECT * FROM users WHERE name = '{name}'"
  print("#"*10)
  print(query)
  print("#"*10)
  cursor.execute(query)
  result = cursor.fetchall()
  return {"result": result}


@app.get("/greet", response_class=HTMLResponse)
def greet(name: str):
  return f"<h1>Hola, {name}</h1>"