# 프로그래머스 Level1 <신규 아이디 추천>
# 기존 코드에서 테스트 케이스 26건 중에 1건이 계속 실패함 ㅠㅠ 
# 3단계를 정규식으로 바꿈 

def solution(new_id):
  answer = ''
  valid = ["-", "_", "."]
  point = False
  point_num = 1
  index = 0

  answer = new_id.lower() #1단계 
  for a in answer:
    index = index + 1

    #2단계
    if not (a >= 'a' and a<= 'z') and a not in valid and not (a >= '0' and a<= '9'):
      answer = answer.replace(a, "")

    # 3단계 오류남
    # if a == '.': 
    #   if index == len(answer):
    #     point_num = point_num + 1
    #     answer = answer.replace("."*point_num, ".")
    #   else:
    #     if point:
    #       point_num = point_num + 1
    #     else:
    #       point = True
    # else: 
    #   answer = answer.replace("."*point_num, ".")
    #   point_num = 1  
    #   point = False

    #3단계 정규식 사용
    answer = re.sub("[\.]+",".",answer)

  #4단계
  answer = answer.lstrip(".")
  answer = answer.rstrip(".")
  
  #5단계
  if answer == "":
    answer = "a"

  #6단계 
  if len(answer) >= 16:
    answer = answer[:15]
  answer = answer.rstrip(".")

  #7단계
  if len(answer) <= 2:
    last = answer[-1]
    while len(answer) < 3:
      answer = answer + last

  return answer

new_id = "=.="
# new_id = "[][][][][][][][][][]."
answer = solution(new_id)
print(answer)
