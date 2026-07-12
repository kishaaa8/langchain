"""
text_splitter.py

This module is responsible for splitting large documents
into smaller chunks.

Why?

LLMs have a context window (they can't read infinitely long text),
so we split documents into manageable pieces.

We also keep a small overlap so that context isn't lost
between consecutive chunks.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    """
    Splits documents into overlapping chunks.

    Parameters:
        documents (list): List of LangChain Documents.
        chunk_size (int): Maximum size of each chunk.
        chunk_overlap (int): Overlap between chunks.

    Returns:
        list: List of split document chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    return splitter.split_documents(documents)


# ==========================================================
# TESTING
# ==========================================================

if __name__ == "__main__":

    from ingestion import load_pdf

    print("Loading PDF...")

    docs = load_pdf()

    print(f"Pages loaded: {len(docs)}")

    print("\nSplitting documents...")

    chunks = split_documents(docs)

    print(f"Total Chunks: {len(chunks)}")

    print("\nFirst Chunk:\n")
    print(chunks[0].page_content[:500])
    
    print("\nsecond Chunk:\n")
    print(chunks[1].page_content[:500])
    
    print("\nthird Chunk:\n")
    print(chunks[2].page_content[:500])