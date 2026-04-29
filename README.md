# AI Support Assistant

AI-powered customer support assistant using LLM that answers user queries based on predefined knowledge.

---

##  Features
- Answers customer queries using LLM
- Simple UI using Streamlit
- Uses API-based inference (OpenRouter)
- Environment-based secure API handling

---

##  Setup Instructions

1. Clone the repository  
2. Install dependencies  
   pip install -r requirements.txt  

3. Create a `.env` file and add your API key  
   OPENROUTER_API_KEY=your_api_key_here  

4. Run the app  
   streamlit run app.py  

---

##  Tooling

- **Streamlit** → UI for interaction  
- **Python** → Backend logic  
- **OpenRouter API** → LLM access  
- **python-dotenv** → Secure environment variable handling  

---

##  Tradeoffs

- Used API-based LLM instead of local model for simplicity and speed  
- Limited context handling due to time constraints  
- No database used — responses are generated dynamically  

---

##  Notes

- `.env` file is not included for security reasons  
- Use `.env.example` as reference  

---