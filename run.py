
from query_stargazers_from_repos import query_stargazers_from_repos
from load_links import load_links
from get_owner_repo import get_owner_repo
from data_processing import data_processing
import pandas as pd

my_token = 'b05f22c728d8550e38326cc67bfaab55ecd04fcc'

#data = load_links("repos.csv")

# After processing the gists links, deuplicate repos and invalid links are drooped.

#df = data_processing(data)

df = pd.read_csv("owner_repo.csv")

## There are 6000 links. So we do the first 500 first.
first_500 = df.iloc[0:499]

#print(first_500.iloc[1])

#for index in range(len(df)):
        
#    owner, repo = df.loc[index, "Owner"], df.loc[index, "Repo"]

#    print(owner,repo)



## This function writes the data into a folder.
query_stargazers_from_repos(first_500, my_token)

