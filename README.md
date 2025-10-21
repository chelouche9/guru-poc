# Casino Guru Research Agent

A Streamlit-powered web interface for querying information from Casino Guru using an AI agent with headless browser automation.

## Features

- 🎰 Simple question input interface
- 🤖 AI agent performs headless web browsing
- 📊 Clean response display
- 🔍 Searches Casino Guru for casinos, bonuses, games, complaints, and news
- ☁️ Supports both local and cloud browser deployment

## Local Development Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a `.env` file with your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Install Playwright Browsers (for local development)

```bash
playwright install chrome
```

### 4. Run the App

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

## Streamlit Cloud Deployment

When deploying to Streamlit Cloud, you need to use a **cloud browser service** because Streamlit Cloud doesn't support installing local browsers.

### Option 1: Using Browserbase (Recommended)

1. **Sign up for Browserbase** at [browserbase.com](https://www.browserbase.com/)

2. **Get your API credentials**:

   - API Key
   - Project ID

3. **Configure Streamlit Cloud Secrets**:
   Go to your Streamlit Cloud app settings and add these secrets:

   ```toml
   OPENAI_API_KEY = "your_openai_api_key"
   BROWSERBASE_API_KEY = "your_browserbase_api_key"
   BROWSERBASE_PROJECT_ID = "your_browserbase_project_id"
   USE_CLOUD_BROWSER = "true"
   ```

4. **Deploy your app** - The app will automatically use the cloud browser when `USE_CLOUD_BROWSER=true`

### Option 2: Using CDP URL (Advanced)

If you have your own browser server with Chrome DevTools Protocol (CDP) enabled, you can configure it using environment variables.

## Environment Variables

| Variable                 | Required   | Description                                                         |
| ------------------------ | ---------- | ------------------------------------------------------------------- |
| `OPENAI_API_KEY`         | Yes        | Your OpenAI API key                                                 |
| `USE_CLOUD_BROWSER`      | No         | Set to `"true"` for Streamlit Cloud deployment (default: `"false"`) |
| `BROWSERBASE_API_KEY`    | Cloud only | Browserbase API key (required if `USE_CLOUD_BROWSER=true`)          |
| `BROWSERBASE_PROJECT_ID` | Cloud only | Browserbase Project ID (required if `USE_CLOUD_BROWSER=true`)       |

## How to Use

1. Enter your question in the text area
2. Click "🚀 Send" button
3. Wait for the agent to search and analyze (runs headless in background)
4. View the final response when ready

## Example Questions

- Find the ZotaBet Casino Review, list the safety index, pros and cons
- Which casinos have a Safety Index over 90 and accept PayPal?
- What are the latest bonuses for new players?
- Find complaints about [Casino Name]
- What are the top-rated casinos in 2025?

## Troubleshooting

### "Error getting browser path" on Streamlit Cloud

This means the local browser couldn't be installed. Make sure you've:

1. Set `USE_CLOUD_BROWSER=true` in your Streamlit secrets
2. Added your Browserbase API credentials

### Local browser installation fails

Install Playwright browsers manually:

```bash
playwright install chrome --with-deps
```
