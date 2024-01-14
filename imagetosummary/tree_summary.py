# Libraries to load environment variables
import os
from dotenv import load_dotenv
load_dotenv()

# libraries to use google generative ai
import google.generativeai as genai
import PIL.Image


# configure API key for google gemini
gemini_api_key = os.environ["GEMINI_API_KEY"]
genai.configure(api_key = gemini_api_key)


# load the gemini pro vision model"
model_name = "gemini-pro-vision"
llm = genai.GenerativeModel(model_name)

# load the image using pillow
img = PIL.Image.open("../image_files/scanned_tree.jpg")

# generate response
response = llm.generate_content(img)
print("text_response",response.text)

