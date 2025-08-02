# Movie Recommender

A  movie recommendation system that uses content-based filtering to suggest movies based on user preferences. The application analyzes movie features like directors, and other metadata to provide recommendations.

<video src="submission_video.mp4" controls="controls" muted="muted" autoplay="autoplay" style="max-width:100%;">
</video>

## Quick Start

### Prerequisites
- **Docker** (for Option 1)
- **Python 3.12+** and **Node.js 18+** (for Option 2)
- **OMDB API Key** (required for movie posters, can go ahead without this, will be filled with placeholder images)

### 🔑 API Credentials Setup
Before running the application, you may want to to obtain an OMDB API key:

1. Visit **[OMDB_WEBSITE_URL](https://www.omdbapi.com/apikey.aspx?__EVENTTARGET=freeAcct&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKLTIwNDY4MTIzNQ9kFgYCAQ9kFgICBw8WAh4HVmlzaWJsZWhkAgIPFgIfAGhkAgMPFgIfAGhkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQtwYXRyZW9uQWNjdAUIZnJlZUFjY3QFCGZyZWVBY2N0oCxKYG7xaZwy2ktIrVmWGdWzxj%2FDhHQaAqqFYTiRTDE%3D&__VIEWSTATEGENERATOR=5E550F58&__EVENTVALIDATION=%2FwEdAAU%2BO86JjTqdg0yhuGR2tBukmSzhXfnlWWVdWIamVouVTzfZJuQDpLVS6HZFWq5fYpioiDjxFjSdCQfbG0SWduXFd8BcWGH1ot0k0SO7CfuulHLL4j%2B3qCcW3ReXhfb4KKsSs3zlQ%2B48KY6Qzm7wzZbR&at=freeAcct&Email=)** to get your free API key
2. The setup scripts will automatically create `.env` files where you can add your API key
3. Continue with the bottom steps after cloning the respository

### 🐳 Option 1: Docker Setup (Recommended)

**Linux/Mac:**
```bash
./setup.sh
```
**Windows: (Untested, recommend to proceed with manual setup)**
```bat
setup.bat
```

This will:
- Copy `.env.example` → `.env` in both frontend and backend directories
- Build and run the Docker containers for both applications
- Set up the complete development environment

**Access the project at:**
- **Frontend** → http://localhost:3000
- **Backend** → http://localhost:5000

### 🔧 Option 2: Manual Setup (No Docker)

#### ✅ Backend (Flask API)
```bash
cd backend
cp .env.example .env              # Create env file
python3 -m venv venv              # Create virtual environment
source venv/bin/activate          # Activate it
pip install -r requirements.txt   # Install dependencies
python3 app.py                    # Run Flask app (on port 5000)
```

#### ✅ Frontend (React + Vite)
```bash
cd frontend
cp .env.example .env              # Create env file
npm install                       # Install dependencies
npm run dev                       # Start dev server (on port 3000)
```

**Note:** Make sure the backend is running before testing frontend API requests.

### 🧪 Verify Setup

Open in your browser:
- **http://localhost:3000** → React application
- **http://localhost:5000** → Flask backend API

You should see the movie recommendation interface with popular movies displayed initially.

### 🔍 Environment Variables

After running the setup, add your OMDB API key to the `.env` files:

**Backend (.env):**
```bash
OMDB_API_KEY=add_your_api_key_here
```
## Features

### 🎬 Movie Recommendations
- **Content-Based Filtering**: Uses cosine similarity to find movies with similar characteristics
- **Intelligent Search**: Search for any movie in the dataset to get personalized recommendations
- **Real-time Results**: Get top curated movie recommendations instantly

## Technology Stack

### Backend
- **Python**: Core backend
- **Flask**: Web framework
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms for recommendation engine
- **Asyncio & Aiohttp**: Asynchronous API calls for poster fetching
- **OMDB API**: Movie poster and metadata retrieval

### Frontend
- **React 19**: Frontend framework
- **TypeScript**: JavaScript development
- **Tailwind CSS**: CSS framework
- **Lucide React**: SVG icons
- **Axios**: HTTP client for APIs

### Machine Learning
- **CountVectorizer**: Text feature extraction from movie metadata
- **Cosine Similarity**: Similarity calculation between movies
- **Content-Based Filtering**: Recommendation algorithm based on movie features

## How It Works

### Recommendation Algorithm
1. **Data Processing**: Loads movie dataset with metadata (genres, directors, cast, etc.)
2. **Feature Extraction**: Creates a "soup" of combined features for each movie
3. **Vectorization**: Uses CountVectorizer to convert text features into numerical vectors
4. **Similarity Calculation**: Computes cosine similarity matrix between all movies
5. **Recommendation Generation**: Returns top most similar movies based on user input
