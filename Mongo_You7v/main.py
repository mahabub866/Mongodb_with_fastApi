# https://docs.mongoengine.org/guide/connecting.html
import json

from fastapi import FastAPI, HTTPException,Depends
from auth import create_access_token, get_password_hash,oauth2_scheme,authenticate_user
from models import Employee, NewEmployee, NewUser, User
from fastapi import Path, Query
from mongoengine import connect
from fastapi.security import OAuth2PasswordRequestForm
from mongoengine.queryset.visitor import Q
from datetime import timedelta
app = FastAPI()

connect(db="hrms", host="localhost", port=27017)

@app.post("/token")
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    username=form_data.username
    password=form_data.password
    print(username,password)
    if authenticate_user(username,password):
        access_token=create_access_token(data={"sub":username},expires_delta=timedelta(minutes=30))
        return {"access_token":access_token,"token_type":"bearer"}
    else:
        raise HTTPException(status_code=401,detail="Incorrect username or password")


@app.get('/')
def home(token:str=Depends(oauth2_scheme)):
    return { "token":token}

@app.get('/all-employee')
def all_employees():
    # employees=Employee.objects().to_json()

    employees_list = json.loads(Employee.objects().to_json())
    # print(type(employees_list)
    # print(employees)
    return {"employees": employees_list}


@app.get('/employee/{id}')
def employee(id: int = Path(..., gt=0)):
    # print(emp_id)
    employee = Employee.objects.get(employee_id=id)

    employee_dict = {
        "employee_id": employee.employee_id,
        "name": employee.name,
        "age": employee.age,
        "teams": employee.teams
    }
    return employee_dict


@app.get('/search/employees/')
def search_employees(name, age: int = Query(None, gt=18)):
    employees = json.loads(Employee.objects.filter(
        Q(name__icontains=name) | Q(age=age)).to_json())

    return {"employees": employees}


@app.post("/add/employees/")
def add_employee(request: NewEmployee):
    new_employee = Employee(employee_id=request.employee_id,
                            name=request.name, age=request.age, teams=request.teams,
                            )
    new_employee.save()

    return {"message": "Added employee Successfully"}

@app.post("/sign_up")
def sign_up(request: NewUser):
    user=User(username=request.username, password=get_password_hash(request.password))
    user.save()
    return {"message": "New User Successfully"}