from langchain.agents import Tool
import requests

# Define each CRUD operation as a separate tool
def create_item(data):
    response = requests.post("http://localhost:5000/items", json=data)
    return response.json()

def read_item(item_id):
    response = requests.get(f"http://localhost:5000/items/{item_id}")
    return response.json()

def update_item(item_id, data):
    response = requests.put(f"http://localhost:5000/items/{item_id}", json=data)
    return response.json()

def delete_item(item_id):
    response = requests.delete(f"http://localhost:5000/items/{item_id}")
    return response.json()

# Register these functions as LangChain tools
create_tool = Tool(name="Create Item", func=create_item, description="Creates an item, by creating a valid json object from user input .")
read_tool = Tool(name="Read Item", func=read_item, description="Fetches an item.")
update_tool = Tool(name="Update Item", func=update_item, description="Updates an item.")
delete_tool = Tool(name="Delete Item", func=delete_item, description="Deletes an item.")
