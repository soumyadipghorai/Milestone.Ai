from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from utils.web_socket_util import Manager
from config.logs import logger
from sqlalchemy.orm import Session
from models.database import get_db   
from utils.db_operations import * 
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/v1", tags=["notification service"])

@router.websocket("/ws/{role}")
async def websocket_endpoint(websocket: WebSocket, role: str):
    logger.info("opier")
    await Manager.connect(websocket, role)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        Manager.disconnect(websocket, role)

@router.get("/get_notifs/{role}")
def get_notifs(db: Session = Depends(get_db), role: str=''):
    try:
        unsent_notifs = (
            db.query(Notification)
            .filter(Notification.role == role)
            .order_by(Notification.created_at.desc())
            .all()
        )
        messages = []
        for notif in unsent_notifs:
            messages.append({"id": notif.id, "message": notif.content, "status": notif.status})
            notif.status = "sent"
        db.commit()
        return {"messages": messages}
    except Exception as e:
        logger.error(f"Error fetching notifications: {e}")
        return JSONResponse(status_code=500, content={"error": "Internal Server Error"})

@router.delete("/delete_notif/{id}")
def del_notifs(db: Session = Depends(get_db), id: str="") : 
    notif_to_del = db.query(Notification).filter(Notification.id == id).first()
    db.delete(notif_to_del)
    db.commit()
    return {"message":f"Succesfuly eleted notification with id {id}"}