
import pandas as pd
import plotly.express as px
from sqlalchemy import desc
import time

import db_engine
from src.models.sheet import Sheet
from src.sheets.get_sheets import get_google_sheets
from src.db_data.db_datas import get_db_data


def plot():
    """
    Plot graph based on google sheets data
    :return:
    fig_out - output graph
    df_graph - output table
    """
    res = get_google_sheets()
    res = res["valueRanges"]
    res = res[0]["values"]
    get_db_data(res)
    get_data_from_db = db_engine.session.query(Sheet).order_by(desc(Sheet.Delivery_time_col_D)).all()
    numbers = [num.Number_col_A for num in get_data_from_db]
    costs_usd = [cost.Cost_USD_col_C for cost in get_data_from_db]
    orders = [order.Order_number_col_B for order in get_data_from_db]
    y = [y.Cost_RUB for y in get_data_from_db]
    x = [x.Delivery_time_col_D.date() for x in get_data_from_db]

    data_graph = {'№': numbers, 'стоимость,$': costs_usd, 'заказ №': orders, 'срок поставки': x, 'стоимость,руб': y}

    df_graph = pd.DataFrame(data_graph)  # Create DataFrame with columns

    fig_out = px.line(df_graph, x="срок поставки", y="стоимость,руб",
                      labels={
                         "срок поставки": "Дата поставки",
                         "стоимость,руб": "стоимость, руб",
                      },
                      )
    return fig_out, df_graph
