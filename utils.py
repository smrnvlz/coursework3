import requests
from datetime import datetime
from pprint import pprint


def get_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "INFO: Данные получены успешно!\n"
        return None, f"ERROR: status_code: {response.status_code}\n"
    except requests.exceptions.ConnectionError:
        return None, "ERROR: requests.exceptions.ConnectionError\n"
    except requests.exceptions.JSONDecodeError:
        return None, "ERROR: requests.exceptions.JSONDecodeError\n"


def get_filtered_data(data, filtered_empty_from=False):
    data = [i for i in data if "state" in i and i["state"] == "EXECUTED"]
    if filtered_empty_from:
        data = [i for i in data if "from" in i]
    return data


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda i: i["date"], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_data(data):
    formatted_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]
        from_info, from_bill = "", ""
        if "from" in row:
            sender = row["from"].split()
            from_bill = sender.pop(-1)
            from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
            from_info = " ".join(sender)
        to = f"{row['to'].split()[0]} **{row['to'][-4:]}"
        operation_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"
        formatted_data.append(f"""\
{date} {description}
{from_info} {from_bill} -> {to}
{operation_amount}""")
    return formatted_data