# my_game_project_use_vue_threeJS_fastapi
VUE3+threeJS+fastapi+superbase
##第一階段：增加frontend&backend資料夾
##1.增加前端設定
### 進入 frontend 資料夾
cd frontend
### 使用 Vite 建立 Vue + TypeScript 專案 (名稱用 . 代表當前資料夾)
npm create vite@latest . -- --template vue-ts
### 安裝基本依賴套件
npm install
### 安裝 TresJS 核心與 Three.js 相關套件
npm install three @tresjs/core
##2.增加後端設定
### 回到根目錄並進入 backend
cd ../backend
### 建立 Python 虛擬環境
python3 -m venv venv
### 啟動虛擬環境
source venv/bin/activate
### 安裝 FastAPI、Uvicorn（伺服器運行工具）以及 Supabase Python 套件
pip install fastapi uvicorn supabase python-dotenv
##3.一個簡單的 FastAPI 測試檔案 main.py