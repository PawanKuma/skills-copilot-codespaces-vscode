from fastapi import FastAPI

app = FastAPI()

@app.post("/login")
def login(username: str, password: str):
    # Your login logic here
    # Return appropriate response
    if username == "admin" and password == "admin":
        return {"message": "Login successful"}
    else:
        return {"message": "Login failed"}

@app.post("/logout")
def logout():
    # Your logout logic here
    # Return appropriate response