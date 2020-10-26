# Accept a list of strings, split them and find the username and the repo and
# put them back into a list

def get_owner_repo(link):

    newList = []

    link = link.split("/", 5)
    owner = link[3]
    repo = link[4]

    return owner, repo
        