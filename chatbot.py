import ollama
import requests
import json

# Load LLaMA model
def initialize_model():
    model = ollama.load("llama-3.2")
    return model


def interpret_request(model, user_input):
    # Send the user input to LLaMA and get the response
    response = ollama.query(model, user_input)

    # Analyze response for keywords indicating CRUD operations
    # Here, we assume the response is text, so let's search for keywords.
    if "create" in response.lower():
        return "create"
    elif "read" in response.lower() or "fetch" in response.lower():
        return "read"
    elif "update" in response.lower():
        return "update"
    elif "delete" in response.lower():
        return "delete"
    else:
        return "unknown"