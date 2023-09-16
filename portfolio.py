from fastapi import FastAPI, Query, Path, Body, Form, HTTPException
from enum import Enum
from pydantic import BaseModel, Field
from typing import Annotated


app = FastAPI()


# When defining a Union, include the most specific type first, followed by the less specific type

class Person(BaseModel):
    phone_number : int | None = Field(..., max_length=200, description="this is where your Phone Number should go.", title="this is for your Phone Number")
    Email : str | None = ...

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "Phone Number": "070********8",
                        "Email": "Freeman*****@gmail.com",
                    }
                ]
            }
        }
# +++++++++++++++++++++++
class Gender(str, Enum):
    Male = "Male"
    Female = "Female"

@app.get("/")
async def index(): 
    return {"message": "Hello World"}


@app.post("/person_info")
async def person_info(
    gender: Gender | None = Form(
        ...,
          description="tell us the Gender you belong to"
          ), 
    person : Person = Body(
        ...,
         description="this cannot be left blank"
         ), 
    Freeman: str = Body(),
    ) -> dict[str]:
    if gender.value == "Male":
        return {"msg" : "welcome My guy",
                    "response" : person, 
                    "freeman": Freeman
                    }
    elif gender.value == "Female":
        return {
            "msg" : "welcome My lady",
            "response" : person, 
            "freeman": Freeman
            }
    raise HTTPException(status_code=402, detail="you can't tell me that")

@app.patch("/{person_id}")
async def update_user(person_id  : int, schema : Person):
    return {"person_id": person_id, "person": schema}