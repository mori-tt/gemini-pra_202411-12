import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
# .envファイルからGOOGLE_API_KEYを読み込む
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
# APIキーを渡して設定しておく
genai.configure(api_key=GOOGLE_API_KEY)

# 利用するLLMを選択する
gemini = genai.GenerativeModel("gemini-1.5-flash-002")
picture = [{
    'mime_type': 'image/jpg',
    'data':Path('flower.jpg').read_bytes()#バイナリーデータとしてデータを取得
}]
prompt = "これは何という花ですか？"
response = gemini.generate_content(contents=[prompt,picture[0]])
print(response.text)