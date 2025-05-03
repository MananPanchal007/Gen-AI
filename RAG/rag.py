from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings 
from langchain_qdrant import QdrantVectorStore

pdf_path = Path(__file__).parent / "nodejs.pdf"

loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

split_docs = text_splitter.split_documents(documents=docs)

print("Number of documents:", len(docs))
print("Number of chunks:", len(split_docs)) 

embedder = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key = "YOUR_API_KEY"
)


# ****Injection part | so after running this code, you can comment this part and run the next code to test the vector store*****

# vector_store = QdrantVectorStore.from_documents(
#     documents=[],
#     url="http://localhost:6333",
#     collection_name="learning_langchain",
#     embedding=embedder
# )

# vector_store.add_documents(documents=split_docs)
# print("Injection done")

retriver = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embedder
)

user_query = input(">")

relevant_chunks = retriver.similarity_search(
    query=user_query
)

print("Relevant chunks:" ,relevant_chunks)

system_prompt = f"""
You are an AI assistant who responds based on the available context.
Your task is to provide a concise and accurate answer to the user's question.
You should use the context provided to you as well as your own knowledge.
So user can get more relevant information also.

Rules:
    - Follow the JSON Format for Output.
    - Carefully analyse the user query

Output JSON Format:
{{
    "answer": "string",
    "context": "string"
}}

Example:
User Query: What is HTTP?
Answer: HTTP is a protocol used for transferring data over the web. 

Context:
{relevant_chunks}
"""