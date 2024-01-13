from datetime import datetime

from sqlalchemy import insert
from sqlalchemy import update

from database.models import Base
from database.models import Predictions


class PredictionsQueries:
    @staticmethod
    def create_prediction(user_name: str, birthday: datetime) -> None:
        with Base.get_session() as s:
            s.execute(
                insert(Predictions).
                values(
                    name=user_name,
                    birthday=birthday
                ))
            s.commit()

    @staticmethod
    def update_prediction(uuid: str, text: str) -> None:
        with Base.get_session() as s:
            s.execute(
                update(Predictions).
                where(Predictions.uuid == uuid).
                values(text=text))
            s.commit()
