
from query_stargazers_from_repos import query_stargazers_from_repos
from load_links import load_links
from get_owner_repo import get_owner_repo

my_token = '08c69c309a2d3699dcfa778ce11a871b4e3fbf97'

data = load_links("repos.csv")

## There are 6000 links. So we do the first 500 first.
first_500 = data[0:499]

## This function writes the data into a folder.
query_stargazers_from_repos(first_500, my_token)

