import axios from 'axios';

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL

export const fetchRecommendedMovies = async (title: string) =>{
    const URL= `${BACKEND_URL}/recommendations/${title}`;

    try{
        const response = await axios.get(URL);
        return response.data;
    }catch(err){
        console.error(`Error fetching recommended movies for ${title}`, err)
        return [];
    }
}