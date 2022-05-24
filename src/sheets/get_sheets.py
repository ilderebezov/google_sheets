
import os

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def get_service_sacc():
    """
    Метод для чтения таблицы кот. выдан доступ
    для сервисного аккаунта приложения
    :return:
    """

    creds_json = os.path.dirname(__file__) + "/sacc1.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


def get_google_sheets():
    service = get_service_sacc()
    sheet = service.spreadsheets()

    sheet_id = "16LDqbvPer7YVfgyJpIKMbIyspqJLhbzsX44RqIbNGZU"

    resp = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=["Лист1"]).execute()
    return resp
