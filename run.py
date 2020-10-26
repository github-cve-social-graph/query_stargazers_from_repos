
from query_stargazers_from_repos import query_stargazers_from_repos
from load_links import load_links
from getOwnerRepo import getOwnerRepo

my_token = '08c69c309a2d3699dcfa778ce11a871b4e3fbf97'

data = load_links("repos.csv")

## There are 6000 links. So we do the first 500 first.

first_two = data[0:2]

## This function writes the data into a folder.
queryStargazersFromRepos(first_two, my_token)

