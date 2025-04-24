from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    user_input = data.get("message")
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Mr.WOKE, a helpful and insightful AI."},
            {"role": "user", "content": user_input}
        ]
    )

    return {"reply": response.choices[0].message["content"]}
