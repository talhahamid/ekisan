import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Notification

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def send_notification(self, event):
        message = event['message']

        # Send the message to the client
        await self.send(text_data=json.dumps({'message': message}))
