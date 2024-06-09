import os
from langchain.schema import Document
from typing import List
from langchain_community.document_loaders import DirectoryLoader

DATA_PATH = "target"

def main():
    documents = load_documents()
    save_documents(documents)

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    save_documents(documents)
    return documents

def save_documents(documents: List[Document], output_dir="output", output_file="all_documents.md"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, output_file)

    with open(output_path, "w", encoding="utf-8") as file:
        for document in documents:
            file.write(document.page_content)
            file.write("\n\n")

    print(f"Saved a total of {len(documents)} documents to the '{output_path}' file.")


if __name__ == "__main__":
    main()
