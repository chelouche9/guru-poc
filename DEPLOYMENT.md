# Deployment Guide

## Environment Variables Setup

### Local Development

Create a `.env` file in the project root with:

```env
# OpenAI API Key (Required)
OPENAI_API_KEY=your_openai_api_key_here

# Local browser will be used automatically
USE_CLOUD_BROWSER=false
```

### Streamlit Cloud Deployment

In your Streamlit Cloud app settings, add these secrets:

```toml
# OpenAI Configuration
OPENAI_API_KEY = "your_openai_api_key"

# Enable Cloud Browser
USE_CLOUD_BROWSER = "true"

# Browserbase Credentials (get these from https://www.browserbase.com/)
BROWSERBASE_API_KEY = "your_browserbase_api_key"
BROWSERBASE_PROJECT_ID = "your_browserbase_project_id"
```

## Browserbase Setup

1. Go to [browserbase.com](https://www.browserbase.com/)
2. Sign up for an account
3. Create a new project
4. Copy your API Key and Project ID
5. Add them to your Streamlit Cloud secrets

## Verification

After deployment, if you see errors about "browser path not found":

- ✅ Ensure `USE_CLOUD_BROWSER` is set to `"true"`
- ✅ Verify your Browserbase credentials are correct
- ✅ Check that your Browserbase account is active
