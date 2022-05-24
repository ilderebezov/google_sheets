from __future__ import annotations
from sqlalchemy import Column, BigInteger, DateTime, Numeric
from src.models.base_model import BaseModel
import db_engine
import datetime


class Sheet(BaseModel):
    """
    Data base model
    """
    __tablename__ = "google_sheets_table"

    Id = Column(BigInteger, primary_key=True, autoincrement=True)

    Number_col_A = Column(BigInteger)
    Order_number_col_B = Column(BigInteger)
    Cost_USD_col_C = Column(BigInteger)
    Delivery_time_col_D = Column(DateTime)
    Cost_RUB = Column(Numeric)

    @staticmethod
    def get_or_create(number: int = None,
                      order_number: int = None,
                      cost_usd: int = None,
                      delivery_time: datetime = None,
                      cost_rub: float = None,
                      ) -> Sheet:
        """

        :param number:
        :param order_number:
        :param cost_usd:
        :param delivery_time:
        :param cost_rub:
        :return:
        """

        instance = db_engine.session.query(Sheet).filter(Sheet.Number_col_A == number).first()

        if instance is None:
            instance = Sheet(
                Number_col_A=number,
                Order_number_col_B=order_number,
                Cost_USD_col_C=cost_usd,
                Delivery_time_col_D=delivery_time,
                Cost_RUB=cost_rub,
            )
            db_engine.session.add(instance)
            db_engine.protected_commit()
        return instance
