# 프로그래머스 Level1 <완주하지 못한 선수>
# Counter 함수 대박
# 컨테이너에 동일한 자료가 몇개인지 딕셔너리 형태로 저장하고, 내림차순으로 정렬한다
# 두 개의 카운터를 빼거나 더할 수도 있다

from collections import Counter 

def solution(participant, completion):
  answer = ''
  answer = Counter(participant) - Counter(completion)

  return list(answer.keys())[0]

def main():
  participant = ["leo", "kiki", "eden"]
  completion = ["eden", "kiki"]

  print(solution(participant, completion))

main()