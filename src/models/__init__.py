import db_engine
from src.models.base_model import BaseModel
from src.models.sheet import Sheet

BaseModel.metadata.create_all(db_engine.client)
