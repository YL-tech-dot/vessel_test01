# AidsToNavigationReport
import asyncio
import pandas as pd
import websockets
import json
from datetime import datetime, timezone, timedelta
import os
import AisFilter as AisF
# import pandas as pd


# 데이터 저장을 위한 리스트 초기화
time_ls = []
ship_ls = []
lati_ls = []
long_ls = []
AisVersion  = []
CallSign    = []
Destination = []
DAESAN      = []
Dimension   = []
nara = ''
userid_lr = []
check_country_lr = []
message_lr= []
message_type_lr = []
meta_data_lr = []

# 예시 type_tag 리스트
type_tag = ['PositionReport', 'ShipStaticData', 'AidsToNavigationReport']

def label(tag):
    """주어진 태그가 type_tag에 포함되면 해당 태그를 반환"""
    if tag in type_tag:
        return tag
    return None  # 일치하는 태그가 없으면 None 반환


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

def export_to_txt(file_path,data):
    with open(file_path,"w") as file:
        message, message_type =data
        file.write(f'{str(message)}\n{str(message_type)}')

def check_country(mmsi):
    mmsi_str = str(mmsi)  # MMSI를 문자열로 변환
    if len(mmsi_str) != 9:
        return "Invalid MMSI: Must be 9 digits"

    prefix = mmsi_str[:3]  # 첫 3자리 추출

    country_mapping = {
        "410": "Philippines",
        "440": "South Korea",
        "441": "South Korea",
        "445": "North Korea",
        "412": "China",
        "413": "China",
        "416": "Taiwan",
        "453": 'Macao(china)',
        "477": "HongKong",
        "431": "Japan",
        "432": "Japan",
    }
    country = country_mapping.get(prefix)
    if country is None:
        return "Unknown Country"
    else:
        return country


async def connect_ais_stream():

    async with websockets.connect("wss://stream.aisstream.io/v0/stream") as websocket:
        subscribe_message = {"APIKey": "68ca2b02bc2cee4517be26272068c21c2b531762",
                             "BoundingBoxes": [[[38.859060, 120.754362], [32.720284, 127.647443]]],
                             "FilterShipMMSI":[440113700],
                             # "FilterMessageTypes": ["AidsToNavigationReport"]
                             }

        subscribe_message_json = json.dumps(subscribe_message)
        await websocket.send(subscribe_message_json)

        async for message_json in websocket:
            message = json.loads(message_json)
            message_type = message["MessageType"]
            meta_data = message["MetaData"]
            ais_message = message['Message'].get(label(message_type))

            # Printing 함수들
            AisF.printing(message, "message")
            AisF.printing(message_type,"message_type")
            AisF.printing(meta_data, "meta_data")
            AisF.printing(ais_message, "ais_message")

            if ais_message:
                if 'UserID' in ais_message:
                    userid = ais_message['UserID']
                    # print(userid)
                else:
                    pass

                userid_lr.append(check_country(userid))
                message_lr.append(message)
                message_type_lr.append(message_type)
                meta_data_lr.append(meta_data)

                if len(userid_lr) >= 10:
                    break

            #     #한국시간
            #     korea_time = datetime.now(timezone.utc) + timedelta(hours=9)
            #     formatted_time = korea_time.isoformat()


        # export_to_txt(get_next_filename(base_name='messages_test', extension='.txt', directory='export_txt'), mount)
        korea_time = datetime.now(timezone.utc) + timedelta(hours=9)
        formatted_time = korea_time.isoformat()

        data_dict = {
            'KOR_Time':userid_lr[:19],
            'userID': userid_lr,
            'message': message_lr,
            'message_type': message_type_lr,
            'meta_data': meta_data_lr,
        }

        base_name = "messages_needFilter"  # 기본 이름
        extension = ".csv"  # 파일 형식
        directory = "./export_csv"

        'message': message_lr,
        'message_type': message_type_lr,
        'meta_data': meta_data_lr,



        df = pd.DataFrame(data_dict)
        df.to_csv(get_next_filename(base_name,extension, directory), index=True)
        print('export_csv 완료.')




if __name__ == "__main__":
    api_key = ""
    bounding_box = [[32.0,124.0]]
    asyncio.run(connect_ais_stream(api_key, bounding_box ))



#     print("=This is Printer===========================")
#     print('formatted_time',formatted_time)
#     print('ais_message', ais_message)
#     print("=print Ends ===============================")
#
#     # 데이터 리스트에 추가
#     time_ls.append(formatted_time)
#     ship_ls.append(ais_message['UserID'])
#     # lati_ls.append(ais_message['Latitude'])
#     # long_ls.append(ais_message['Longitude'])
#     AisVersion.append(ais_message['AisVersion'])
#     CallSign.append(ais_message['CallSign'])
#     Destination.append(ais_message['Destination'])
#     Dimension.append(ais_message['Dimension'])