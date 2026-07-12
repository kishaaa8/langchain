"""
vector_store.py

This module is responsible for:

1. Creating embeddings
2. Creating Chroma DB
3. Creating FAISS DB
4. Running similarity search
"""

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma, FAISS


def get_embeddings():
    """
    Creates an OpenAI embedding model.
    """
    return OpenAIEmbeddings()


def create_chroma(documents, embeddings):
    """
    Creates a Chroma Vector Database.
    """

    return Chroma.from_documents(
        documents,
        embeddings,
    )

# def create_faiss(documents, embeddings):
#     """
#     Creates a FAISS Vector Database.
#     """

#     return FAISS.from_documents(
#         documents,
#         embeddings,
#     )


def similarity_search(db, query):
    """
    Performs similarity search on the vector database.
    """

    return db.similarity_search(query)