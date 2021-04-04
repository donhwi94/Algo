# 프로그래머스 Level1 <두 개 뽑아서 더하기>

def solution(numbers):
    answer = []
    
    result = 0
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            result = numbers[i] + numbers[j]
            if result not in answer:
                answer.append(result)
        
        answer.sort()
            
    return answer

def main():
  # 입출력 예
  numbers = [2, 1, 3, 4, 1]

  print(solution(numbers))

main()