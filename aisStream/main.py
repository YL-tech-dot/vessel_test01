import asyncio
import websockets
import json
from datetime import datetime, timezone, timedelta
import os
import pandas as pd


# 데이터 저장을 위한 리스트 초기화
time_ls = []
ship_ls = []
lati_ls = []
long_ls = []



def get_next_filename(base_name, extension, directory):
    if not os.path.exists(directory):
        os.makedirs(directory) #디렉토리가 없을시 생성
    i = 1
    while True:
        # 파일 이름 생성 (형식: base_name_01.csv)
        filename = f"{base_name}{i:02d}{extension}"
        full_path = os.path.join(directory, filename)
        if not os.path.exists(filename):
            return full_path # 기존에 중복명이 없다면 새로 만든 경로를 반환
        else:
            i += 1 # 중복된 이름이 있을 경우 숫자:i값을 늘린다.



async def connect_ais_stream():

    async with websockets.connect("wss://stream.aisstream.io/v0/stream") as websocket:
        subscribe_message = {"APIKey": "68ca2b02bc2cee4517be26272068c21c2b531762", "BoundingBoxes": [[[38.859060, 120.754362], [32.720284, 127.647443]]]}

        subscribe_message_json = json.dumps(subscribe_message)
        await websocket.send(subscribe_message_json)

        async for message_json in websocket:
            message = json.loads(message_json)
            message_type = message["MessageType"]

            if message_type == "PositionReport":
                # the message parameter contains a key of the message type which contains the message itself
                ais_message = message['Message']['PositionReport']
                # if len(ais_message) >= 10:
                #     break

                #한국시간
                korea_time = datetime.now(timezone.utc) + timedelta(hours=9)
                formatted_time = korea_time.isoformat()
                print(f"[{formatted_time}] ShipId: {ais_message['UserID']} Latitude: {ais_message['Latitude']} Longitude: {ais_message['Longitude']}")

                # 데이터 리스트에 추가
                time_ls.append(formatted_time)
                ship_ls.append(ais_message['UserID'])
                lati_ls.append(ais_message['Latitude'])
                long_ls.append(ais_message['Longitude'])
                if len(ship_ls) >= 10:
                    # 수집된 데이터 처리 후 종료
                    # 필요한 작업을 여기에 추가
                    break

        # 데이터프레임 생성 및 CSV 파일 저장
        data_dict = {
                'Timezone': time_ls,
                'ShipId': ship_ls,
                'Latitude': lati_ls,
                'Longitude': long_ls
            }
        # 설정값
        base_name = "ais_data_kor"  # 기본 이름
        extension = ".csv"  # 파일 형식
        directory = "./export_csv"

        df = pd.DataFrame(data_dict)
        df.to_csv(get_next_filename(base_name,extension, directory), index=True)
        print('export_csv 완료.')






if __name__ == "__main__":
    asyncio.run(connect_ais_stream())