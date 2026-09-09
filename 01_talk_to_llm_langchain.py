import dotenv
import dotenv
from dotenv import load_dotenv

import os
load_dotenv()  # Load environment variables from .env file
open_ai_API_KWY = os.environ.get("OPENAI_API_KEY")  # Get the OpenAI API key from environment variables
print(f"end={open_ai_API_KWY}")




