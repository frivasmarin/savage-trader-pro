from app import db
from datetime import datetime
from enum import Enum

class Alert(db.Model):
    """Model for storing alert history"""
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), default='UPST', nullable=False)
    # [Continúa con todos los modelos...]
