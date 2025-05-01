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
    api_key = "YOUR_OPENAI_API_KEY"
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

relevant_chunks = retriver.similarity_search(
    query="What is nodejs?"
)

print("Relevant chunks:" ,relevant_chunks)

system_prompt = f"""
You are an AI assistant who responds based on the available context.
You are not allowed to answer any query that is not related to the context.

Context:
{relevant_chunks}
"""