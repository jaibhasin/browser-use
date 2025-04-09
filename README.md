# Web Scraper using Browser-Use

This project demonstrates the use of [browser-use](https://docs.browser-use.com/quickstart) library to perform web automation tasks using AI. It uses any LLM (chatgpt , deepseek, ollama , gemini) to intelligently navigate and extract information from websites.

## Features

- Automated web browsing using browser-use library
- AI-powered web scraping using Google's Gemini model
- Environment variable based configuration
- Asynchronous execution for better performance

## Prerequisites

- Python 3.11 or higher
- Google Chrome browser installed
- Google Gemini API key or any other LLM API key

## Installation

1. Clone the repository:
```bash
git clone <https://github.com/jaibhasin/browser-use>
cd web_scraper
```

2. Create and activate a virtual environment using uv (recommended by browser-use):
```bash
uv venv --python 3.11
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

3. Install the required dependencies:
```bash
uv pip install browser-use langchain-google-genai python-dotenv
```

4. Install Playwright:
```bash
playwright install
```

5. Create a `.env` file in the project root and add your API key:
```
GEMINI_API_KEY=your_api_key_here
# For OpenAI, you can also add:
# OPENAI_API_KEY=your_openai_api_key
```

## Configuration

The script is configured to use:
- Google Chrome browser (path configured for Windows)
- Gemini 2.0 Flash model for AI processing
- Environment variables for API key management

## Usage

1. Make sure your Chrome browser is installed at the default location:
   - Windows: `C:\Program Files\Google\Chrome\Application\chrome.exe`
   - macOS: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
   - Linux: `/usr/bin/google-chrome`

2. Run the script:
```bash
python main.py
```

The script will:
- Connect to your Chrome browser
- Use Gemini AI to navigate and search for information
- Extract and display the requested data
- Automatically close the browser when done

## Example Task

The current script is configured to search for "bhasin group india" and extract emails of the top 5 people. You can modify the `task` parameter in `main.py` to perform different web scraping tasks.

## Documentation

For more detailed information about browser-use, please refer to the [official documentation](https://docs.browser-use.com/quickstart).

## License
MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 
