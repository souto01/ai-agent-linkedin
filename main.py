from fastapi import FastAPI

app = FastAPI(
    title="AI Agent",
    description="Projeto de agente de IA para portfólio",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"status": "ok", "message": "AI Agent rodando 🚀"}
