## Mock LLM Response Notice

This project currently uses mocked AI/LLM responses instead of real LLM API calls.

Why?

* No external API key is required
* The project can run completely offline
* Makes testing and demonstration easier
* Simulates how a real production AI response would look

The analysis responses (MEDDIC extraction, objection analysis, coaching insights, and deal intelligence) are generated using predefined intelligent mock logic inside:


This was intentionally designed to demonstrate:

* FastAPI backend architecture
* AI workflow design
* Structured response generation
* Frontend integration
* End-to-end system flow

without depending on paid LLM services.

In a real production environment, the mocked response layer can easily be replaced with:

* OpenAI GPT APIs
* Claude APIs
* Gemini APIs
* Ollama Local LLMs
* LangChain pipelines
* HuggingFace models

The current implementation focuses on demonstrating system architecture and AI application flow rather than real-time LLM inference.
