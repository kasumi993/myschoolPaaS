from channels.generic.websocket import WebsocketConsumer
import json

class CourseUpdateConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.group_name = "course_updates"
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        pass

    def course_update(self, event):
        message = event['message']
        self.send(text_data=json.dumps({'message': message}))
