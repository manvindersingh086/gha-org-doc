from fastapi import FastAPI, Query, Depends, Cookie, Response,status, Form
from typing import Annotated
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

EmployeeList = [
    {
        "name" : "Manvinder Singh",
        "employeeId" : 1097623,
        "designation" : "Software Developer"
    },
     {
        "name" : "Deepak Gupta",
        "employeeId" : 1097624,
        "designation" : "Software Developer"
    },
       {
        "name" : "Manvinder Singh",
        "employeeId" : 1097623,
        "designation" : "Software Developer"
    },
]


@app.get('/getEmp', status_code=status.HTTP_302_FOUND)
async def getEmployeeById(empId: Annotated[int, Query(gt=5)]):
    employee = []
    for emp in EmployeeList:
        if emp.get("employeeId") == empId:
            employee.append(emp)
    return employee

#BODY PARAMETER AND QUERY PARAMETER EXAMPLE

class Employe(BaseModel):
    name: str = Field(examples=["John Singh"])
    employeeId: int
    designation: str

    

@app.post('/createEmployee')
async def createEmployee(employeeData: Employe):
     EmployeeList.append(employeeData)
     return EmployeeList


#COOKIES
@app.get("/readCookie")
async def readCookie(sessionId : Annotated[str| None, Cookie()] = None):
    if sessionId:
        return {"cookie_value": sessionId}
    return {"message": "No cookie found"}

@app.get("/set-cookie")
async def set_cookie(response: Response):
    # Set a cookie named "my_cookie" with value "fastapi_value"
    response.set_cookie(key="sessionId", value="1234567")
    return {"message": "Cookie has been set"}


## USING FORMS


@app.post("/login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return { "username" : username , "password": password}


class FormModels(BaseModel):
    username: str
    password: str

@app.post("/loginWithFormModel")
async def loginModel(data: Annotated[FormModels, Form()]):
    return { "username" : data.username , "password": data.password}


###  FASTAPI DEPENDENCY INJECTION

# async def common_parameters(q:str | None = None, skip : int =0, limit: int = 100):
#     return {"q" : q, "skip": skip, "limit": limit}


# @app.get("/items/")
# async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
#     return commons


# @app.get("/users/")
# async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
#     return commons


### CLASS AS A DEPENDENCY INJECTION

class common_parameters:
    def __init__(self, q: str | None = None, skip : int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons