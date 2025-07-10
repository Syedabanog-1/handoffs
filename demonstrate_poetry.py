import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel, AsyncOpenAI
from agents.extensions.models.litellm_model import LitellmModel
set_tracing_disabled(disabled=True)
load_dotenv()
provider = AsyncOpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)
model = OpenAIChatCompletionsModel(
    openai_client=provider,
    model="gemini-2.0-flash",
)

default_poem = """
From dawn till dusk, I've felt your love so true,
My heart beats with joy, my soul feels anew.
You've found the courage to come to me,
My heart overflows with love, wild and carefree.
"""

# ✅ Poet Agent
poet_agent = Agent(
    name="poet_agent",
    instructions=(
        "Take poetry stanza from the user as input, or use the default poem if none is provided.\n\n"
        f"Default poem:\n{default_poem}"
    ),
    model=model,
)

# ✅ Lyric Agent
lyrics_agent = Agent(
    name="lyrics_agent",
    instructions=(
        "You are a lyric poetry expert. Identify and analyze personal and emotional themes in the poem. "
        "Describe the poem's emotional tone and expressive elements."
    ),
    model=model,
)

# ✅ Narrative Agent
narrative_agent = Agent(
    name="narrative_agent",
    instructions=(
        "You are a narrative poetry expert. Identify storytelling features in the poem, like plot, sequence, and characters. "
        "Explain the narrative arc and message."
    ),
    model=model,
)

# ✅ Dramatic Agent
dramatic_agent = Agent(
    name="dramatic_agent",
    instructions=(
        "You are a dramatic poetry expert. Look for performance aspects in the poem like dialogue, monologue, or character speech. "
        "Describe how it's meant to be acted and its dramatic structure."
    ),
    model=model,
)

# ✅ Triage Agent — SINGLE HandOff with all analysis agents
triage_agent = Agent(
    name="triage_agent",
    instructions=(
        "You are a smart poetry classifier. Based on the content of the poem, determine if it's lyric, narrative, or dramatic poetry. "
        "Then use the correct expert agent to analyze it."
    ),
    handoffs=[lyrics_agent,narrative_agent,dramatic_agent],
    model=model,
)

# ✅ Main Function
def main():
    print("🎭 Poetry Analyzer — Gemini + OpenAI Agent SDK")
    print("Enter your poem or press Enter to use the default poem:\n")
    user_input = input("📝 Your poem: ").strip()

    # Use default poem if user input is empty
    poem = user_input if user_input else default_poem

    print("\n🤖 Classifying and analyzing your poem using HandOff...\n")
    result = Runner.run_sync(triage_agent, poem)

    print("\n📊 Final Analysis:")
    print(result.final_output)
main()