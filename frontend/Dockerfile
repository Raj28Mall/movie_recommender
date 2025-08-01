# frontend/Dockerfile
FROM node:22-alpine

WORKDIR /app

COPY package*.json ./
COPY tsconfig*.json ./
COPY vite.config.ts ./
COPY eslint.config.js ./
RUN npm install

COPY . .

RUN cp .env.example .env || true

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--host"]
