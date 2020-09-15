import requests

class Repository:
    def __init__(self, num_repositories, token):
        self.num_repositories = num_repositories
        self.token = token
    
    def __get_query(self, after):
        after = "null" if after == None else f'"{after}"'
        query = f"""
        {{
            search(
            query:"stars:>0", 
            type:REPOSITORY, 
            first:5,
            after:{after}
            ) {{
            pageInfo {{
                startCursor
                endCursor
                hasPreviousPage
                hasNextPage
            }}
            edges {{
                node {{
                ... on Repository {{
                    nameWithOwner
                    createdAt
                    pushedAt
                    primaryLanguage {{
                    name
                    }}
                    stargazers {{
                    totalCount
                    }}
                    totalIssues: issues(labels: null, states: null) {{
                    totalCount
                    }}
                    closedIssues: issues(labels:null,	states:[CLOSED]) {{
                    totalCount
                    }}
                    releases(
                    orderBy: {{
                        field: CREATED_AT, 
                        direction: ASC
                    }}
                    ) 
                    {{
                    totalCount
                    }}
                    pullRequests(
                    states:[MERGED],
                    labels: null
                    ) 
                    {{
                    totalCount
                    }}
                }}
                }}
            }}
            }}
        }}
        """
        return query

    def get_repositories(self):
        headers = headers = {'Authorization': f'Bearer {self.token}'}
        repositories = list()
        endCursor = None
        hasNextPage = True
        while hasNextPage and len(repositories) < self.num_repositories:
            query = self.__get_query(endCursor)
            result = requests.post("https://api.github.com/graphql", json={'query': query}, headers=headers)
            if result.status_code == 200:
                data = result.json()['data']['search']
                pageinfo = data['pageInfo']
                endCursor = pageinfo['endCursor']
                hasNextPage = pageinfo['hasNextPage']
                repositories.extend(list(map(lambda x: x['node'], data['edges'])))
                print(f"\rRetrieve {len(repositories)} repositories", end = '')
        return repositories
