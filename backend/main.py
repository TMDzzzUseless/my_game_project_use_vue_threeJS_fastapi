from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client, Client

# 從我們自己寫的 config.py 匯入金鑰
from config import SUPABASE_URL, SUPABASE_KEY

# 初始化 Supabase Client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
    email: str
    password: str

@app.get("/")
def read_root():
    return {"message": "FastAPI 後端與 Supabase Auth 連結準備就緒！"}

@app.post("/api/login")
def login(data: LoginRequest):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": data.email,
            "password": data.password
        })
        
        session = response.session
        user = response.user
        
        if session:
            return {
                "success": True,
                "message": "登入成功！",
                "access_token": session.access_token,
                "user": {
                    "id": user.id,
                    "email": user.email
                }
            }
        else:
            raise HTTPException(status_code=400, detail="登入失敗，請檢查 Email 或密碼")
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"登入失敗: {str(e)}")

    
# 👈 加上這段，讓你在命令列直接執行 python main.py 就能啟動並指定 port 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)