from utils import get_data


def main():
    OPERATIONS_URL = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1676898376414&signature=5niRDR6y2gNOmDjD-sZjXaS_RkTbq5b7PUdZAHkFTA4&downloadName=operations.json"
    data = get_data(OPERATIONS_URL)


if __name__ == "__main__":
    main()
