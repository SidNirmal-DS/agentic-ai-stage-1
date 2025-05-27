from agent_recommender import get_movie_recommendations

if __name__ == "__main__":
    mood = input("Enter your current mood or genre preference: ")
    result = get_movie_recommendations(mood)
    print("\nYour Movie Recommendations:\n")
    print(result)