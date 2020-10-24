from gqlQuery import gqlQuery
from loadLinks import loadLinks

data = loadLinks("repos.csv")

repo_link = data[0]

print("")
print("The repo link is:")
print(repo_link)
print("")
print("The data:")
print("")

result = gqlQuery(repo_link, getStargazers = True, getWatchers = False, getForkers = False)

print(result)
