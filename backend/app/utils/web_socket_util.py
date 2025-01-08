from typing import Dict, List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect 
from config.logs import logger

from models.db_models.app_services import Notification

from fastapi import APIRouter, HTTPException, Depends
from models.database import SessionLocal
from sqlalchemy.orm import Session

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, role: str):
        try:
            await websocket.accept()
            if role not in self.active_connections:
                self.active_connections[role] = []
            self.active_connections[role].append(websocket)
        except Exception as e:
            logger.error(f"web_socket_util:{str(e)}")

    def disconnect(self, websocket: WebSocket, role: str):
        if role in self.active_connections:
            self.active_connections[role].remove(websocket)

    async def send_message(self, to_role: str, message: str, milestone_id:str,db:Session=None):
        new_notif=Notification(role=to_role, content=message, status="pending",milestone_id=milestone_id)
        if to_role in self.active_connections:
            for connection in self.active_connections[to_role]:
                json_payload={
                    "id":new_notif.id,
                    "message":new_notif.content,
                    "status":new_notif.status,
                    "milestone_id":new_notif.milestone_id
                                }                
                await connection.send_json(json_payload)
                new_notif.status="sent"
        else:
            print(f"No active connections for role: {to_role}")
        await save_notification(notification=new_notif, db=db)
        logger.info("Notif saved to db")

async def save_notification(notification:Notification, db: Session = None):
    local_db = False
    if db is None:
        db = SessionLocal()
        local_db = True
    try:
        db.add(notification)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error saving notification: {e}")
    finally:
        if local_db:
            db.close()


Manager = ConnectionManager()


async def push_notification(to_role: str, message: str,milestone_id:str, db=None):
    await Manager.send_message(to_role, message,milestone_id, db=None)