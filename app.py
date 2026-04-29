import streamlit as st
import requests
import os
import json
import re
from dotenv import load_dotenv

# ==============================
# 🔐 LOAD ENV
# ==============================
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

# ==============================
# 🎨 UI SETUP
# ==============================
st.set_page_config(page_title="AI Support Assistant", layout="centered")

st.markdown("## 🤖 AI Customer Support Assistant")
st.markdown("Analyze customer issues and generate smart replies")

# API KEY CHECK
if not API_KEY:
    st.error("❌ API key not found. Check your .env file")
    st.stop()

user_input = st.text_area("Enter customer message:")

# ==============================
# 🧠 API FUNCTION
# ==============================
def analyze_message(message):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "AI Support Assistant",
        "Content-Type": "application/json"
    }

    data = {
       "model": "openrouter/auto",
        "messages": [
            {
                "role": "user",
                "content": f"""
You are an AI customer support assistant.

Return ONLY valid JSON.
Do NOT include explanation.
Ensure all keys and strings use double quotes.
Escape special characters properly.

Message: {message}

Output:
{{
  "intent": "refund | exchange | complaint | other | null",
  "urgency": "low | medium | high",
  "reason": "short explanation",
  "confidence": 0-1,
  "reply_en": "professional reply in English",
  "reply_ar": "same reply in Arabic"
}}
"""
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        result = response.json()

        if "choices" in result:
            return result["choices"][0]["message"]["content"]
        else:
            return None, result

    except Exception as e:
        return None, str(e)

# ==============================
# 🔧 JSON CLEANER (STRONG)
# ==============================
def extract_json(text):
    try:
        # extract JSON using regex
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            json_str = match.group()

            # clean common issues
            json_str = json_str.replace("\n", " ")
            json_str = json_str.replace("\t", " ")

            return json.loads(json_str)

        return None
    except:
        return None

# ==============================
# 🚀 MAIN BUTTON
# ==============================
if st.button("Analyze"):
    if not user_input:
        st.warning("⚠️ Please enter a message")
    else:
        with st.spinner("Analyzing..."):
            result = analyze_message(user_input)

        # handle API failure
        if isinstance(result, tuple):
            st.error(f"API Error: {result[1]}")
        else:
            parsed = extract_json(result)

            if parsed:
                st.success(f"Intent: {parsed.get('intent')}")
                st.info(f"Urgency: {parsed.get('urgency')}")
                st.write(f"**Reason:** {parsed.get('reason')}")
                st.write(f"**Confidence:** {parsed.get('confidence')}")

                st.markdown("### 💬 Suggested Reply (English)")
                st.write(parsed.get("reply_en"))

                st.markdown("### 🌍 Suggested Reply (Arabic)")
                st.write(parsed.get("reply_ar"))

            else:
                st.error("⚠️ Could not parse JSON (model issue)")
                st.write(result)