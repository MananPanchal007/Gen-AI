from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

# Load and split the PDF
pdf_path = Path(__file__).parent / "nodejs.pdf"
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_docs = text_splitter.split_documents(docs)

print("Number of documents:", len(docs))
print("Number of chunks:", len(split_docs))

# Initialize embeddings
embedder = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key="YOUR_API_KEY"
)

# Connect to the vector store
retriever = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embedder
)

# Get user query
user_query = input("> ")

# Define a few simple alternative queries
parallel_queries = [
    user_query,
    f"Explain {user_query}",
    f"Overview of {user_query}"
    f"Details about {user_query}",
    f"How does {user_query} work?",
]

# Collect results from all queries
all_relevant_chunks = []
for query in parallel_queries:
    results = retriever.similarity_search(query=query, k=4)
    all_relevant_chunks.extend(results)

# Remove duplicates by using page_content as key
unique_chunks = {chunk.page_content: chunk for chunk in all_relevant_chunks}
filtered_chunks = list(unique_chunks.values())

print(f"\nTotal unique relevant chunks: {len(filtered_chunks)}")

# Build system prompt
context_text = "\n\n".join([chunk.page_content for chunk in filtered_chunks])

system_prompt = f"""
You are an AI assistant who responds based on the available context.
Your task is to provide a concise and accurate answer to the user's question.
You should use the context provided to you as well as your own knowledge.

Rules:
    - Follow the JSON Format for Output.
    - Carefully analyse the user query.

Output JSON Format:
{{
    "answer": "string",
    "context": "string"
}}

Example:
User Query: {user_query}
Answer: <Your generated answer here>

Context:
{context_text}
"""