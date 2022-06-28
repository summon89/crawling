import urllib.request as request
import urllib.parse
#주소 담기
API = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

#요청할 때 넘겨줄 파라미터를 딕셔너리 타입으로 처리할 경우
values = {"stnId" : "108"}
params = urllib.parse.urlencode(values)

#요청 url 완성
url = API + "?" + params
print(url)

data = request.urlopen(url).read()
text = data
print(text)



# urllib.request에 내장된 메서드
import urllib.request

response = urllib.request.urlopen("https://www.naver.com/")

"""
1. geturl() : 받아온 리소스의 URL를 반환받습니다.
2. info() : 패킷의 메타 데이터(헤더 등)를 반환받습니다.
3. getcode() : 응답 패킷의 HTTP 상태 코드를 반환받습니다.
4. read() : 받아온 데이터를 바이트형으로 반환받습니다.
5. readline() : 받아온 데이터를 바이트형으로 한 줄씩 반환받습니다.
6. close() : 연결된 요청을 닫습니다.
"""



# 1 받아온 리소스의 URL을 반환
# print(response.geturl())

# 2 패킷의 메타 데이터(헤더 등)를 반환받습니다.
# print(response.info())


# 3 응답 패킷의 HTTP 상태 코드를 반환
# print(response.getcode())
# 200 = OK
# https://www.w3schools.com/tags/ref_httpmessages.asp

# 4 받아온 데이터를 바이트형으로 반환
# print(response.read())
# HTML 코드로 인코딩
# rep = response.read()
# print(rep.decode())
# print(response.read().decode())


# # 5 받아온 데이터를 바이트형으로 한 줄씩 반환
# print(response.readline())
# print(response.readline())
# print(response.readline())
# print(response.readline())

# # 6 연결된 요청을 닫음
response.close()




