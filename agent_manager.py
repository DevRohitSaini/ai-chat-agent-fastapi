from chatAgent import ChatAgent

class AgentManager:
    def __init__(self):
        self.agents = {}

    def get_agent(self, name: str) -> ChatAgent:
        if name not in self.agents:
            self.agents[name] = ChatAgent(name)
        return self.agents[name]