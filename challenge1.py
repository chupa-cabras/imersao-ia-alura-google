import google.generativeai as genai
import os
import dotenv

dotenv.load_dotenv()

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('Você é um criador de conteúdo para Youtube e Tiktok. O seu conteúdo é de entretenimento gamer. Seus vídeos são bem humorados e informátivos. Você é especialista em PNL, copy e skills semelhantes. Gostaria que me montasse um texto e roteiro sobre a Lore do game Helldivers2 para um vídeo de 3 minutos de forma comica e em um tom facista. Obrigado!')

print(response.text)