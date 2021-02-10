from mongoengine import Document, BooleanField

class Parameters(Document):
    websocketActive = BooleanField(default=True)
