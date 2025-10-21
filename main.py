import streamlit as st
from browser_use import Agent, ChatOpenAI
from browser_use.browser.session import BrowserSession
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

# Context that will be prepended to user queries
CONTEXT = """
Context:
The website Casino Guru (https://casino.guru) is an independent information platform focused on online casinos, bonuses, free casino games, user reviews, complaints resolution, and industry news. It is not a casino operator, but a listing + review + community platform.

Structure & content:
- Large database of online casinos and bonus offers
- Each casino review page includes an expert "Safety Index", pros and cons, supported languages, payment methods, user feedback, and other metadata
- Bonus-offers section with casino bonus promotions, details and terms
- Games section offers free-play games and metadata about each game
- Complaints/forum section allows players to post issues with casinos
- News section provides articles about online gambling industry developments

Crawl focus:
Stay within casino.guru domain, focusing on:
- /casino-reviews/ pages → extract casino metadata
- /bonuses/ → extract bonus offers
- /games/ or /free-games/ → extract game info
- /complaints/ and/or /forum/ → extract complaint summaries
- /news/ → extract news articles

Data to capture:
- Casinos: name, URL, Safety Index, pros, cons, supported languages, payment methods, user feedback
- Bonuses: casino name, bonus value, terms, link, valid countries
- Games: game title, provider, free version link, game type
- Complaints: casino name, date, issue summary, resolution status

Goal:
Answer user queries by retrieving relevant information from casino.guru, citing URLs/pages, and summarizing findings.

YOUR TASK:
"""

async def run_agent(user_question):
    """Run the agent with the user's question in headless mode"""
    task = CONTEXT + user_question
    llm = ChatOpenAI(model="gpt-4.1-mini")
    
    # Check if we should use cloud browser (for Streamlit Cloud deployment)
    # Cloud browser requires BROWSERBASE_API_KEY and BROWSERBASE_PROJECT_ID env vars
    use_cloud_browser = os.getenv('USE_CLOUD_BROWSER', 'false').lower() == 'true'
    
    if use_cloud_browser:
        # Validate Browserbase credentials
        browserbase_api_key = os.getenv('BROWSERBASE_API_KEY')
        browserbase_project_id = os.getenv('BROWSERBASE_PROJECT_ID')
        
        if not browserbase_api_key or not browserbase_project_id:
            raise ValueError(
                "Cloud browser mode is enabled but Browserbase credentials are missing. "
                "Please set BROWSERBASE_API_KEY and BROWSERBASE_PROJECT_ID environment variables. "
                "Get your credentials at https://www.browserbase.com/"
            )
        
        # Configure browser session to use cloud browser (Browserbase)
        browser = BrowserSession(
            headless=True,
            use_cloud=True
        )
    else:
        # Use local browser (for local development)
        browser = BrowserSession(headless=True)
    
    # Create agent with configured browser
    agent = Agent(task=task, llm=llm, browser=browser)
    result = await agent.run()
    return result

def main():
    st.set_page_config(page_title="Casino Guru Agent", page_icon="🎰", layout="wide")
    
    st.title("🎰 Casino Guru Research Agent")
    st.markdown("Ask questions about casinos, bonuses, games, and complaints from Casino Guru.")
    
    # Initialize session state for response
    if 'response' not in st.session_state:
        st.session_state.response = None
    if 'processing' not in st.session_state:
        st.session_state.processing = False
    
    # Question input
    user_question = st.text_area(
        "Enter your question:",
        placeholder="Example: Find the ZotaBet Casino Review, list the safety index, pros and cons.",
        height=150,
        key="question_input"
    )
    
    # Send button
    col1, col2 = st.columns([1, 5])
    with col1:
        send_button = st.button("🚀 Send", type="primary", use_container_width=True)
    
    # Process the query
    if send_button and user_question.strip():
        st.session_state.processing = True
        st.session_state.response = None
        
        with st.spinner("🔍 Agent is searching and analyzing..."):
            try:
                # Run the agent headless
                result = asyncio.run(run_agent(user_question))
                # Extract only the final result (final_result is a method, so call it)
                final_answer = result.final_result()
                st.session_state.response = final_answer if final_answer else "✅ Task completed, but no final result was extracted."
                st.session_state.processing = False
            except ValueError as e:
                # Configuration errors (like missing Browserbase credentials)
                st.session_state.response = f"⚙️ Configuration Error:\n\n{str(e)}"
                st.session_state.processing = False
            except FileNotFoundError as e:
                # Missing dependencies (like uvx or playwright)
                error_msg = str(e)
                if 'uvx' in error_msg:
                    st.session_state.response = (
                        "❌ Browser Setup Error:\n\n"
                        "The local browser installation failed. This usually happens when:\n\n"
                        "1. **For Local Development**: Install Playwright browsers with:\n"
                        "   ```bash\n"
                        "   playwright install chrome\n"
                        "   ```\n\n"
                        "2. **For Streamlit Cloud**: Set `USE_CLOUD_BROWSER=true` and add your Browserbase credentials:\n"
                        "   - BROWSERBASE_API_KEY\n"
                        "   - BROWSERBASE_PROJECT_ID\n\n"
                        "Get credentials at: https://www.browserbase.com/"
                    )
                else:
                    st.session_state.response = f"❌ Error: {error_msg}"
                st.session_state.processing = False
            except Exception as e:
                # General errors
                st.session_state.response = f"❌ Error: {str(e)}\n\nIf you're on Streamlit Cloud, make sure USE_CLOUD_BROWSER=true and Browserbase credentials are set."
                st.session_state.processing = False
    
    # Display response
    if st.session_state.response is not None:
        st.markdown("---")
        st.subheader("📊 Response:")
        st.markdown(st.session_state.response)

if __name__ == "__main__":
    main()