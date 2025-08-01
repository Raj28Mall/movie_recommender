# Movie Recommender

A movie recommendation system that uses content-based filtering to suggest movies based on user preferences. The application analyzes movie features like genres, directors, and other metadata to provide personalized recommendations.

## Features

### 🎬 Movie Recommendations
- **Content-Based Filtering**: Uses cosine similarity to find movies with similar characteristics
- **Intelligent Search**: Search for any movie in the dataset to get personalized recommendations
- **Real-time Results**: Get top curated movie recommendations instantly

## Technology Stack

### Backend
- **Python 3.12**: Core backend language
- **Flask**: Lightweight web framework with CORS support
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms for recommendation engine
- **Asyncio & Aiohttp**: Asynchronous API calls for poster fetching
- **OMDB API**: Movie poster and metadata retrieval

### Frontend
- **React 19**: Modern frontend framework with hooks
- **TypeScript**: Type-safe JavaScript development
- **Vite**: Fast build tool and development server
- **Tailwind CSS**: Utility-first CSS framework
- **Lucide React**: Beautiful SVG icons
- **Axios**: HTTP client for API communication

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



