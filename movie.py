#!/usr/bin/env python3
from args import args
import tasks
import json

def main():
  #API key
  the_key = input("Enter your key: ")
  
  #Get last used url for comparison
  with open("url.json", "r") as json_file:
    url_data = json.load(json_file)
    last_url = url_data["last_url"]

  #url's for comparison
  play_url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={the_key}&language=en-US&page=1"
  pop_url = f"https://api.themoviedb.org/3/movie/popular?api_key={the_key}&language=en-US&page=1"
  top_url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={the_key}&language=en-US&page=1"
  upcoming_url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={the_key}&language=en-US&page=1"

  #If last url matches url run task, else, get/update data and run task
  if args.type == "playing":
    if last_url == play_url:
      tasks.playing_data()
    else:
      tasks.get_playing_data(the_key)
      tasks.playing_data()
  elif args.type == "popular":
    if last_url == pop_url:
      tasks.popular_data()
    else:
      tasks.get_popular_data(the_key)
      tasks.popular_data()
  elif args.type == "top":
    if last_url == top_url:
      tasks.top_data()
    else:
      tasks.get_top_data(the_key)
      tasks.top_data()
  elif args.type == "upcoming":
    if last_url == upcoming_url:
      tasks.upcoming_data()
    else:
      tasks.get_upcoming_data(the_key)
      tasks.upcoming_data()
  else:
    print("Invalid Comamnd. Options: playing, popular, top, or upcoming")

if __name__ == '__main__':
  main()
