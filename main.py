from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class KakaoRequest(BaseModel):
    userRequest: dict

@app.post("/kakao/chatbot")
async def kakao_chatbot(request: KakaoRequest):
    user_input = request.userRequest.get("utterance", "")
    response_text = f"'{user_input}'에 대한 추천 정보를 가져올게요!"
    return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": response_text}}]}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
