import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv("Environment.env")
ny = os.getenv('USA_NY')          # 'New York'
ma = os.getenv('USA_MA')          # 'Massachusetts'
ap = os.getenv('INDIA_AP')        # 'Andhra Pradesh'

print(f"New York: {ny}")
print(f"Massachusetts: {ma}")
print(f"Andhra Pradesh: {ap}")