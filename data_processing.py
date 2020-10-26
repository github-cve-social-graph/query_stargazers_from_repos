import pandas as pd
from get_owner_repo import get_owner_repo

def data_processing(data):

    df = pd.DataFrame(columns = ['Owner', 'Repo'])

    for link in data:

        try:

            owner, repo = get_owner_repo(link)
            temp = pd.Series([owner, repo], index = ['Owner','Repo'])
            df = df.append(temp, ignore_index=  True)

        except Exception:

            print("Link missing information or invalid format")
            print(link)

    # Drop the duplicate repos
    df = df.drop_duplicates()

    # Write the data frame to file
    df.to_csv("owner_repo.csv")

    return df