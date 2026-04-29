# AI Support Assistant

AI-powered customer support assistant that uses LLMs to answer user queries in real-time.

---

## Features

* Answers customer queries using an LLM
* Simple UI built with Streamlit
* Uses API-based inference via OpenRouter
* Secure API key handling using environment variables

---

## How It Works

* User enters a query through the Streamlit interface
* The query is sent to the OpenRouter API
* The LLM processes the request and generates a response
* The response is displayed back to the user in real-time

---

## Setup Instructions

1. Clone the repository

2. Install dependencies

```
pip install -r requirements.txt
```

3. Create a `.env` file and add your API key

```
OPENROUTER_API_KEY=your_api_key_here
```

4. Run the application

```
streamlit run app.py
```

---

## Tooling

* **Streamlit** → UI for interaction
* **Python** → Backend logic
* **OpenRouter API** → LLM access
* **python-dotenv** → Secure environment variable handling

---

## Tradeoffs

* Used API-based LLM instead of a local model for simplicity and faster development
* Limited context handling due to time constraints
* No database used — responses are generated dynamically

---

## Notes

* `.env` file is not included in the repository for security reasons
* Use `.env.example` as a reference

---

## Example Queries

* "What is your return policy?"
* "How long does delivery take?"

The assistant responds with relevant answers using an LLM.

---

## Future Improvements

* Add conversation memory for better context handling
* Integrate a knowledge base for domain-specific responses
* Improve UI/UX for a better user experience
* Add authentication and user session handling
