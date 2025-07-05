Medi-bot 🤖💊
Welcome to Medi-Bot, your intelligent healthcare assistant designed to simplify medical information processing and provide quick insights from your health data.

Overview
Medi-Bot is a smart chatbot application that allows users to upload medical reports and receive helpful, AI-driven responses. It supports multiple input formats and provides an accessible way to understand complex medical documents.

Features
Multi-format Uploads: Upload medical reports in PDF, image, or audio formats.
AI-Powered Insights: Utilizes advanced AI to analyze medical data and answer user queries.
User-Friendly Interface: Easy-to-use interface built with Streamlit for quick interactions.
Multi-language Support: Communicate in various languages for wider accessibility.
Voice Interaction: Supports voice commands for hands-free operation.
Gemini API Model
Medi-bot leverages the Gemini API model, developed by Google DeepMind, which is a state-of-the-art large language model designed for advanced conversational AI and multimodal understanding.

Key Highlights of Gemini API:
Conversational AI: Supports complex, multi-turn dialogue interactions.
Multimodal Input: Processes text and images for richer context (depending on API capabilities).
Enhanced Reasoning: Improved logic, arithmetic, and nuanced understanding.
Few-shot / Zero-shot Learning: Efficiently performs new tasks with minimal examples.
Scalable Integration: Accessible via Google Cloud AI API for seamless app integration.
By integrating Gemini, Medi-bot provides accurate, context-aware responses to medical queries, helping users interpret their health reports with confidence.

Getting Started
Follow these steps to run Medi-bot on your local machine:

Prerequisites
Python 3.7+
Pip package manager
Google Cloud account with Gemini API access and credentials
Installation
Clone the repository:

git clone https://github.com/IshaanKapil/Medi-Bot.git
cd Medi-Bot
Create a .env file:

Add necessary environment variables such as your Google API credentials and Gemini API keys.

Install dependencies:

bash Copy code pip install -r requirements.txt Run the application:

bash Copy code streamlit run app.py Usage Upload your medical reports in supported formats.

Interact with Medi-bot through text or voice commands.

Receive AI-powered responses and insights to understand your health data better.
