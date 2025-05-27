import os

# Use Streamlit secrets in cloud, fallback to environment variable locally
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or \
                 __import__("streamlit").secrets["OPENAI_API_KEY"]