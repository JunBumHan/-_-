import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.facebook.com/profile.php?id=1000053229801138" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["white", "black"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "남건우")
write("description", "대구중앙중학교 출신")
write("button", "페이스북")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "생년월일": "2007년 10월 22일",
  "좋아하는 것": "고양이",
  "싫어하는 것": "매운 음식",
  "한마디": "고양이는 세상에서 제일 귀여운 존재다"
}
information(informations)
