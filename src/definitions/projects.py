PARKER_AI_TECHNOLOGIES = ["Python", "OpenAI", "Retell", "FastAPI", "Google Calendar API", "Calendly API"]

PARKER_AI_DETAILS = """
Using RetellAI, Parker is an AI customer service agent to aid in addressing customer inquiries about a company's services, 
and is also capable of booking meetings with Google Calendar and Google Meet.
"""

FINANCE_TRACKER_TECHNOLOGIES = [
    "Python", "OpenAI", "Typescript", "Express", "Redis", "Streamlit"
]

FINANCE_TRACKER_DETAILS = """
An LLM Powered finance tracker that analyzes expenditures and generates recommendations. Also features a personalized 
chat bot with GPT4o which enables you to make inquiries about your spending data. 
"""

SENTIMENT_ANALYSIS_TECHNOLOGIES = ["Python", "OpenAI", "Flask", "Redis", "BeautifulSoup"]

SENTIMENT_ANALYSIS_DETAILS = """
Scrapes and processes news articles in order to generate a forecast and sentiment analysis of future price fluctuations, 
which are classified by the LLM.
"""

ML_TECHNOLOGIES = ["Python", "SKLearn", "Huggingface"]
ML_DETAILS = """
Trained a Binary Text Classification Machine Learning model for optimizing web scraping operations, and developed an optimization
method for finding and training the most optimal model, and benchmarked with classification results from an LLM.
"""

MT5_DATALOADER_DETAILS = """ 
Spearheaded the development of a data pipeline for fetching historical OHLCV data for assets in MetaTrader 5 across 
multiple timeframes.
"""

SLACK_DETAILS = """
Led the development of a Slack application that integrates with a company's API, and developed custom modals for enhanced 
user experiences.
"""

PROJECTS = [
    {
        "title": "ParkerAI",
        "description": "An AI Customer Service agent",
        "technologies": PARKER_AI_TECHNOLOGIES,
        "details": PARKER_AI_DETAILS
    },
    {
        "title": "LLM Finance Tracker",
        "description": "An LLM Powered finance tracker",
        "technologies": FINANCE_TRACKER_TECHNOLOGIES,
        "details": FINANCE_TRACKER_DETAILS,
        "link": "https://expense-tracker-st-app.fly.dev/"
    },
    {
        "title": "GPT Sentiment Analysis",
        "description": "Generates a sentiment analysis on prices based on recent events.",
        "technologies": SENTIMENT_ANALYSIS_TECHNOLOGIES,
        "details": SENTIMENT_ANALYSIS_DETAILS
    },
    {
        "title": "MT5Dataloader",
        "description": "Data pipeline for OHLCV data for MetaTrader5.",
        "technologies": ["Python", "MetaTrader5 API"],
        "details": MT5_DATALOADER_DETAILS,
    },
    {
        "title": "ML Text Classification",
        "description": "Text Classification Machine Learning Model for optimizing web scraping operations",
        "technologies": ML_TECHNOLOGIES,
        "details": ML_DETAILS
    },
    {
        "title": "Slack Integration",
        "description": "Application to allow access to a company's API via Slack.",
        "technologies": ["Python", "Slack API"],
        "details": SLACK_DETAILS
    }
]
