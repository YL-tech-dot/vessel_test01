import asyncio
import websockets
import json
from datetime import datetime, timezone
from shapely.geometry import Point, Polygon

# 중국 어선 MMSI의 접두사 목록
CHINESE_MMSI_PREFIXES = ['412', '413', '414']

# 한중 잠정 조치 수역 동측 한계선 좌표 (위도, 경도)
BOUNDARY_POINTS = [
    (32 + 11 / 60, 125 + 25 / 60),  # 차: 북위 32도 11분, 동경 125도 25분
    (33 + 20 / 60, 124 + 8  / 60),  # 카: 북위 33도 20분, 동경 124도 08분
    (34 + 0  / 60, 124 + 0  / 60 + 30 / 3600),  # 타: 북위 34도 00분, 동경 124도 00분 30초
    (35 + 0  / 60, 124 + 7  / 60 + 30 / 3600),  # 파: 북위 35도 00분, 동경 124도 07분 30초
    (35 + 30 / 60, 124 + 30 / 60),  # 하: 북위 35도 30분, 동경 124도 30분
    (36 + 45 / 60, 124 + 30 / 60),  # 거: 북위 36도 45분, 동경 124도 30분
    (37 + 0  / 60, 124 + 20 / 60),  # 너: 북위 37도 00분, 동경 124도 20분
    (32 + 11 / 60, 126 + 45 / 60)  # 바: 북위 32도 11분, 동경 126도 45분
]


async def connect_ais_stream(api_key, bounding_box):
    """AIS 스트림에 연결하고 데이터를 처리하는 함수"""
    try:
        async with websockets.connect("wss://stream.aisstream.io/v0/stream") as websocket:
            subscribe_message = create_subscription_message(api_key, bounding_box)
            await websocket.send(json.dumps(subscribe_message))
            print("Subscription message sent successfully.")

            progress_task = asyncio.create_task(display_progress())

            async for message_json in websocket:
                try:
                    message = json.loads(message_json)
                    vessel_data = parse_ais_data(message)
                    if vessel_data:
                        check_vessel_entry(vessel_data)
                except Exception as e:
                    print(f"Error while processing AIS message: {e}")

            progress_task.cancel()

    except Exception as e:
        print(f"Error while connecting to websocket: {e}")


def create_subscription_message(api_key, bounding_box):
    """AIS 스트림 구독 메시지 생성"""
    return {
        "APIKey": api_key,
        "BoundingBoxes": [bounding_box],
    }


async def display_progress():
    """진행 상태를 10초마다 출력"""
    while True:
        print(f"[{datetime.now(timezone.utc)}] Waiting for AIS data...")
        await asyncio.sleep(10)


def parse_ais_data(message):
    """AIS 메시지에서 선박 데이터를 추출"""
    try:
        metadata = message.get("MetaData", {})
        mmsi = metadata.get("MMSI")
        latitude = metadata.get("latitude")
        longitude = metadata.get("longitude")

        if not mmsi or not latitude or not longitude:
            raise ValueError("Invalid AIS data: Missing MMSI, latitude or longitude")

        return {
            "MMSI": mmsi,
            "latitude": latitude,
            "longitude": longitude
        }

    except KeyError as e:
        print(f"KeyError: {e} in AIS message.")
        return None
    except ValueError as e:
        print(e)
        return None


def is_chinese_vessel(mmsi):
    """MMSI 번호를 통해 중국 어선인지 여부를 판별"""
    return str(mmsi).startswith(tuple(CHINESE_MMSI_PREFIXES))


def point_in_polygon(lon, lat, boundary_points):
    """주어진 좌표가 경계선 내부에 있는지 확인"""
    point = Point(lon, lat)
    polygon = Polygon(boundary_points)
    return polygon.contains(point)


def check_vessel_entry(vessel_data):
    """선박 데이터를 통해 동측 한계선 진입 여부 확인"""
    mmsi = vessel_data['MMSI']
    latitude = vessel_data['latitude']
    longitude = vessel_data['longitude']

    inside_boundary = point_in_polygon(longitude, latitude, BOUNDARY_POINTS)

    if is_chinese_vessel(mmsi):
        if inside_boundary:
            log_entry(f"중국 어선 {mmsi} 이(가) 협정선 내로 진입했습니다.")
        else:
            log_entry(f"중국 어선 {mmsi} 이(가) 협정선 밖에 있습니다.")
    else:
        if inside_boundary:
            log_entry(f"제3의 국적 선박 {mmsi} 이(가) 협정선 내로 진입했습니다.")
        # 경계 밖에 있는 제3국 선박은 특별히 처리하지 않음


def log_entry(message):
    """로그 메시지를 출력"""
    print(f"[{datetime.now(timezone.utc)}] {message}")


if __name__ == "__main__":
    api_key = "8a9c8c36742443cb9b73c0af1d72cc214a197ad4"
    bounding_box = [[32.0, 124.0]]

    asyncio.run(connect_ais_stream(api_key, bounding_box))
