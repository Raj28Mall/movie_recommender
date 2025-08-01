@echo off
echo 🛠 Setting up environment files...

REM Copy backend .env
IF EXIST backend\.env.example (
    copy backend\.env.example backend\.env >nul
    echo ✅ backend\.env created
) ELSE (
    echo ⚠️  backend\.env.example not found
)

REM Copy frontend .env
IF EXIST frontend\.env.example (
    copy frontend\.env.example frontend\.env >nul
    echo ✅ frontend\.env created
) ELSE (
    echo ⚠️  frontend\.env.example not found
)

echo 🐳 Building and starting containers...
docker compose up --build
