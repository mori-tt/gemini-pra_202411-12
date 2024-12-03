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

while True:
  # LLMに対して送りたいプロンプトを指定
  prompt = input("プロンプトを入力してください。終了するにはexitを入力してください")
  if prompt.lower() == 'exit':
    print("プログラムを終了します")
    break
  if not prompt.strip():
    print("プロンプトが空です。再度入力してください")
    continue
  try:
    response = gemini.generate_content(prompt)
    print(response.text)
  except Exception as e:
    print(f"コンテンツの生成中にエラーが出ました:{e}")