
import db_engine
from src.models.sheet import Sheet
from datetime import datetime
from pycbrf import ExchangeRates


def get_db_data(res: str):

    db = db_engine.session.query(Sheet).all()

    if len(db) > len(res[1:]):
        get_numbers = db_engine.session.query(Sheet.Number_col_A).all()
        db_numbers = [number[0] for number in get_numbers]
        get_sheet_numbers = [int(number[0]) for number in res[1:]]
        numbers_difference = [item for item in db_numbers if item not in get_sheet_numbers]
        for element in numbers_difference:
            db_engine.session.query(Sheet).filter(Sheet.Number_col_A == element).delete()
            db_engine.protected_commit()
    now = datetime.now()
    rates = ExchangeRates(now, locale_en=True)
    for element in res[1:]:
        is_in_db = db_engine.session.query(Sheet).filter(Sheet.Number_col_A == int(element[0])).first()
        if is_in_db is None:
            delivery_time = datetime.strptime(element[3], '%d.%m.%Y').date()
            Sheet.get_or_create(number=int(element[0]),
                                order_number=int(element[1]),
                                cost_usd=int(element[2]),
                                delivery_time=delivery_time,
                                cost_rub=round(float(element[2]) * float(rates['USD'].value), 4))
        else:
            get_element = Sheet.get_or_create(number=int(element[0]))
            delivery_time = datetime.strptime(element[3], '%d.%m.%Y').date()
            if int(get_element.Order_number_col_B) != int(element[1]) or \
                    int(get_element.Cost_USD_col_C) != int(element[2]) or \
                    get_element.Delivery_time_col_D.date() != delivery_time:
                db_engine.session.query(Sheet). \
                    filter(Sheet.Number_col_A == element[0]). \
                    update({'Order_number_col_B': int(element[1]),
                            'Cost_USD_col_C': int(element[2]),
                            'Delivery_time_col_D': delivery_time,
                            'Cost_RUB': round(float(element[2]) * float(rates['USD'].value), 4)})
                db_engine.protected_commit()
