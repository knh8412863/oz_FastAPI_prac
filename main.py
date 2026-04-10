from fastapi import FastAPI

# 127.0.0.1:8000 서버 실행
app = FastAPI()

# Python 데코레이터: 파이썬 함수에 추가적인 기능을 부여하는 문법

# GET / 요청이 들어오면, root_handler 라는 함수를 실행하라
@app.get("/")
def root_handler():
    return {"ping": "pong"}

# GET /hello 요청이 들어오면, hello_handler() 실행
@app.get("/hello")
def hello_handler():
    return {"message": "Hello from FastAPI"}

# 임시 데이터베이스
users = [
        {"id": 1, "name": "alex", "job": "student"},
        {"id": 2, "name": "bob", "job": "sw engineer"},
        {"id": 3, "name": "chris", "job": "barista"}
]

# 전체 사용자 목록 조희 API
# GET /users
@app.get("/users")
def get_users_handler():
    return users

# 단일 사용자 데이터 조희 API
# GET /users/{user_id} -> {user_id}번 사용자 데이터 조회
@app.get("/users/{user_id}")
def get_user_one_handler(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user