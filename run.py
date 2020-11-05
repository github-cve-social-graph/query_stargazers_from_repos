
from query_stargazers_from_repos import query_stargazers_from_repos
from load_links import load_links
from get_owner_repo import get_owner_repo
from data_processing import data_processing
import pandas as pd

my_token = '2a6fa0f02190cc5f0d6d59f9791226061c88e156'

#data = load_links("repos.csv")

# After processing the gists links, deuplicate repos and invalid links are drooped.

#df = data_processing(data)

#df.to_csv("owner_repo.csv")

df = pd.read_csv("owner_repo.csv")

## There are 6000 links. So we do the first 500 first.
first_500 = df.iloc[0:499]

#for index in first_500.index:
        
#    owner = first_500.loc[index, "Owner"] 
#    repo = first_500.loc[index, "Repo"]

#    print(owner,repo)

#for index in first_500.index:
#    print(index)



## This function writes the data into a folder.
query_stargazers_from_repos(first_500, my_token)

