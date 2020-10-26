# Accept a list of strings, split them and find the username and the repo and
# put them back into a list

def get_owner_repo(link):

    newList = []

    link = link.split("/", 5)

    if len(link) < 5 or link[2] != "github.com":
        raise Exception


    owner = link[3]
    repo = link[4]

    return owner, repo
