from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.tavily import TavilyTools
import google.generativeai as genai
import os
from utils import API_KEY,TAVIL_API_KEY
from constants import PROMPT, INSTRUCTIONS
os.environ["GOOGLE_API_KEY"] = API_KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Set up the agent with a model and tools
agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    tools=[TavilyTools(api_key=TAVIL_API_KEY)],
    markdown=True,
    system_prompt=PROMPT,
    instructions=INSTRUCTIONS
)

# Analyze the image
try:
    # Ensure the image path is correct
    image_path = "./images/test_case_1.jpg"
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at path: {image_path}")

    # Provide the image to the agent for analysis
    agent.print_response(
        "Analyze the Image",
        images=[image_path],
        stream=True
    )
except Exception as e:
    print(f"Error: {e}")
