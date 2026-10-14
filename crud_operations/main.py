from fastapi import FastAPI
from crud_operations.data_models import (
    NewEmployee,
    UpdateEmployee,
)


app = FastAPI(  # instance of our application
    title="CRUD-operation",
    description="This API will implement CRUD",
)

employees = {
    1: {
        "name": "Michael",
        "age": 49,
        "pos": "Manager",
    },
    2: {
        "name": "Saksham",
        "age": 21,
        "pos": "Intern",
    },
}


# Home page of our API
@app.get("/")
def index():
    return "Welcome to this API for CRUD operations"


@app.get("/employees")
def get_employees():
    return employees


@app.get("/employee/{emp_id}")
def get_employee(emp_id: int):
    if emp_id not in employees:
        return {"message": "Employee not found"}
    return employees[emp_id]


@app.post("/add-employee")
def add_employee(emp: NewEmployee):
    if not employees:
        new_id = 1
    else:
        new_id = max(employees.keys()) + 1
    employees[new_id] = emp.model_dump()
    return employees[new_id]


@app.put("/update-employee/{emp_id}")
def update_employee(emp_id: int, emp: UpdateEmployee):
    if emp_id not in employees:
        return {"message": f"No employees found with ID = {emp_id}"}

    if emp.name is not None:
        employees[emp_id]["name"] = emp.name

    if emp.age is not None:
        employees[emp_id]["age"] = emp.age

    if emp.pos is not None:
        employees[emp_id]["pos"] = emp.pos

    return employees[emp_id]


@app.delete("/delete-employee/{emp_id}")
def delete_employee(emp_id: int):
    if emp_id not in employees:
        return {"message": f"No employees found with ID = {emp_id}"}

    del employees[emp_id]
    return employees 

