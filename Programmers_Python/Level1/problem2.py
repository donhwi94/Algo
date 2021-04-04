# Programmers level1 <크레인 인형뽑기 게임> (2019 카카오 개발자 겨울 인턴십)

def solution(board, moves):
  answer = 0
  basket = []

  for m in moves:
    for i in range(len(board)):
      if board[i][m-1] != 0:
        basket.append(board[i][m-1])
        board[i][m-1] = 0

        index = len(basket) - 1
        if index != 0:
          if basket[index] == basket[index-1]:
            basket.pop()
            basket.pop()
            answer = answer + 2

        break

  return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))