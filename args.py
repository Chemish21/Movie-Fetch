#Python
import argparse

#Setting top level parsers
parser = argparse.ArgumentParser()

#Setting type argument
parser.add_argument("--type", type=str, required=True, choices=["playing", "popular", "top", "upcoming"],help="Sets type of movie")

#Finalizing parser
args = parser.parse_args()
