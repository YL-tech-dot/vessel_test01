# ================Message type: PositionReport================
{
    'Message': { # AIS에서 수신된 메시지 정보를 담고 있는 객체
        'PositionReport': { # AIS 위치 보고서 (Position Report)
            'Cog': 55.7, # 지면 기준 선박의 진행 방향, Course over Ground (도 단위, 0~360도)
            'CommunicationState': 59916, # AIS 장비의 통신 상태를 나타내는 코드
            'Latitude': 26.388879999999997, # 선박의 위도
            'Longitude': 56.14770333333333, # 선박의 경도
            'MessageID': 1, # AIS 메시지 유형, 여기서는 1번 메시지 (Position Report)
            'NavigationalStatus': 0, # 항해 상태 (0 = 항해 중, 1 = 닻을 내림, 2 = 묶여 있음, 등)
            'PositionAccuracy': False, # 위치 정확도, False일 경우 10미터 이상 오차, True는 10미터 이내
            'Raim': False, # RAIM(Receiver Autonomous Integrity Monitoring) 유효성, False일 경우 RAIM 신호가 유효하지 않음
            'RateOfTurn': 0, # 선박의 회전 속도 (ROT), 0은 회전 없음, 양수는 우회전, 음수는 좌회전
            'RepeatIndicator': 0, # 메시지 반복 전송 횟수 (0은 처음 전송, 1 이상은 재전송)
            'Sog': 11.6, # 지면 기준 선박의 속도, Speed over Ground (노트 단위)
            'Spare': 0, # 예약된 필드 (해당 메시지에는 사용되지 않음)
            'SpecialManoeuvreIndicator': 0,  # 특별 기동 상태 (0 = 없음, 1 = 기동 중)
            'Timestamp': 42, # 메시지 전송 시각을 나타내는 타임스탬프 (AIS에서 초 단위로 전송)
            'TrueHeading': 54, # 진북 기준 선박의 진행 방향 (헤딩, 도 단위, 0~360도)
            'UserID': 229618000, # 선박의 MMSI (Maritime Mobile Service Identity, 고유 식별 번호)
            'Valid': True  # 메시지의 유효성 (True는 유효한 메시지)
        }
    },
    'MessageType': 'PositionReport',  # 메시지 유형, PositionReport는 위치 보고서
    'MetaData': {  # 추가적인 메타데이터 정보
        'MMSI': 229618000,  # 선박의 MMSI 번호 (고유 식별 번호)
        'MMSI_String': 229618000,  # MMSI 번호의 문자열 버전
        'ShipName': 'HYDRA               ',  # 선박의 이름, 여기서는 'HYDRA'
        'latitude': 26.388879999999997,  # 선박의 위도 (위치), PositionReport의 Latitude와 동일
        'longitude': 56.14770333333333,  # 선박의 경도 (위치), PositionReport의 Longitude와 동일
        'time_utc': '2024-09-27 00:19:44.21411417 +0000 UTC'  # 메시지 수신 시간 (UTC 기준)
    }
}
# =============================================================================
# ================Message type: StaticDataReport================
{
    'Message': {
        'StaticDataReport': {  # AIS 정적 데이터 보고서 (Static Data Report)
            'MessageID': 24,  # 메시지 유형 (24번 메시지는 Static Data Report)
            'PartNumber': False,  # 파트 번호 (AIS 메시지가 2개의 파트로 나눠지는 경우도 있음, 여기서는 False)
            'RepeatIndicator': 0,  # 메시지 반복 전송 횟수 (0은 처음 전송)
            'ReportA': {  # ReportA는 선박 이름 관련 정보 포함
                'Name': 'TA FA',  # 선박 이름
                'Valid': True  # 이 정보의 유효성
            },
            'ReportB': {  # ReportB는 선박의 다른 속성 정보 포함 (호출부호, 크기 등)
                'CallSign': '',  # 선박의 호출 부호 (여기서는 빈 값)
                'Dimension': {  # 선박의 크기 (A, B, C, D는 각 부분에 대한 치수)
                    'A': 0,  # 선박의 앞쪽에서 안테나까지의 거리
                    'B': 0,  # 선박의 뒤쪽에서 안테나까지의 거리
                    'C': 0,  # 선박의 왼쪽에서 안테나까지의 거리
                    'D': 0  # 선박의 오른쪽에서 안테나까지의 거리
                },
                'FixType': 0,  # 위치 고정 방식 (0은 위치가 고정되지 않음을 의미)
                'ShipType': 0,  # 선박 유형 (0은 미설정)
                'Spare': 0,  # 예약된 필드 (사용되지 않음)
                'Valid': False,  # 이 정보의 유효성 (False는 유효하지 않음을 의미)
                'VenderIDModel': 0,  # 공급업체 ID 모델
                'VenderIDSerial': 0,  # 공급업체 시리얼 번호
                'VendorIDName': ''  # 공급업체 이름 (여기서는 없음)
            },
            'Reserved': 0,  # 예약된 필드
            'UserID': 677037400,  # 선박의 MMSI (고유 식별 번호)
            'Valid': True  # 메시지의 유효성
        }
    },
    'MessageType': 'StaticDataReport',  # 메시지 유형 (정적 데이터 보고서)
    'MetaData': {
        'MMSI': 677037400,  # 선박의 MMSI
        'MMSI_String': 677037400,  # MMSI 번호의 문자열 버전
        'ShipName': 'TA FA',  # 선박 이름
        'latitude': 22.599813333333334,  # 선박의 위도 (위치)
        'longitude': 120.28171999999999,  # 선박의 경도 (위치)
        'time_utc': '2024-09-27 02:39:28.786098959 +0000 UTC'  # 메시지 수신 시간 (UTC 기준)
    }
}

# =============================================================================
# ================Message type: AidsToNavigationReport================
{
    'Message': {
        'AidsToNavigationReport': {  # 항해 보조물 관련 보고서 (AtoN, Aids to Navigation)
            'AssignedMode': False,  # 항해 보조물의 할당 모드 (False는 할당되지 않았음을 의미)
            'AtoN': 0,  # 항해 보조물(AtoN)의 유형
            'Dimension': {  # 항해 보조물의 크기
                'A': 0,  # AtoN의 앞쪽에서 위치까지의 거리
                'B': 0,  # AtoN의 뒤쪽에서 위치까지의 거리
                'C': 0,  # AtoN의 왼쪽에서 위치까지의 거리
                'D': 0  # AtoN의 오른쪽에서 위치까지의 거리
            },
            'Fixtype': 7,  # 위치 고정 방식 (7은 GNSS 위성 시스템을 사용)
            'Latitude': 12.576128333333333,  # AtoN의 위도
            'Longitude': 123.76131166666667,  # AtoN의 경도
            'MessageID': 21,  # 메시지 유형 (21번 메시지는 AtoN Report)
            'Name': 'ATON_TEST_1',  # AtoN의 이름
            'NameExtension': '',  # 이름 확장 (여기서는 없음)
            'OffPosition': False,  # AtoN이 원래 위치에 있는지 여부 (False는 원래 위치에 있음을 의미)
            'PositionAccuracy': True,  # 위치 정확도 (True는 정확함)
            'Raim': False,  # RAIM 유효성 (False는 유효하지 않음을 의미)
            'RepeatIndicator': 1,  # 메시지 반복 전송 횟수 (1은 재전송 중임을 의미)
            'Spare': False,  # 예약된 필드
            'Timestamp': 27,  # 메시지 전송 시각을 나타내는 타임스탬프
            'Type': 1,  # AtoN의 유형 (1은 특정 항해 보조물)
            'UserID': 990000001,  # AtoN의 MMSI (고유 식별 번호)
            'Valid': True,  # 메시지의 유효성
            'VirtualAtoN': True  # AtoN이 가상 항해 보조물임을 나타냅니다 (True는 가상 AtoN)
        }
    },
    'MessageType': 'AidsToNavigationReport',  # 메시지 유형, AtoN 보고서 (Aids to Navigation Report)
    'MetaData': {  # AIS 메시지의 부가적인 메타데이터
        'MMSI': 990000001,  # AtoN의 MMSI
        'MMSI_String': 990000001,  # MMSI의 문자열 버전
        'ShipName': 'B001-73%',  # 가상 항해 보조물의 이름
        'latitude': 12.576128333333333,  # AtoN의 위도
        'longitude': 123.76131166666667,  # AtoN의 경도
        'time_utc': '2024-09-27 02:39:28.875760364 +0000 UTC'  # UTC 기준 메시지 수신 시간
    }
}
# ================Message type: GnssBroadcastBinaryMessage================
{
    "Message": {
        "GnssBroadcastBinaryMessage": {  # GNSS (Global Navigation Satellite System) 관련 이진 메시지
            "Data": "\u0000\u0000\u0000\u0000...",  # GNSS 데이터를 이진 형식으로 포함. 위치 및 시간 정보 전송
            "Latitude": 26.93,  # 메시지에서 수신된 위도
            "Longitude": 50.50333333333333,  # 메시지에서 수신된 경도
            "MessageID": 17,  # 메시지 ID (AIS 메시지 타입 17)
            "RepeatIndicator": 0,  # 메시지 전송 횟수 (0 = 처음 전송)
            "Spare1": 0,  # 예약된 필드
            "Spare2": 0,  # 예약된 필드
            "UserID": 4033002,  # MMSI(고유 선박 식별 번호)
            "Valid": True  # 메시지 유효성 (True = 유효한 메시지)
        }
    },
    "MessageType": "GnssBroadcastBinaryMessage",  # 메시지 유형 (GNSS 이진 메시지)
    "MetaData": {  # 부가 메타데이터
        "MMSI": 4033002,  # MMSI 번호 (선박 고유 식별 번호)
        "MMSI_String": 4033002,  # 문자열 형태의 MMSI
        "ShipName": "",  # 선박의 이름 (없음)
        "latitude": 26.93005833333333,  # 선박의 위도
        "longitude": 50.503568333333334,  # 선박의 경도
        "time_utc": "2024-09-27 02:56:30.321496023 +0000 UTC"  # 메시지 수신 시간 (UTC 기준)
    }
}

# ================Message type: BaseStationReport================
{
    "Message": {
        "BaseStationReport": {  # 육상 기지국에서 수신된 보고 메시지
            "CommunicationState": 393222,  # 통신 상태 코드
            "FixType": 1,  # 위치 고정 방식 (1 = GPS)
            "Latitude": 22.409675,  # 기지국 위치의 위도
            "LongRangeEnable": False,  # 장거리 통신 가능 여부 (False = 비활성화)
            "Longitude": 114.12454833333332,  # 기지국 위치의 경도
            "MessageID": 4,  # 메시지 ID (AIS 메시지 타입 4)
            "PositionAccuracy": False,  # 위치 정확도 (False = 낮은 정확도)
            "Raim": False,  # RAIM 유효성 (False = 유효하지 않음)
            "RepeatIndicator": 0,  # 메시지 반복 횟수 (0 = 처음 전송)
            "Spare": 0,  # 예약된 필드
            "UserID": 2110000,  # 기지국의 MMSI
            "UtcDay": 27,  # UTC 기준의 일 (날짜)
            "UtcHour": 2,  # UTC 기준의 시 (시간)
            "UtcMinute": 56,  # UTC 기준의 분 (분)
            "UtcMonth": 9,  # UTC 기준의 월 (9월)
            "UtcSecond": 29,  # UTC 기준의 초 (29초)
            "UtcYear": 2024,  # UTC 기준의 연도 (2024년)
            "Valid": True  # 메시지 유효성 (True = 유효한 메시지)
        }
    },
    "MessageType": "BaseStationReport",  # 메시지 유형 (기지국 보고)
    "MetaData": {  # 부가 메타데이터
        "MMSI": 2110000,  # 기지국의 MMSI 번호
        "MMSI_String": 2110000,  # 문자열 형태의 MMSI
        "ShipName": "",  # 선박 이름 없음 (기지국이기 때문)
        "latitude": 22.409675,  # 기지국의 위도
        "longitude": 114.12454833333332,  # 기지국의 경도
        "time_utc": "2024-09-27 02:56:30.485636946 +0000 UTC"  # 메시지 수신 시간 (UTC 기준)
    }
}

# ================Message type: UnknownMessage================
{
    "Message": {
        "UnknownMessage": {}  # 내용이 없는 미확인 메시지
    },
    "MessageType": "UnknownMessage",  # 메시지 유형 (알 수 없는 메시지)
    "MetaData": {  # 부가 메타데이터
        "MMSI": 356993000,  # MMSI (이 메시지와 관련된 선박의 고유 식별 번호)
        "MMSI_String": 356993000,  # 문자열 형태의 MMSI
        "ShipName": "SHUN DA",  # 선박 이름
        "latitude": 23.482633333333336,  # 선박의 위도
        "longitude": 118.14563333333334,  # 선박의 경도
        "time_utc": "2024-09-27 02:56:30.554713435 +0000 UTC"  # 메시지 수신 시간 (UTC 기준)
    }
}

# ================Message type: AssignedModeCommand================
{
    "Message": {
        "AssignedModeCommand": {  # 할당된 모드 명령 메시지
            "Commands": {  # 명령 세부 정보
                "0": {
                    "DestinationID": 574000510,  # 명령 대상 선박의 MMSI
                    "Increment": 0,  # 명령에 따른 증분 (여기서는 없음)
                    "Offset": 200,  # 명령의 오프셋 값
                    "Valid": True  # 명령의 유효성
                },
                "1": {
                    "DestinationID": 574000510,  # 명령 대상 선박의 MMSI
                    "Increment": 0,  # 명령에 따른 증분 (없음)
                    "Offset": 200,  # 오프셋 값
                    "Valid": True  # 명령의 유효성
                }
            },
            "MessageID": 16,  # 메시지 ID (AIS 메시지 타입 16)
            "RepeatIndicator": 0,  # 메시지 반복 횟수 (0 = 처음 전송)
            "Spare": 0,  # 예약된 필드
            "UserID": 5741005,  # 명령을 보낸 선박의 MMSI
            "Valid": True  # 메시지 유효성
        }
    },
    "MessageType": "AssignedModeCommand",  # 메시지 유형 (할당 모드 명령)
    "MetaData": {  # 부가 메타데이터
        "MMSI": 5741005,  # MMSI 번호
        "MMSI_String": 5741005,  # 문자열 형태의 MMSI
        "ShipName": "",  # 선박 이름 없음
        "latitude": 10.583988333333334,  # 선박의 위도
        "longitude": 106.82788833333333,  # 선박의 경도
        "time_utc": "2024-09-27 02:56:30.556604521 +0000 UTC"  # 메시지 수신 시간 (UTC 기준)
    }
}

# ================Message type: StandardClassBPositionReport================
{
    "Message": {
        "StandardClassBPositionReport": {  # Class B 선박 위치 보고서
            "AssignedMode": False,  # 할당 모드 비활성화
            "ClassBBand": True,  # Class B 밴드 활성화
            "ClassBDisplay": False,  # Class B 디스플레이 비활성화
            "ClassBDsc": False,  # Class B 디지털 선택 호출(DSC) 비활성화
            "ClassBMsg22": True,  # 메시지 22 수신 여부 (True = 활성화)
            "ClassBUnit": True,  # Class B 단위 정보 (활성화됨)
            "Cog": 83.1,  # 지면 기준 선박의 진행 방향 (도 단위)
            "CommunicationState": 393222,  # 통신 상태 코드
            "CommunicationStateIsItdma": True,  # ITDMA 모드에서 통신 상태인지 여부
            "Latitude": 1.2769883333333332,  # 선박의 위도
            "Longitude": 103.91095166666668,  # 선박의 경도
            "MessageID": 18,  # 메시지 ID (AIS 메시지 타입 18)
            "PositionAccuracy": False,  # 위치 정확도 (False = 낮음)
            "Raim": False,  # RAIM 유효성 (False = 신호가 유효하지 않음)
            "RepeatIndicator": 0,  # 메시지 전송 횟수 (0 = 처음 전송)
            "Sog": 16.1,  # 지면 기준 선박의 속도, Speed over Ground (노트 단위)
            "Spare1": 0,  # 예약된 필드 1 (특별한 의미 없음)
            "Spare2": 0,  # 예약된 필드 2 (특별한 의미 없음)
            "Timestamp": 30,  # AIS 메시지의 타임스탬프 (초 단위)
            "TrueHeading": 511,  # 선박의 실제 진행 방향 (511은 방향을 알 수 없음을 의미)
            "UserID": 563066440,  # MMSI(고유 선박 식별 번호)
            "Valid": True  # 메시지 유효성 (True = 유효한 메시지)
        }
    },
    "MessageType": "StandardClassBPositionReport",  # 메시지 유형 (Class B 위치 보고서)
    "MetaData": {  # 부가적인 메타데이터 정보
        "MMSI": 563066440,  # 선박의 MMSI (고유 식별 번호)
        "MMSI_String": 563066440,  # MMSI의 문자열 형식
        "ShipName": "",  # 선박의 이름 (이 메시지에서는 이름이 없음)
        "latitude": 1.2769883333333332,  # 선박의 위도
        "longitude": 103.91095166666668,  # 선박의 경도
        "time_utc": "2024-09-27 02:56:30.616990467 +0000 UTC"  # UTC 기준 메시지 수신 시간
    }
}
