#!/usr/bin/env python3
import os
from args import args
import tasks
from tasks import API_KEY
import json

def main():

  the_key = API_KEY
  
  if not os.path.exists("url.json"):
    with open("url.json", "w") as json_file:
      set_data = {"last_url": "url_spot"}
      json.dump(set_data, json_file, indent=2)
      last_url = "none"
  else:
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
      tasks.get_playing_data()
      tasks.playing_data()
  elif args.type == "popular":
    if last_url == pop_url:
      tasks.popular_data()
    else:
      tasks.get_popular_data()
      tasks.popular_data()
  elif args.type == "top":
    if last_url == top_url:
      tasks.top_data()
    else:
      tasks.get_top_data()
      tasks.top_data()
  elif args.type == "upcoming":
    if last_url == upcoming_url:
      tasks.upcoming_data()
    else:
      tasks.get_upcoming_data()
      tasks.upcoming_data()
  else:
    print("Invalid Comamnd. Options: playing, popular, top, or upcoming")

if __name__ == '__main__':
  main()
