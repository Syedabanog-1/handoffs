
🎭 Poetry Analyzer — Gemini + OpenAI Agent SDK
This project is a Poetry Analyzer Agent System built using the OpenAI Agent SDK and Gemini 2.0 API via LiteLLM. It classifies a poem into one of three types — Lyric, Narrative, or Dramatic — and provides a detailed analysis using specialized agents.

.

🧠 Project Structure
This project consists of:

poet_agent: Accepts a user-input poem or defaults to a predefined stanza.

triage_agent: Classifies the poem type and routes it to the appropriate expert agent.

lyrics_agent: Analyzes lyric (emotional/personal) poetry.

narrative_agent: Analyzes narrative (story-based) poetry.

dramatic_agent: Analyzes dramatic (performance/dialogue-based) poetry.


🛠️ Tech Stack
Python 3.10+

OpenAI Agent SDK

Gemini 2.0 Flash via LiteLLM

Environment variables via python-dotenv

🚀 How It Works
User provides a poem input (or defaults to a built-in stanza).

triage_agent identifies the type of poem.

HandOff is used to delegate the analysis to the right expert agent.

The system returns an in-depth breakdown of the poem.


🔐 Environment Setup
Create a .env file in the project root:
GOOGLE_API_KEY=your_gemini_api_key

▶️ Run the Program
 py demonstrate_poetry.py 
 or
 uv run demonstrate_poetry.py

 
📚 Poetry Types Explained
Lyric Poetry: Focuses on emotions, personal feelings (e.g., love, joy).

Narrative Poetry: Tells a story with plot and characters.

Dramatic Poetry: Involves performance, dialogue, and monologue (like a play).

.

🧪 Example Poem

From dawn till dusk, I've felt your love so true,
My heart beats with joy, my soul feels anew.
You've found the courage to come to me,
My heart overflows with love, wild and carefree.


🤝 Credits
Gemini API (Google AI)

OpenAI Agent SDK

LiteLLM for model integration

📝 License
This project is licensed under the MIT License.


<img width="1611" height="902" alt="code" src="https://github.com/user-attachments/assets/4cafd7ac-94a8-4ee4-aa24-37139a279759" />

<img width="1612" height="903" alt="Narrative Poetry" src="https://github.com/user-attachments/assets/ae25a761-b361-4f96-9baa-9e33520a3092" />
<img width="1607" height="904" alt="Lyric Poetry" src="https://github.com/user-attachments/assets/73758ca1-38c6-4311-bb3b-17657b93a21d" />
<img width="1608" height="902" alt="Dramatic Poetry" src="https://github.com/user-attachments/assets/3a1c62bc-475c-455e-8045-b91a601cf382" />
<img width="1610" height="904" alt="Lyrics Poetry" src="https://github.com/user-attachments/assets/47772b50-794b-4b36-9586-b4108cf591a9" />
