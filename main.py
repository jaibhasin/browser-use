from langchain_google_genai import ChatGoogleGenerativeAI
# from browser_use import Agent
from pydantic import SecretStr
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


from browser_use import Agent, Browser, BrowserConfig
import asyncio
# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',  # macOS path
        # For Windows, typically: 
        # For Linux, typically: '/usr/bin/google-chrome'
    )
)

# llm = ChatOpenAI(model="gpt-4o")
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))


async def main():
    agent = Agent(
    task="Get the latest price of bitcoin, ethereum and cardano and also show volume traded",
    llm=llm,
    browser=browser
    )
    result = await agent.run()
    print(result)
    await browser.close()

asyncio.run(main())