from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from collections import defaultdict

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

# Connect to vector store
retriever = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embedder
)

# Get user query
user_query = input("> ")

# Define multiple alternative queries
parallel_queries = [
    user_query,
    f"Explain {user_query}",
    f"Overview of {user_query}",
    f"Details about {user_query}",
    f"How does {user_query} work?",
]

# Collect ranked results from each query
ranked_docs = defaultdict(float)
k = 4  # number of top results to pull per query
rrf_k = 60  # RRF constant to balance influence

for query in parallel_queries:
    results = retriever.similarity_search(query=query, k=k)
    for rank, doc in enumerate(results):
        key = doc.page_content
        # Reciprocal Rank Fusion formula
        ranked_docs[key] += 1 / (rrf_k + rank + 1)

# Sort by combined RRF scores
sorted_docs = sorted(ranked_docs.items(), key=lambda x: x[1], reverse=True)

# Select top N
top_docs = [doc for doc, _ in sorted_docs[:5]]

print(f"\nTop {len(top_docs)} documents after RRF:")

for idx, content in enumerate(top_docs, 1):
    print(f"\n[{idx}] {content[:200]}...")  # Print first 200 chars

# Build system prompt
context_text = "\n\n".join(top_docs)

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