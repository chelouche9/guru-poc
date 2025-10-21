# Quick Start Guide

## 🚀 Getting Started

### For Local Development (Your Computer)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Install Playwright browsers
playwright install chrome

# 3. Set up your secrets (choose one)
# Option A: Streamlit secrets (recommended)
mkdir -p .streamlit
echo 'OPENAI_API_KEY = "your_key_here"' > .streamlit/secrets.toml

# Option B: Environment variables
# echo "OPENAI_API_KEY=your_key_here" > .env

# 4. Run the app
streamlit run main.py
```

---

### For Streamlit Cloud Deployment

**The error you're seeing (`uvx not found`) means you need to use cloud browser mode.**

#### Quick Fix Steps:

1. **Sign up for Browserbase** (free tier available)

   - Go to: https://www.browserbase.com/
   - Create account → Create project
   - Copy your API Key and Project ID

2. **Add to Streamlit Secrets** (in your app settings):

   ```toml
   OPENAI_API_KEY = "your_openai_key"
   USE_CLOUD_BROWSER = "true"
   BROWSERBASE_API_KEY = "your_browserbase_key"
   BROWSERBASE_PROJECT_ID = "your_project_id"
   ```

3. **Restart your Streamlit app**

That's it! The app will now use cloud browsers instead of trying to install Chrome locally.

---

## ❓ Why This Change?

**Problem**: Streamlit Cloud doesn't allow installing browsers (no sudo access)

**Solution**: Use Browserbase cloud browser service

**Cost**: Free tier available for testing

---

## 📋 Summary of Files

| File               | Purpose                                       |
| ------------------ | --------------------------------------------- |
| `main.py`          | Main Streamlit app with cloud browser support |
| `requirements.txt` | Python dependencies (includes playwright)     |
| `README.md`        | Full documentation                            |
| `DEPLOYMENT.md`    | Detailed deployment instructions              |
| `QUICK_START.md`   | This file - quick setup guide                 |

---

## 🆘 Still Having Issues?

1. Check `DEPLOYMENT.md` for detailed troubleshooting
2. Make sure `USE_CLOUD_BROWSER = "true"` (with quotes!) in Streamlit secrets
3. Verify your Browserbase credentials are correct
4. Ensure you have credits remaining on Browserbase account
