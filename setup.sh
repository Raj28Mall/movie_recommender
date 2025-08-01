#!/bin/bash

echo "Setting up environment files..."

# Copy .env.example to .env for backend
if [ -f ./backend/.env.example ]; then
  cp ./backend/.env.example ./backend/.env
  echo "backend/.env created"
else
  echo " backend/.env.example not found"
fi

# Copy .env.example to .env for frontend
if [ -f ./frontend/.env.example ]; then
  cp ./frontend/.env.example ./frontend/.env
  echo "frontend/.env created"
else
  echo "frontend/.env.example not found"
fi

echo "🐳 Building and starting containers..."
docker compose up --build
