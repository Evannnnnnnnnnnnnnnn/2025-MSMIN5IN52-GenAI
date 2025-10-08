import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows the frontend to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    text: str

# Initialize OpenAI Chat Model
llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))

# Define a prompt template for the travel agent
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI travel agent. Your goal is to create a detailed travel plan based on the user's request."),
    ("user", "{query}")
])

# Create a simple chain
chain = prompt | llm

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/plan")
async def get_plan(query: Query):
    # Use the LangChain chain to get a response from the LLM
    response = await chain.ainvoke({"query": query.text})
    return {"plan": response.content}