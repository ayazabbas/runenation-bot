import gspread
import pandas as pd
import logging
from oauth2client.service_account import ServiceAccountCredentials

logger = logging.getLogger()

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)

pd.set_option("display.max_colwidth", None)

levels = ["Novice", "Intermediate", "Proficient", "Advanced"]


def _get_player_info(sheet, rsn):
    logger.info(f"Getting {sheet} info for {rsn}")
    data = sheet.get_all_values()
    del data[-1]
    headers = data.pop(0)

    df = pd.DataFrame(data, columns=headers)
    player_info = df.loc[df["RSN"].str.lower() == rsn.lower()]

    if len(player_info.index) < 1:
        error = f'Player "{rsn}" not found on Google sheet.'
        return None, error
    elif len(player_info.index) > 1:
        error = f'Oops, multiple entries found for player "{rsn}"'
        return None, error

    return player_info, None


def cox(rsn, sheet):
    sheet = client.open("Mentor Log/Calendar").worksheet(sheet)
    player_info, error = _get_player_info(sheet, rsn)

    if error is not None:
        return error

    player_level = None
    for level in levels:
        if player_info.iloc[0][level] != "":
            if player_level is None:
                player_level = level
            elif levels.index(level) > levels.index(player_level):
                player_level = level

    if player_level is None:
        player_level = "None"

    player_info_final = pd.DataFrame(
        {
            "RSN": [rsn],
            "KC": [player_info.iloc[0]["KC"]],
            "Level": [player_level],
            "Notes": [player_info.iloc[0]["Notes for improvement:"]],
        }
    )

    response = ""
    for column in player_info_final.columns:
        response = response + f"\n{column}: {player_info_final.iloc[0][column]}"

    return response


def tob(rsn, sheet):
    sheet = client.open("Mentor Log/Calendar").worksheet("TOB")
    player_info, error = _get_player_info(sheet, rsn)

    if error is not None:
        return error

    verzik_verified = player_info.iloc[0]["Verzik Verification"] != ""
    verzik_tank = player_info.iloc[0]["Verzik Tank Capable"] != ""

    player_level = None
    for level in levels:
        if player_info.iloc[0][level] != "":
            if player_level is None:
                player_level = level
            elif levels.index(level) > levels.index(player_level):
                player_level = level

    if player_level is None:
        player_level = "None"

    player_info_final = pd.DataFrame(
        {
            "RSN": [rsn],
            "KC": [player_info.iloc[0]["KC"]],
            "Level": [player_level],
            "Verzik Verified": [verzik_verified],
            "Verzik Tank": [verzik_tank],
            "Last Session": [player_info.iloc[0]["Last session"]],
            "Notes": [player_info.iloc[0]["Notes for improvement:"]],
        }
    )

    response = ""
    for column in player_info_final.columns:
        response = response + f"\n{column}: {player_info_final.iloc[0][column]}"

    return response
