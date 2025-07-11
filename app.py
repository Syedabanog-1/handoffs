import os
import streamlit as st
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel, AsyncOpenAI
from agents.extensions.models.litellm_model import LitellmModel

# ----------------------------------------
# ✅ Disable Tracing and Load API Key
# ----------------------------------------
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

# ----------------------------------------
# ✅ Default Poem
# ----------------------------------------
default_poem = """
From dawn till dusk, I've felt your love so true,
My heart beats with joy, my soul feels anew.
You've found the courage to come to me,
My heart overflows with love, wild and carefree.
"""

# ----------------------------------------
# ✅ Agents Setup
# ----------------------------------------
poet_agent = Agent(
    name="poet_agent",
    instructions=(
        "Take poetry stanza from the user as input, or use the default poem if none is provided.\n\n"
        f"Default poem:\n{default_poem}"
    ),
    model=model,
)

lyrics_agent = Agent(
    name="lyrics_agent",
    instructions=(
        "You are a lyric poetry expert. Identify and analyze personal and emotional themes in the poem. "
        "Describe the poem's emotional tone and expressive elements."
    ),
    model=model,
)

narrative_agent = Agent(
    name="narrative_agent",
    instructions=(
        "You are a narrative poetry expert. Identify storytelling features in the poem, like plot, sequence, and characters. "
        "Explain the narrative arc and message."
    ),
    model=model,
)

dramatic_agent = Agent(
    name="dramatic_agent",
    instructions=(
        "You are a dramatic poetry expert. Look for performance aspects in the poem like dialogue, monologue, or character speech. "
        "Describe how it's meant to be acted and its dramatic structure."
    ),
    model=model,
)

triage_agent = Agent(
    name="triage_agent",
    instructions=(
        "You are a smart poetry classifier. Based on the content of the poem, determine if it's lyric, narrative, or dramatic poetry. "
        "Then use the correct expert agent to analyze it."
    ),
    handoffs=[lyrics_agent, narrative_agent, dramatic_agent],
    model=model,
)

# ----------------------------------------
# ✅ Streamlit UI
# ----------------------------------------
st.set_page_config(page_title="Poetry Analyzer", page_icon="🎭")
st.title("🎭 Poetry Analyzer — Streamlit + Gemini Agents")
st.write("Paste your poem below or leave it blank to use the default poem.")

user_input = st.text_area("📜 Enter your poem:", height=200)

if st.button("🔍 Analyze"):
    poem = user_input.strip() if user_input.strip() else default_poem
    st.info("⏳ Analyzing the poem, please wait...")

    async def analyze():
        result = await Runner.run(triage_agent, poem)
        return result.final_output

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    analysis_result = loop.run_until_complete(analyze())

    st.success("✅ Analysis Complete!")
    st.subheader("📊 Final Analysis:")
    st.write(analysis_result)
