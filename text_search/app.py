import sys
from jina import Client
from docarray import DocumentArray


# Connect to client
HOST = str(sys.argv[1])  # take from CLI argument
client = Client(host=HOST)

# Generate docs to index. We'll only index ~100 since this is just a demo
docs = DocumentArray.from_csv("data/data.csv", field_resolver={"answer": "text"})[0:100]

# Index our docs
client.index(docs)

# Use our first Document as our query image
query = docs[0]

# Query our index and get results
response = client.search(query)

# Print matches
print("Here are your matches:")
for match in response[0].matches:
    print(match.text)
