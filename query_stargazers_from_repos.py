import csv
import datetime
import argparse
from get_owner_repo import get_owner_repo
from run_query import run_query



## Change to NAME OF OWNER AND REPO to scrape
#name_with_owner = "marmelab/react-admin"
#nwo_list = name_with_owner.split("/")
# owner = 'cypress-io'
# repo = 'cypress'
#owner = nwo_list[0]
#repo = nwo_list[1]

#fields = ["username", "name", "blog", "company", "bio", "location", "avatar_url",
#          "hireable", "num_followers", "num_following", "created_at", "star_time"]




def query_stargazers_from_repos(data, mytoken):

    ## Change to your GITHUB PERSONAL ACCESS TOKEN

    headers = {"Authorization": "token " + mytoken}

    ## Load in the list of links to the repos

    fields = ["username","name","numberOfReposStarred"]

    query = """
    query {{
    repository(owner:"{0}", name:"{1}") {{
        stargazers(first:100 {2}) {{
        pageInfo {{
            endCursor
            hasNextPage
            hasPreviousPage
            startCursor
        }}
        edges {{
            starredAt
            node {{
                login
                location
                starredRepositories {{
                    totalCount
                }}
            }}
        }}
    }}
    }}
    }}
    """
    count_repo = 0

    for repo_link in data:

        owner, repo = get_owner_repo(repo_link)

        # RUN THE QUERY
        #star_list = []
        endCursor = ""  # Start from begining
        count = 0  
        hasNextPage = True

        print(f"Running query for repository '{repo}':")
        file_name = f"data/stargazers_{repo}.csv"

        with open(file_name, 'w', encoding="utf-8") as stars:
            stars_writer = csv.writer(stars)
            stars_writer.writerow(fields)
        # by default, GQL only allows 100 elemenets per page, so need to use cursor to get all data
            while hasNextPage and count <= 15_000:   ## LIMIT stargazers 
                this_query = query.format(owner, repo, endCursor)
                result = run_query(this_query, headers)  # Execute the query
                # print(this_query)
                # print(result)
                hasNextPage = result['data']['repository']['stargazers']['pageInfo']['hasNextPage']
                endCursor = result['data']['repository']['stargazers']['pageInfo']['endCursor']
                endCursor = ', after: "' + endCursor + '"'
                data = result['data']['repository']['stargazers']['edges']

                for item in data:
                    username = item['node']['login']
                    #name = item['node']['name']
                    #num_followers = item['node']['followers']['totalCount']
                    #num_following = item['node']['following']['totalCount']
                    #hireable = item['node']['isHireable']
                    #company = item['node']['company']
                    #bio = item['node']['bio']
                    location = item['node']['location']
                    numberOfReposStarred = item['node']['starredRepositories']['totalCount']
                    #avatar_url = item['node']['avatarUrl']
                    #blog = item['node']['websiteUrl']

                    #created_at = item['node']['createdAt']
                    #created_at = datetime.datetime.strptime(
                    #    created_at, '%Y-%m-%dT%H:%M:%SZ')
                    #created_at = created_at + datetime.timedelta(hours=-5)  # EST
                    #created_at = created_at.strftime('%Y-%m-%d %H:%M:%S')

                    #star_time = datetime.datetime.strptime(
                    #    item['starredAt'], '%Y-%m-%dT%H:%M:%SZ')
                    #star_time = star_time + datetime.timedelta(hours=-5)  # EST
                    #star_time = star_time.strftime('%Y-%m-%d %H:%M:%S')
                    #star_list.append((username, star_time))
                    #stars_writer.writerow([username, name, blog, company, bio, location, avatar_url,
                    #                       hireable, num_followers, num_following, created_at, star_time])
                    stars_writer.writerow([username, location, numberOfReposStarred])


                count = count + 100
                print(str(count) + " users processed.")


        print("")        
        print("Repo: " + repo + " done.")
        print("")
        count_repo += 1
        print(str(count_repo) + " repos processed.")
        print("")
        print("")
