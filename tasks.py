#Python
import sys
import requests
import json

def get_playing_data(key: str):
  API_KEY = key

  url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=en-US&page=1"
  the_url = url
  with open("url.json", "w") as json_file:
    json_url = {"last_url": the_url}
    json.dump(json_url, json_file, indent=2)

  request = requests.get(url)
  if request.status_code == 404:
      print("Couldn't find data")
      sys.exit()
  else:
      with open("movie-db.json", "w") as json_file:
          movie_data = request.json()
          if not movie_data:
              print("No data found")
              sys.exit()
          json.dump(movie_data, json_file, indent=2)
  

def get_popular_data(key: str):
  API_KEY = key

  url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1"
  the_url = url
  with open("url.json", "w") as json_file:
    json_url = {"last_url": the_url}
    json.dump(json_url, json_file, indent=2)

  request = requests.get(url)
  if request.status_code == 404:
      print("Couldn't find data")
      sys.exit()
  else:
      with open("movie-db.json", "w") as json_file:
          movie_data = request.json()
          if not movie_data:
              print("No data found")
              sys.exit()
          json.dump(movie_data, json_file, indent=2)
  

def get_top_data(key: str):
  API_KEY = key

  url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=en-US&page=1"
  the_url = url
  with open("url.json", "w") as json_file:
    json_url = {"last_url": the_url}
    json.dump(json_url, json_file, indent=2)

  request = requests.get(url)
  if request.status_code == 404:
      print("Couldn't find data")
      sys.exit()
  else:
      with open("movie-db.json", "w") as json_file:
          movie_data = request.json()
          if not movie_data:
              print("No data found")
              sys.exit()
          json.dump(movie_data, json_file, indent=2)
  
def get_upcoming_data(key: str):
  API_KEY = key

  url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}&language=en-US&page=1"
  the_url = url
  with open("url.json", "w") as json_file:
    json_url = {"last_url": the_url}
    json.dump(json_url, json_file, indent=2)

  request = requests.get(url)
  if request.status_code == 404:
      print("Couldn't find data")
      sys.exit()
  else:
      with open("movie-db.json", "w") as json_file:
          movie_data = request.json()
          if not movie_data:
              print("No data found")
              sys.exit()
          json.dump(movie_data, json_file, indent=2)

def play_data():
    with open("movie-db.json", "r") as json_file:
        json_data = json.load(json_file)
        results = json_data.get("results", [])
        for movie in results:
            movie_title = movie.get("title", "Unknown")
            release_date = movie.get("release_date", "Unknown")
            print(f"Playing Now: {movie_title}")
            print(f"Release Date: {release_date}")
            print()

def popular_data():
    with open("movie-db.json", "r") as json_file:
        json_data = json.load(json_file)
        results = json_data.get("results", [])
        for movie in results:
            movie_title = movie.get("title", "Unknown")
            release_date = movie.get("release_date", "Unknown")
            print(f"Popular movie: {movie_title}")
            print(f"Release Date: {release_date}")
            print()

def top_data():
    with open("movie-db.json", "r") as json_file:
        json_data = json.load(json_file)
        results = json_data.get("results", [])
        for movie in results:
            movie_title = movie.get("title", "Unknown")
            release_date = movie.get("release_date", "Unknown")
            print(f"Top movie: {movie_title}")
            print(f"Release Date: {release_date}")
            print()

def upcoming_data():
    with open("movie-db.json", "r") as json_file:
        json_data = json.load(json_file)
        results = json_data.get("results", [])
        for movie in results:
            movie_title = movie.get("title", "Unknown")
            release_date = movie.get("release_date", "Unknown")
            print(f"Coming Soon: {movie_title}")
            print(f"Release Date: {release_date}")
            print()