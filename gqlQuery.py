from gql import gql, Client, AIOHTTPTransport
from getOwnerRepo import getOwnerRepo

def gqlQuery(link, getStargazers = True, getForkers = True, getWatchers = True):

    # Variables for the query
    params = {"getStargazers": getStargazers,
          "getForkers": getForkers,
          "getWatchers": getWatchers
          }

    token = "Bearer 08c69c309a2d3699dcfa778ce11a871b4e3fbf97"

    transport = AIOHTTPTransport(url="https://api.github.com/graphql", headers={"Authorization": token})

    client = Client(transport=transport, fetch_schema_from_transport=True)

    owner, repo = getOwnerRepo(link)

    query = gql(

            """
            query getGraph( $getStargazers: Boolean!, $getForkers: Boolean!, $getWatchers: Boolean! ) {
                repository(owner: "%s" , name: "%s" ) {
                
                stargazerCount @include(if: $getStargazers)
                
                stargazers @include(if: $getStargazers) {
                
                ...getStargazersInfo
                
                }
                
                forkCount @include(if: $getForkers)
                
                forks @include(if: $getForkers)  {
                
                ...getForksInfo
                
                }
                
                
                watchers @include(if: $getWatchers) {
                
                totalCount
                
                ...getWatchersInfo
                
                }
                
            }
            }

            fragment getStargazersInfo on StargazerConnection {
            
            connectedTo: edges {
                user: node {
                    login
                    }
                }
            }

            fragment getForksInfo on RepositoryConnection {
            forkedTo: edges {
                repo: node {
                user: owner {
                    login
                }
                }
            }
            }

            fragment getWatchersInfo on UserConnection {
            watchedBy:edges {
                user: node {
                login
                }
            }
            }

            """ % (owner, repo))

    result = client.execute(query, variable_values=params)

    return result