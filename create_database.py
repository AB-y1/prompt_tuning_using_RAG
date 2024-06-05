from langchain.documnet_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import document 
from langchain.document import OpenAIEmbeddings
from langchain.vectorstores.chroma import chroma 
import os 
import shutil
from tqdm import tqdm


CHROMA_PATH = "/chroma"
DATA_PATH = "data/patterns"


def main():
    generate_data_store()


def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)


def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = []
    for document in tqdm(documents, desc="Splitting documents"):
        chunks.extend(text_splitter.split_documents([document]))    
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks


def save_to_chroma(chunks: list[Document]):
    # Check if the vector store already exists
    if os.path.exists(CHROMA_PATH):
        print(f"Vector store already exists at {CHROMA_PATH}. Skipping creation.")
        return
    else:
        os.makedirs(CHROMA_PATH, exist_ok=True)

        
        # Create a new DB from the documents.
        db = Chroma.from_documents(
            tqdm(chunks, desc="Embedding chunks"),
            OpenAIEmbeddings(),
            persist_directory=CHROMA_PATH
        )
        db.persist()
        print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")



if __name__ == "__main__":
    main()