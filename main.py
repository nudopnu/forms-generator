from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    name: str
    surname: str
    birthdate: date
    gender: str
    subscribed: bool

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("form.j2")

schema = User.model_json_schema()
html = template.render(schema=schema["properties"])

print(html)