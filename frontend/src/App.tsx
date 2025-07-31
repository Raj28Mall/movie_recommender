"use client"

import { useState } from "react"
import { Search, Calendar, User, TrendingUp, Loader2 } from "lucide-react"
import { Input } from "@/components/ui/input"
import { Card, CardContent } from "@/components/ui/card"
import { fetchRecommendedMovies } from "./lib/api"
import type { Movie } from "@/lib/types"

const initialMovies = [
	{
		id: 1,
		title: "The Shawshank Redemption",
		director: "Frank Darabont",
		release_date: "1994-09-23",
		poster: "https://picsum.photos/200/300",
	},
	{
		id: 2,
		title: "The Godfather",
		director: "Francis Ford Coppola",
		release_date: "1972-03-24",
		poster: "https://picsum.photos/200/300",
	},
	{
		id: 3,
		title: "The Dark Knight",
		director: "Christopher Nolan",
		release_date: "2008-07-18",
		poster: "https://picsum.photos/200/300",
	},
	{
		id: 4,
		title: "Pulp Fiction",
		director: "Quentin Tarantino",
		release_date: "1994-10-14",
		poster: "https://picsum.photos/200/300",
	},
	{
		id: 5,
		title: "Forrest Gump",
		director: "Robert Zemeckis",
		release_date: "1994-07-06",
		poster: "https://picsum.photos/200/300",
	},
	{
		id: 6,
		title: "Inception",
		director: "Christopher Nolan",
		release_date: "2010-07-16",
		poster: "https://picsum.photos/200/300",
	},
	{
		id: 7,
		title: "The Matrix",
		director: "The Wachowskis",
		release_date: "1999-03-31",
		poster: "https://picsum.photos/200/300",
	},
	{
		id: 8,
		title: "Goodfellas",
		director: "Martin Scorsese",
		release_date: "1990-09-19",
		poster: "https://picsum.photos/200/300",
	},
]

export default function MovieRecommendationSystem() {
	const [loading, setLoading] = useState(false)
	const [moviesToDisplay, setMoviesToDisplay] = useState<Movie[]>(initialMovies)
	const [searchQuery, setSearchQuery] = useState("")
	const [hasSearched, setHasSearched] = useState(false)

	const getRecommendedMovies = async (title: string) => {
		try {
			const response = await fetchRecommendedMovies(title)
      console.log(response);
      
		} catch (error) {
			console.error("Error fetching recommended movies:", error)
		} finally {
			setLoading(false)
		}
	}

	const handleSearch = (e: React.KeyboardEvent<HTMLInputElement>) => {
		if (e.key == "Enter" && searchQuery.trim() !== "") {
			setHasSearched(true)
			setLoading(true)
			const movie_name = searchQuery.toLowerCase().trim()
			getRecommendedMovies(movie_name)
		}
	}

	const formatDate = (dateString: string) => {
		const date = new Date(dateString)
		return date.getFullYear().toString()
	}

	return (
		<div className="px-8 min-h-screen bg-gradient-to-br from-slate-50 to-slate-100">
			<div className="container mx-auto px-4 py-8">
				<div className="text-center mb-12">
					<h1 className="text-4xl md:text-5xl font-bold text-slate-800 mb-4">
						Movie Recommendations
					</h1>
					<p className="text-lg text-slate-600 mb-8">
						{hasSearched
							? "Find your perfect movie match"
							: "Discover your next favorite movie"}
					</p>

					<div className="relative max-w-2xl mx-auto">
						<Search className="absolute left-4 top-1/2 transform -translate-y-1/2 text-slate-400 h-5 w-5" />
						<Input
							type="text"
							placeholder="Search for movies, directors, or genres..."
							value={searchQuery}
							onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
								setSearchQuery(e.target.value)
							}
							onKeyDown={(e) => handleSearch(e)}
							className="pl-12 pr-4 py-6 text-lg rounded-full border-2 border-slate-200 focus:border-blue-500 shadow-lg"
						/>
					</div>
				</div>

				<div className="mb-8">
					{!hasSearched ? (
						<div className="text-center">
							<div className="flex items-center justify-center gap-2 mb-2">
								<TrendingUp className="h-6 w-6 text-orange-500" />
								<h2 className="text-2xl font-bold text-slate-800">
									Popular Movies
								</h2>
							</div>
							<p className="text-slate-600">
								Here are some of the most beloved movies of all time
							</p>
						</div>
					) : (
						<div className="text-center">
							<h2 className="text-2xl font-bold text-slate-800 mb-2">
								Top Recommended Movies
							</h2>
						</div>
					)}
				</div>

				<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
					{moviesToDisplay.map((movie) => (
						<Card
							key={movie.id}
							className="pt-0 pb-3 group hover:shadow-xl transition-all duration-300 hover:-translate-y-2 bg-white border-0 shadow-lg overflow-hidden"
						>
							<div className="relative overflow-hidden">
								<img
									src={movie.poster || "/placeholder.svg"}
									alt={`${movie.title} poster`}
									className="w-full h-80 object-cover group-hover:scale-105 transition-transform duration-300"
								/>
							</div>

							<CardContent className="p-4">
								<h3 className="font-bold text-lg text-slate-800 mb-2 line-clamp-2 group-hover:text-blue-600 transition-colors">
									{movie.title}
								</h3>

								<div className="space-y-2">
									<div className="flex items-center text-slate-600 text-sm">
										<User className="h-4 w-4 mr-2 flex-shrink-0" />
										<span className="truncate">{movie.director}</span>
									</div>

									<div className="flex items-center text-slate-600 text-sm">
										<Calendar className="h-4 w-4 mr-2 flex-shrink-0" />
										<span>{formatDate(movie.release_date)}</span>
									</div>
								</div>
							</CardContent>
						</Card>
					))}
				</div>

				{hasSearched && !loading && moviesToDisplay.length === 0 && (
					<div className="text-center py-12">
						<div className="text-6xl mb-4">🎬</div>
						<h3 className="text-xl font-semibold text-slate-700 mb-2">
							No movies found
						</h3>
						<p className="text-slate-500">
							Try searching with different keywords
						</p>
					</div>
				)}
			</div>
		</div>
	)
}
