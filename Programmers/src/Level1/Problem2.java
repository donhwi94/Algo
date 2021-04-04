package Level1;

// 프로그래머스  Level1 <크레인 인형뽑기 게임> (2019 카카오 개발자 겨울 인턴십) 

import java.util.Stack;
import java.util.ArrayList;

public class Problem2 {
	
	public static int solution(int[][] board, int[] moves){
		int answer = 0;
		
		ArrayList<Stack> ary = new ArrayList<Stack>();
		Stack<Integer> stack;
		Stack<Integer> basket = new Stack<Integer>();
		
		// 격자 만들기
		for(int i=0; i<board.length ; i++){
			stack = new Stack<Integer>();
			for(int j=board.length-1 ; j>=0 ; j--){
				if(board[j][i] != 0){
					stack.add(board[j][i]);
				}
			}
			ary.add(stack);
			//System.out.println(ary.get(0));
		}	
		
		int doll = 0; // 인형 
		
		for(int i=0 ; i<moves.length ; i++){
			int loc = moves[i]-1; // 크레인으로 뽑을 위치
			
			if(!ary.get(loc).isEmpty()){
				doll = (int)ary.get(loc).pop(); // 격자에서 인형을 뽑아서 
				basket.add(doll); // 바구니에 담음
				
				int index = basket.size() - 1;

				if(index != 0){ // 바구니에 인형이 두개 이상 들어있을 때, 
					if(basket.elementAt(index) == basket.elementAt(index-1)){ //같은 인형이 연속으로 있으면 
						basket.pop();
						basket.pop(); // 인형 두개를 없애고 
						answer += 2; // 두개가 터졌음을 카운팅
					}
				}
			}
			
		}
		
		return answer;
	}
	
	public static void main(String[] args) {
		// 입출력 예
		int[][] board = {{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}};
		int[] moves = {1,5,3,5,1,2,1,4};
		
		int ans = solution(board, moves);
		
		System.out.println(ans);
		
	}

}
