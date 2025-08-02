#!/bin/bash

echo "Setting up environment files..."

# Copy .env.example to .env for backend only if .env doesn't exist
if [ -f ./backend/.env.example ] && [ ! -f ./backend/.env ]; then
  cp ./backend/.env.example ./backend/.env
  echo "backend/.env created"
elif [ -f ./backend/.env ]; then
  echo "backend/.env already exists, skipping..."
else
  echo "backend/.env.example not found"
fi

# Copy .env.example to .env for frontend only if .env doesn't exist
if [ -f ./frontend/.env.example ] && [ ! -f ./frontend/.env ]; then
  cp ./frontend/.env.example ./frontend/.env
  echo "frontend/.env created"
elif [ -f ./frontend/.env ]; then
  echo "frontend/.env already exists, skipping..."
else
  echo "frontend/.env.example not found"
fi

echo "🐳 Building and starting containers..."
docker compose up --build