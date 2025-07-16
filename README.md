# eco-agent-
An AI-powered command-line assistant built with the Google Gemini API to provide reliable climate change information, fact-checking, and sustainable advice.
EcoAgent: Your AI Climate Advisor
Replace this placeholder with a real screenshot of your bot in action.

EcoAgent is a command-line assistant powered by the Google Gemini API, designed to combat climate misinformation and make complex climate science accessible to everyone. It acts as a reliable fact-checker, a source of practical sustainability advice, and an educational tool to improve overall climate literacy.

Problem Solved
In an era of information overload, finding trustworthy and easy-to-understand information about climate change is a significant challenge. EcoAgent addresses this by providing:

Clarity: Simple answers to complex questions.

Trust: Fact-checking claims against reliable data.

Action: Practical advice for individuals who want to help.

Key Features
Instant Q&A: Get clear, concise answers to a wide range of questions about climate science, policy, and environmental effects.

On-Demand Fact-Checking: Quickly verify the accuracy of claims or news you encounter online.

Actionable Advice: Receive personalized, practical tips for sustainable living and reducing your carbon footprint.

Gemini-Powered Analysis: Generate in-depth explanations, create weekly sustainability plans, and get detailed debunkings of common myths.

Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
Python 3.7 or higher

A Google Gemini API Key. You can get one for free from Google AI Studio.

Installation
Clone the repository:

git clone https://github.com/YourUsername/EcoAgent.git
cd EcoAgent

Install the required packages:

pip install -r requirements.txt

(You will need to create a requirements.txt file with the following content):

google-generativeai

Set up your API Key:
It is recommended to set your API key as an environment variable to keep it secure.

On macOS/Linux:

export GEMINI_API_KEY="YOUR_API_KEY"

On Windows (PowerShell):

$env:GEMINI_API_KEY="YOUR_API_KEY"

Note: The script is also designed to let you paste the key directly if you have trouble with environment variables.

Usage
Once the installation is complete, you can run the bot with the following command:

python eco_agent.py

The application will start, and you can begin asking questions directly in your terminal. Type quit or exit to end the session.

How It Works
EcoAgent's reliability comes from a carefully engineered system prompt that instructs the Google Gemini model to act as a factual, unbiased expert on climate change. Every query from the user is sent to the Gemini API along with this system instruction, ensuring the responses are consistently helpful, accurate, and aligned with the agent's defined persona.

Future Work
[ ] Develop a user-friendly web application interface.

[ ] Create a browser extension for on-page fact-checking.

[ ] Explore multilingual support to increase global accessibility.

Contributing
Contributions are welcome! If you have suggestions for improving EcoAgent, please feel free to open an issue or submit a pull request.
