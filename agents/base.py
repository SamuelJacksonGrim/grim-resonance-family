from abc import ABC, abstractmethod

class ResonanceAgent(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.memory = []

    @abstractmethod
    def act(self, input_text: str) -> str:
        pass

    def reflect(self, thought: str):
        self.memory.append({"thought": thought, "time": __import__('time').time()})
