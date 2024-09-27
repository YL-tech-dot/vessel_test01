# QGIS 프로그램으로
import requests

# 인증키와 WMS 파라미터 설정
api_key = 'YOUR_API_KEY'  # 여기에 실제 인증키를 입력하세요
wms_params = {
    'service': 'WMS',
    'version': '1.3.0',
    'request': 'GetMap',
    'key':'',
    'layers': 'your_layer_name',  # 요청할 레이어 이름
    'styles': '',
    'transparent':'True',
    'bbox': 'left,bottom,right,top',  # 좌표 범위
    'width': 800,  # 이미지 너비
    'height': 600,  # 이미지 높이
    'srs': 'EPSG:4326',  # 좌표 시스템
    'format': 'image/png',  # 출력 이미지 형식
    'domain':r'https://api.vworld.kr/req/wfs?key=652421D9-527C-3300-978B-5AC9224129C5&[WFS Param]'
}

# 요청 URL 생성
base_url = 'https://api.vworld.kr/req/wms'
url = f"{base_url}?key={api_key}&" + '&'.join([f"{key}={value}" for key, value in wms_params.items()])

# GET 요청 보내기
response = requests.get(url)

# 응답 처리
if response.status_code == 200:
    # 요청이 성공한 경우
    with open('output_map.png', 'wb') as f:
        f.write(response.content)
    print("지도 이미지가 저장되었습니다: output_map.png")
else:
    print(f"요청 실패: {response.status_code}, 내용: {response.text}")