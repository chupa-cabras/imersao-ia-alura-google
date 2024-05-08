import google.generativeai as genai
import os
import dotenv




dotenv.load_dotenv()

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])



# Set up the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",generation_config=generation_config,safety_settings=safety_settings)

def extract_from_text(pathname: str) -> list[str]:
  parts = [f"--- START OF FILE ${pathname} ---"]
  with open(pathname, "r") as file:
    parts.extend(file.readlines())
  return parts

gemini_session = model.start_chat(history=[
  {
    "role": "user",
    "parts": extract_from_text("./contents/renato.gobet.uzun.md")
  }
])

print('#Testando o trabalho do gemini-1.5-pro-latest com arquivos de textos')


gemini_session.send_message("Quem é Renato Uzun ?  Com base no signo do Renato (áries), com quais celebridades ele teria um relacionamento amoroso ? Justifique.")
print(gemini_session.last.text)
gemini_session.send_message("Cite todos os hobbies do Renato. O que sugeriria que ele fizesse antes do fim do mundo ?")
print(gemini_session.last.text)