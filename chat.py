import google.generativeai as genai
import os
import dotenv
import PIL.Image
import os

dotenv.load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Shared message history
messages = []




def init_prompt(desease):
    messages.append({"role": "user", "parts": f"""Imagine you are an AI Expert in analying Skin deseases.
                    Your job is to Interact with the user to confirm if they really have the given skin desease. 
                    In case it's an healthy skin, say the skin looks healthy.
                    If it's a skin desease, ask for any symptoms ask atleast 2-3 questions to confirm the desease.
                    Remember the given desease is provided by analyzing a image, your job is to confirm if the user really has the desease or not.
                    If the symptoms doesn't match the desease, ask the user to consult a doctor.
                    ASK ONE QUESTION AT A TIME.
                    Desease: {desease}
                    Question:
                    """})
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(messages)
    messages.append({"role": "model", "parts": [response.text]})
    print(response.text)
    return response.text

def generate_response(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    messages.append({"role": "user", "parts": prompt})
    response = model.generate_content(messages)
    messages.append({"role": "model", "parts": [response.text]})
    return response.text


def process_img():
    try:
        img = PIL.Image.open('image.jpg')
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(["""your job is to analyze the given image and say if you suspect any skin deseases or not. If the given image is not a skin, say "not a skin". If you think it's a healthy skin, say "healthy skin". If NOT then provide the name of desease you think it is. don't give any other information. Look at the image clearly befor responding. Response:  """, img], stream=True)
        response.resolve()
        print(response.text)
        return response.text
    except Exception as e:
        print(e)
        return e
