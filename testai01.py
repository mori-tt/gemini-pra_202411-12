import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
# .envファイルからGOOGLE_API_KEYを読み込む
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
# APIキーを渡して設定しておく
genai.configure(api_key=GOOGLE_API_KEY)

# 利用するLLMを選択する
gemini = genai.GenerativeModel("gemini-1.5-flash-002")

# LLMに対して送りたいプロンプトを指定
prompt = "日本で2番目に高い山はどこで、標高は何メートルですか？"
# LLMのAPIに対してプロンプトを投げる→結果はresponseに入ってくる
response = gemini.generate_content(prompt)

# response.textを指定すると答えを表示できる
print(response.text)