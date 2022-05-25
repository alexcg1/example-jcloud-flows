import sys
from jina import Client
from docarray import DocumentArray, Document


# Connect to client
HOST = str(sys.argv[1])  # take from CLI argument
client = Client(host=HOST)

# Generate docs to index
docs = DocumentArray.from_files("./data/**/*.jpg")

# Create a pre-processing function to process our image for the Flow
def process(doc: Document):
    doc.load_uri_to_image_tensor().set_image_tensor_shape(
        (64, 64)
    ).set_image_tensor_normalization()


for doc in docs:
    process(doc)

# Index our docs
client.index(docs)

# Use our first Document as our query image
query = docs[0]

# Query our index and get results
response = client.search(query)

# Print matches
print("Here are your matches:")
for match in response[0].matches:
    print(match.uri)
