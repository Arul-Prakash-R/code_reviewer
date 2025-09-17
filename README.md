# Code Scanner GitHub App

A GitHub App that scans repositories for security vulnerabilities using AI models from Hugging Face. Built with Python and Flask.

## Features
- Listens to GitHub webhook events (push, pull_request)
- Scans code for vulnerabilities using Hugging Face Transformers
- Posts results as comments on PRs or as GitHub Checks

## Setup

1. **Clone the repo**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables:**
   - Copy `.env.example` to `.env` and fill in your GitHub App credentials and Hugging Face API key (if needed)
4. **Run the Flask server:**
   ```bash
   flask run
   ```

## Files
- `app.py`: Flask webhook server
- `github_app.py`: GitHub App authentication/utilities
- `scanner.py`: Hugging Face code scanning logic

## Notes
- You need to create and configure a GitHub App (see GitHub docs)
- For advanced scanning, customize `scanner.py` with your preferred Hugging Face model "# code_reviewer" 
g
