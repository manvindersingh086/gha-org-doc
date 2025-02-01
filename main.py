from fastapi import FastAPI, Query, Cookie, Response
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


@app.get('/getEmp')
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