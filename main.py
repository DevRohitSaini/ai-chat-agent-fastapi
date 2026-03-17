from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from agent_manager import AgentManager

app = FastAPI()

# Create an instance of AgentManager to manage our agents
manager = AgentManager()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

class ChatRequest(BaseModel):
    name: str
    message: str

def get_manager():
    return manager

@app.post("/chat")
async def chat(chat: ChatRequest, manager: AgentManager = Depends(get_manager)):    
    agent = manager.get_agent(chat.name)
    response = await agent.respond(chat.message)
    return {"response": response, "memory": agent.get_memory()}

@app.get("/history/{name}")
async def get_memory(name: str,manager: AgentManager = Depends(get_manager)):    
    agent = manager.get_agent(name)
    return {"memory": agent.get_memory()}