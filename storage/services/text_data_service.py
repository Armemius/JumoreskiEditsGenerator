from storage.base import SessionLocal
from storage.models.text_data_model import TextData


def insert_text_data(entry: TextData):
    session = SessionLocal()
    session.add(entry)
    session.commit()
    session.close()


def get_text_data_by_id(id: int) -> TextData:
    session = SessionLocal()
    entry = session.query(TextData).filter(TextData.id == id).first()
    session.close()
    return entry
