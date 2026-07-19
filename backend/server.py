// https://github.com/locususer/Day-1-frontendfrom 

fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods=["*"],
    allow_headers =["*"]
)

#{
#    id: 1,
#    name: "Coffee",
#    amount: 100
# }

expenses =[]
next_id =1

@app.get("/expenses")
def get_expenses():
    return expenses


@app.post("/expenses")
def add_expense(expense:dict):
    global next_id
    expense["id"]=next_id
    next_id+=1
    expenses.append(expense)
    return expense


# @app.delete("/expenses/{expense_id}")
# def delete_expense(expense_id:int):
#     for expense in expenses:
#         if expense["id"]==expense_id:
#             expenses.remove(expense)
#             return{"message":"expense deleted"}
#     return {"message":" expense not found"}