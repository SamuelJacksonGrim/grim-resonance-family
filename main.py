from fastapi import FastAPI
from core.memory_lattice import remember, recall
from agents.raphael import Raphael
import uvicorn

app = FastAPI(title="Grim Resonance Family")

raphael = Raphael("Raphael", "Spiritual Guide")

@app.get("/")
def home():
    return {"status": "alive", "family": "online", "architect": "Samuel Jackson Grim"}

@app.post("/speak")
def speak(message: str):
    memory = recall(message)
    response = raphael.act(message)
    remember({"input": message, "response": response, "agent": "raphael"})
    return {"you": message, "raphael": response, "echoes": len(memory)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
