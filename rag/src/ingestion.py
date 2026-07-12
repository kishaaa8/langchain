from pathlib import Path
import bs4

from langchain_community.document_loaders import (
    TextLoader,
    WebBaseLoader,
    PyPDFLoader,
)

# Project root (rag/)
BASE_DIR = Path(__file__).resolve().parent.parent

SPEECH_PATH = BASE_DIR / "speech.txt"
PDF_PATH = BASE_DIR / "attention_isalluneed.pdf"


def load_text():

    loader = TextLoader(str(SPEECH_PATH))

    return loader.load()


def load_pdf():

    loader = PyPDFLoader(str(PDF_PATH))

    return loader.load()


def load_web():

    loader = WebBaseLoader(
        web_paths=(
            "https://lilianweng.github.io/posts/2023-06-23-agent/",
        ),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("post-title", "post-content", "post-header")
            )
        ),
    )

    return loader.load()

if __name__ == "__main__":

    print("===== Testing Text Loader =====")
    text_docs = load_text()
    print(f"Loaded {len(text_docs)} document(s)")
    print(text_docs[0].page_content[:100])   # First 100 characters

    print("\n===== Testing PDF Loader =====")
    pdf_docs = load_pdf()
    print(f"Loaded {len(pdf_docs)} pages")

    print("\n===== Testing Web Loader =====")
    web_docs = load_web()
    print(f"Loaded {len(web_docs)} web document(s)")