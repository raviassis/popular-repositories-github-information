from dotenv import load_dotenv, find_dotenv
import os
import json
import pandas as pd
from repositories import Repository

load_dotenv(find_dotenv())

repository = Repository(1000, os.getenv("TOKEN"))
print("Get Repositories")
repositories = repository.get_repositories()
df = pd.json_normalize(repositories)
csvText = df.to_csv().replace("\r", "")
filename = "repositories.csv"
print(f"Write repositories on file {filename}")
file = open(filename, "w")
file.write(csvText)
file.close()
print("End script")