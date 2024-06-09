import tiktoken

file_path = "/home/abdoo/Desktop/prompt_tuning/output/all_documents.md"

def count_tokens_in_file(file_path):
    """
    Calculates the number of tokens in a file using the tiktoken library.
    
    Args:
        file_path (str): The path to the file.
        
    Returns:
        int: The number of tokens in the file.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Useing the 'cl100k_base' encoding name to count the tokens for embedding model
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    
    return len(tokens)

num_tokens = count_tokens_in_file(file_path)
print(f"The file contains {num_tokens} tokens.")
