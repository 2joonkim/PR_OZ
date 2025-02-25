from fastapi import FastAPI, WebSocket,WebSocketDisconnect
from typing import List

app = FastAPI()

class ConnectionManager:
    """ WebSocket 연결 관리 """
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """ 클라이언트가 WebSocket 연결을 요청하면 리스트에 추가 """
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """ 클라이언트 연결 종료 시 리스트에서 제거 """
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        """ 모든 연결된 클라이언트에게 메시지 전송 """
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """ 클라이언트가 /ws 경로로 WebSocket 연결 요청 """
    await manager.connect(websocket)
    try:
        print(f"연결된 클라이언트 수: {len(manager.active_connections)}")
        while True:
            data = await websocket.receive_text()  # 클라이언트에서 데이터 수신
            await manager.broadcast(f"📢 새로운 알림: {data}")  # 모든 연결된 클라이언트에 전송
            print(f"클라이언트로부터 받은 메시지: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("클라이언트가 연결을 종료했습니다.")