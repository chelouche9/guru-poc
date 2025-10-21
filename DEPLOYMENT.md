# Deployment Guide

## 🏠 Local Development Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Playwright Browsers

This is **required** for local development:

```bash
playwright install chrome
```

Or with system dependencies:

```bash
playwright install chrome --with-deps
```

### 3. Set Up Secrets

**Option A: Using Streamlit Secrets (Recommended)**

Create `.streamlit/secrets.toml` in the project root:

```toml
# OpenAI API Key (Required)
OPENAI_API_KEY = "your_openai_api_key_here"

# Local browser will be used automatically (default)
# USE_CLOUD_BROWSER = "false"
```

**Option B: Using Environment Variables**

Create a `.env` file in the project root:

```env
# OpenAI API Key (Required)
OPENAI_API_KEY=your_openai_api_key_here

# Local browser will be used automatically (default)
# USE_CLOUD_BROWSER=false
```

The app checks `st.secrets` first, then falls back to environment variables.

### 4. Run the App

```bash
streamlit run main.py
```

---

## ☁️ Streamlit Cloud Deployment

Streamlit Cloud **cannot install local browsers** due to system restrictions. You **must** use a cloud browser service.

### Step 1: Sign Up for Browserbase

1. Go to [browserbase.com](https://www.browserbase.com/)
2. Sign up for an account (they offer a free tier)
3. Create a new project
4. Navigate to Settings → API Keys
5. Copy your:
   - **API Key**
   - **Project ID**

### Step 2: Configure Streamlit Cloud Secrets

In your Streamlit Cloud app settings → Secrets, add:

```toml
# OpenAI Configuration
OPENAI_API_KEY = "sk-..."

# Enable Cloud Browser (IMPORTANT!)
USE_CLOUD_BROWSER = "true"

# Browserbase Credentials
BROWSERBASE_API_KEY = "bb_..."
BROWSERBASE_PROJECT_ID = "..."
```

**⚠️ Important**: Make sure `USE_CLOUD_BROWSER` is set to `"true"` (with quotes)

### Step 3: Deploy

1. Push your code to GitHub
2. Deploy through Streamlit Cloud
3. The app will automatically use Browserbase cloud browser

---

## 🔍 Troubleshooting

### Error: "No such file or directory: 'uvx'"

This means the app is trying to install a local browser. Solutions:

**If on Streamlit Cloud:**

- ✅ Set `USE_CLOUD_BROWSER = "true"` in Secrets
- ✅ Add Browserbase API credentials
- ✅ Restart your app

**If on Local:**

- ✅ Run `playwright install chrome`
- ✅ Make sure `USE_CLOUD_BROWSER` is NOT set to "true" locally

### Error: "Browser path not found" or "CDP URL not set"

**On Streamlit Cloud:**

- ✅ Verify `USE_CLOUD_BROWSER = "true"` (with quotes!)
- ✅ Double-check Browserbase credentials are correct
- ✅ Ensure your Browserbase account is active
- ✅ Check you have remaining credits/quota on Browserbase

**On Local:**

- ✅ Install browsers: `playwright install chrome`
- ✅ Make sure `USE_CLOUD_BROWSER` is false or not set

### Error: "Browserbase credentials are missing"

- ✅ Add `BROWSERBASE_API_KEY` to Streamlit Secrets
- ✅ Add `BROWSERBASE_PROJECT_ID` to Streamlit Secrets
- ✅ Make sure there are no typos in the secret names

---

## 💰 Browserbase Pricing

- **Free Tier**: Available for testing
- **Paid Tiers**: For production use
- Check [browserbase.com/pricing](https://www.browserbase.com/pricing) for details

---

## 🔄 Switching Between Local and Cloud

The app automatically detects the environment:

| Environment         | Configuration                                      |
| ------------------- | -------------------------------------------------- |
| **Local Dev**       | `USE_CLOUD_BROWSER=false` or not set               |
| **Streamlit Cloud** | `USE_CLOUD_BROWSER=true` + Browserbase credentials |

You can also use cloud browser locally by setting the environment variables.
