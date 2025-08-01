import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os

load_dotenv()
PLACEHOLDER_URL='https://picsum.photos/200/300'


def load_dataset(FILE_PATH="master_dataset_final.csv"):
    """
    Load the dataset from a CSV file.
    
    Parameters:
    FILE_PATH (str): The path to the CSV file containing the dataset.
    
    Returns:
    pd.DataFrame: The loaded dataset as a pandas DataFrame.
    """
    try:
        df = pd.read_csv(FILE_PATH)
        return df
    except FileNotFoundError:
        print(f"Error: The file {FILE_PATH} was not found.")
        raise FileNotFoundError(f"Dataset file not found: {FILE_PATH}. Please check the file path.")
    except pd.errors.EmptyDataError:
            raise ValueError(f"The file {FILE_PATH} is empty or contains no valid data.")
    except Exception as e:
        raise RuntimeError(f"Failed to load dataset from {FILE_PATH}: {str(e)}")
    
def create_count_matrix(dataset):
    """Create count matrix"""
    count_vectorizer = CountVectorizer(stop_words='english')
    count_matrix = count_vectorizer.fit_transform(dataset['soup'])
    return count_matrix

def create_similarity_matrix(count_matrix):
    """Create similarity matrix"""
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    return cosine_sim

def get_recommendations(title, dataset, cosine_sim, top_n=8):
    """Get movie recommendations based on the title.
    
    Parameters:
    title (str): The title of the movie to find recommendations for.
    dataset (pd.DataFrame): The dataset containing movie information.
    cosine_sim (np.ndarray): The cosine similarity matrix.
    top_n (int): The number of recommendations to return.
    
    Returns:
    pd.DataFrame: A DataFrame containing the recommended movies.
    """
    if not isinstance(dataset, pd.DataFrame):
        raise ValueError("The dataset must be a pandas DataFrame.")
    
    if not isinstance(cosine_sim, np.ndarray):
        raise ValueError("The cosine similarity must be a numpy ndarray.")
    
    if title is None or not isinstance(title, str):
        raise ValueError("Title must be a non-empty string.")
    
    if top_n <= 0:
        raise ValueError("top_n must be a positive integer.")
    
    if 'title' not in dataset.columns:
        raise ValueError("The dataset must contain a 'title' column.")
    
    if 'release_date' not in dataset.columns:
        raise ValueError("The dataset must contain a 'release_date' column.")
    
    indices = pd.Series(dataset.index, index=dataset['title'].str.lower()).drop_duplicates()
    
    if title.lower() not in indices:
        print(f"Title '{title}' not found in the dataset.")
        return pd.DataFrame()
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n + 1]
    
    movie_indices = [i[0] for i in sim_scores]
    
    recommendations = dataset.iloc[movie_indices][['title', 'release_date']]
    recommendations['director'] = dataset.iloc[movie_indices]['main_director']
    recommendations['index'] = dataset.iloc[movie_indices]['movieId']
    recommendations = recommendations.reset_index(drop=True)
    
    return (recommendations.to_dict('records'))

async def get_recommended_movie_posters(session, movie):
    """Get the posters for the given movie asynchronously
    
    Parameters:
    movie : Movie object without poster
    
    Returns:
    movie : Movie object with poster
    """
    API_KEY = os.getenv("OMDB_API_KEY")
    if not API_KEY:
        print("OMDB API key not found.")
        movie['poster'] = PLACEHOLDER_URL    
        return movie

    URL = f'http://www.omdbapi.com/?t={movie["title"]}&apikey={API_KEY}'

    try:
        async with session.get(URL) as response:
            if response.status == 200:
                data = await response.json()
                if data.get('Response') == 'True' and 'Poster' in data and data['Poster'] != 'N/A':
                    movie['poster'] = data['Poster']
                else:
                    print(f"No poster found for movie: {movie['title']}")
                    movie['poster'] = PLACEHOLDER_URL
            else:
                print(f"Error fetching poster for movie: {movie['title']}. Status code: {response.status}")
                movie['poster'] = PLACEHOLDER_URL
    except Exception as e:
        print(f"An exception occurred while fetching poster for {movie['title']}: {e}")
        movie['poster'] = PLACEHOLDER_URL
        
    return movie

if __name__ == "__main__":
    # Example usage, get by directyly running this file. Recommendations for "The Dark Knight"
    try:
        dataset = load_dataset()
        count_matrix = create_count_matrix(dataset)
        cosine_sim = create_similarity_matrix(count_matrix)
        recommendations = get_recommendations("The Dark Knight", dataset, cosine_sim)
        print(recommendations)
    except Exception as e:
        print(f"An error occurred: {e}")
        raise