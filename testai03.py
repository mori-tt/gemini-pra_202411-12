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

conversation_history =[]#プロンプト内容とLLMからの回答を確保苦悩

while True:
    user_input = input("ユーザー")
    if user_input.lower() == "exit":
        print("プログラムを終了します")
        break
    if not user_input.strip():
        print("プロンプトがからです。再入力してください")
        continue 
    #ユーザーの入力内容を配列に格納する
    conversation_history.append(f"ユーザー:{user_input}")
    #{}内に変数の値を入れると展開される

    #配列から最後の10件を取得し、改行を使って繋いで一つの文章にした上で、改行し、　AI:という文字を追加する
    prompt = "\n".join(conversation_history[-10:])+"\nAI:"

    try:
        response = gemini.generate_content(prompt)

        #strip()を付けて、空白もじや改行を削除する
        ai_response = response.text.strip()

        #所得した返答を表示する
        print(f"AI:{ai_response}")

        #取得した返答を　AI:として配列に格納する
        conversation_history.append(f"AI:{ai_response}")
    
    except Exception as e:
        print(f"コンテンツの生成中にエラーが生じました:{(e)}")

