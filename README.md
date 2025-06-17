# AI Research Assistant

This project is an AI-powered research assistant that generates research paper summaries using language models and web tools. It can search the web, query Wikipedia, and save structured research outputs to a file.

## Features
- Uses Anthropic Claude or OpenAI GPT models via LangChain
- Web search with DuckDuckGo
- Wikipedia queries
- Saves research output with timestamp
- Structured output using Pydantic

## Requirements
Install dependencies with:
```
pip install -r req.txt
```

## Usage
Run the assistant:
```
python main.py
```
You will be prompted to enter a research query. The assistant will use AI and tools to generate a structured summary and optionally save it to a file.

## Configuration
- API keys for Anthropic or OpenAI should be set in a `.env` file (see [dotenv](https://pypi.org/project/python-dotenv/)).
- The virtual environment folder (e.g., `perspa/`) should be excluded from version control using `.gitignore`.

## Files
- `main.py`: Main entry point for the assistant
- `tools.py`: Custom and third-party tools for search, Wikipedia, and saving output
- `req.txt`: Python dependencies

## License
MIT License