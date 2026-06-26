# Serverless AI Sentiment Analysis Integration

A production-ready Python implementation that integrates with the Hugging Face Serverless Inference API to perform real-time sentiment analysis using the `distilbert-base-uncased-finetuned-sst-2-english` model.

## Features
- **Robust Exception Handling:** Implements `try-except` blocks with `requests.raise_for_status()` to gracefully handle network partitions and API errors.
- **Secure Token Authentication:** Uses Bearer token authorization structured within HTTP headers to interact with external providers securely.
- **Encapsulated Architecture:** The logic is completely decoupled into a reusable function `sprawdz_sentyment(tekst_uzytkownika)`, making it ready to be ported into cloud native environments like AWS Lambda.

## Tech Stack
- **Language:** Python 3.11+
- **Libraries:** `requests`
- **AI Infrastructure:** Hugging Face Inference API

## Infrastructure & Troubleshooting (Key Takeaways)
During development, a critical network resolution layout change was successfully diagnosed and mitigated:
- **Endpoint Migration:** The deprecated `api-inference.huggingface.co` endpoint was replaced with the modern `router.huggingface.co/hf-inference` infrastructure to resolve global DNS resolution issues (`NameResolutionError`).
- **Granular Permissions:** Configured fine-grained access tokens with specific `Inference` scopes to comply with the principle of least privilege (PoLP).

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install requests`
3. Generate a Fine-grained Access Token on Hugging Face with `Inference` permissions.
4. Replace `YOUR_HUGGING_FACE_TOKEN_HERE` with your token in the script.
5. Execute the script: `python main.py`
