import requests

def login(username, password):
  """로그인 기능을 구현하는 함수입니다.

  Args:
    username: 로그인할 아이디입니다.
    password: 로그인할 비밀번호입니다.

  Returns:
    로그인에 성공하면 True를, 실패하면 False를 반환합니다.
  """

  # 로그인 요청을 보냅니다.
  response = requests.post("http://localhost:8080/login",
                          data={"username": username, "password": password})

  # 응답 코드를 확인합니다.
  if response.status_code == 200:
    return True
  else:
    return False


if __name__ == "__main__":
  # 로그인 정보를 입력합니다.
  username = input("아이디를 입력하세요: ")
  password = input("비밀번호를 입력하세요: ")

  # 로그인을 시도합니다.
  if login(username, password):
    print("로그인에 성공했습니다.")
  else:
    print("로그인에 실패했습니다.")