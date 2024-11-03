from langchain.agents import initialize_agent
from langchain_ollama import ChatOllama

import tools
from vector_store import vector_store

# Load LLaMA model
llm = ChatOllama(
        temperature=0,
        model="llama3.2",
    )

# Define the agent with tools, LLaMA, and the vector store
agent = initialize_agent(
    tools=[tools.create_tool, tools.read_tool, tools.update_tool, tools.delete_tool],
    llm=llm,
    # retriever=vector_store.as_retriever(),
    verbose=True
)

def main():
    print("Welcome to the intelligent chatbot. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # Agent processes the input and provides a response
        response = agent({"input": user_input})
        print("Bot:", response["output"])

if __name__ == "__main__":
    main()