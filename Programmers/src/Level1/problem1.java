package Level1;

import java.util.ArrayList;
import java.util.Arrays;

/* 프로그래머스 Level1 <두 개 뽑아서 더하기>
 * 배열로 리턴하라고 되어있어서 Arraylist를 배열로 변경하는 로직을 넣었는데,
 * 다른 사람들 풀이 보니까 리턴 타입을 변경해도 되는듯 하다.
*/

public class problem1 {

	private static int[] solution(int[] numbers){
		int[] answer;
		int[] check = new int[201]; // 두 수를 뽑아서 더했을 때, 만들 수 있는 수의 값의 범위는 0~200
        int result = 0;
        
        ArrayList<Integer> ans_list = new ArrayList<Integer>();
	        
        // 서로 다른 인덱스에 있는 두 개의 수를 더한다
        for(int i=0 ; i<numbers.length-1; i++){
            for(int j=i+1 ; j<numbers.length; j++){
                result = numbers[i] + numbers[j];
	                
                // 중복을 제거하기 위해서 체크 여부를 물어봄
                if(check[result] == 0){
                	ans_list.add(result); // 두 수를 뽑아 더해서 만든 수를 리스트에 추가
                	check[result] = 1; // 리스트에 추가했으면 해당 값이 리스트에 들어있음을 체크함 - 1:리스트에 있음, 0:리스트에 없음
                }
            }
        }
	        
	        // Arraylist를 배열로 변경
        answer = new int[ans_list.size()];
        for(int i=0 ; i<answer.length ; i++){
        	answer[i] = ans_list.get(i).intValue();
        }
			
        // 정렬
        Arrays.sort(answer);
	        
		return answer;
	}
	
	public static void main(String[] args) {
		// 입출력 예 
		int[] numbers = {2, 1, 3, 4, 1};
		int[] sol = solution(numbers);

		for(int i=0 ; i<sol.length ; i++){
			System.out.print(sol[i] + " ");
		}	
	}
	
}
