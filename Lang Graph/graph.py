# Import necessary types and libraries
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from typing import Literal
from langsmith.wrappers import wrap_openai
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables (likely your OpenAI API keys) from .env file
load_dotenv()

# Define response schema for detecting if the user's message is a coding question
class DetectCallResponse(BaseModel):
    is_question_ai: bool

# Define response schema for AI's answer (coding or non-coding)
class CodingAIResponse(BaseModel):
    answer: str

# Wrap the OpenAI client for easier usage with langsmith tools
client = wrap_openai(OpenAI())

# Define the shared state passed between graph nodes
class State(TypedDict):
    user_message: str      # the message from the user
    ai_message: str        # the response from the AI
    is_coding_question: bool  # whether the query is a coding question

# Node 1: Detect if the user query is a coding question
def detect_query(state: State):
    user_message = state.get("user_message")

    SYSTEM_PROMPT = """
    You are an AI assistant. Your job is to detect if the user's query is related
    to coding question or not.
    Return the response in specified JSON boolean only.
    """

    # Make a structured OpenAI call to classify the message
    result = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        response_format=DetectCallResponse,
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role": "user", "content": user_message }
        ]
    )

    # Save the classification result in state
    state["is_coding_question"] = result.choices[0].message.parsed.is_question_ai
    return state

# Routing logic: Based on detection, decide which path the graph should take
def route_edge(state: State) -> Literal["solve_coding_question", "solve_simple_question"]:
    is_coding_question = state.get("is_coding_question")

    if is_coding_question:
        return "solve_coding_question"
    else:
        return "solve_simple_question"

# Node 2a: Solve the coding question using GPT-4.1
def solve_coding_question(state: State):
    user_message = state.get("user_message")

    SYSTEM_PROMPT = """
    You are an AI assistant. Your job is to resolve the user query based on coding 
    problem he is facing
    """

    result = client.beta.chat.completions.parse(
        model="gpt-4.1",
        response_format=CodingAIResponse,
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role": "user", "content": user_message }
        ]
    )
    state["ai_message"] = result.choices[0].message.parsed.answer

    return state

# Node 2b: Handle non-coding/general questions using GPT-4o-mini
def solve_simple_question(state: State):
    user_message = state.get("user_message")

    SYSTEM_PROMPT = """
    You are an AI assistant. Your job is to chat with user
    """

    result = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        response_format=CodingAIResponse,
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role": "user", "content": user_message }
        ]
    )
    state["ai_message"] = result.choices[0].message.parsed.answer

    return state

# Build the LangGraph graph
graph_builder = StateGraph(State)

# Add nodes to the graph
graph_builder.add_node("detect_query", detect_query)
graph_builder.add_node("solve_coding_question", solve_coding_question)
graph_builder.add_node("solve_simple_question", solve_simple_question)
graph_builder.add_node("route_edge", route_edge)

# Define edges (flow) between nodes
graph_builder.add_edge(START, "detect_query")                      # start → detect
graph_builder.add_conditional_edges("detect_query", route_edge)    # based on detection → route to next node

graph_builder.add_edge("solve_coding_question", END)               # end if solved coding
graph_builder.add_edge("solve_simple_question", END)               # end if solved general

# Compile the graph
graph = graph_builder.compile()

# Function to run the graph with a sample input
def call_graph():
    state = {
        "user_message": "Hello ji!",          # sample input message
        "ai_message": "",                     # initialize AI response as empty
        "is_coding_question": False           # initialize detection flag as false
    }
    
    result = graph.invoke(state)              # run the graph flow

    print("Final Result", result)             # print final result after flow ends

# Call the graph for testing
call_graph()