import flask, flask_cors
import aiohttp
import asyncio
from recommendations import load_dataset, create_count_matrix, create_similarity_matrix, get_recommendations, get_recommended_movie_posters

app = flask.Flask(__name__)
flask_cors.CORS(app)

master_dataset = None

@app.route('/')
def test():
    return 'Hello World!'

@app.route('/recommendations/<title>', methods=['GET'])
async def recommendations(title):
    recommended_movies = get_recommendations(title, master_dataset, cosine_sim)
    if recommended_movies is None:
        return flask.jsonify({"error": "Movie not found or dataset not loaded"}), 404

    # for movie in recommended_movies:
    #     movie['director'] = master_dataset['main_director'].iloc[movie['index']]
    #     movie['release_date'] = str(master_dataset['release_date'].iloc[movie['index']])

    async with aiohttp.ClientSession() as session:
        tasks = [get_recommended_movie_posters(session, movie) for movie in recommended_movies]
        
        movies_with_posters = await asyncio.gather(*tasks)

    return flask.jsonify(movies_with_posters), 200

if __name__ == '__main__':
    master_dataset = load_dataset()
    if master_dataset.empty:
        print("Dataset was unable to load. Server will not start")
        exit()
    count_matrix = create_count_matrix(master_dataset)
    if count_matrix is None:
        print("Count matrix was unable to load. Server will not start")
        exit()
    cosine_sim = create_similarity_matrix(count_matrix)
    if cosine_sim is None:
        print("Cosine similarity was unable to be computed. Server will not start")
        exit()
    print("Dataset loaded successfully")
    print("Count matrix computed successfully")
    print("Cosine similarity computed successfully")
    app.run(debug=True, port=5000)