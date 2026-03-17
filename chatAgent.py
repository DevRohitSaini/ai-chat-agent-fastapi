class ChatAgent:
    def __init__(self,name):
        self.name = name
        self._memory = []

    async def respond(self,message):
        response = f"Hello {self.name}, your message is : {message}"
        savedData = {"name":self.name, "message":message}
        self._memory.append(savedData)
        return response
    
    def get_memory(self):
        return self._memory.copy() # Return a copy of the memory to prevent external modification