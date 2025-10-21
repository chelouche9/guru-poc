# Casino Guru Research Agent

A Streamlit-powered web interface for querying information from Casino Guru using an AI agent.

## Features

- 🎰 Simple question input interface
- 🤖 AI agent performs headless web browsing
- 📊 Clean response display
- 🔍 Searches Casino Guru for casinos, bonuses, games, complaints, and news

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set up your environment variables:
   Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the Streamlit app:

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

## How to Use

1. Enter your question in the text area
2. Click "Send" button
3. Wait for the agent to search and analyze (runs headless)
4. View the response when ready

## Example Questions

- Find the ZotaBet Casino Review, list the safety index, pros and cons
- Which casinos have a Safety Index over 90 and accept PayPal?
- What are the latest bonuses for new players?
- Find complaints about [Casino Name]
