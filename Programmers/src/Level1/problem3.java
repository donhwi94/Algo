package Level1;

// 프로그래머스 Level1 <완주하지 못한 선수>

import java.util.Arrays;

public class problem3 {

	public static String solution(String[] part, String[] com) {
		
		Arrays.sort(part); // 마라톤에 참여한 선수와,
		Arrays.sort(com);  // 마라톤을 완주한 선수 명단을 정렬한다
		
		for(int i=0 ; i<com.length ; i++){ // 루프를 돌면서 (완주 선수 명단이 참여 선수 명단의 길이보다 1 작다)
			if (!part[i].equals(com[i])){  // 정렬된 참여 선수 명단과 정렬된 완주 선수 명단을 비교했을 때, 선수 이름이 같지 않으면
				return part[i]; // 참여 선수 명단에서 해당 인덱스의 선수가 마라톤에 완주하지 못했으므로 리턴한다
			}
		}
		
		return part[part.length-1]; // 루프에서 리턴되지 못했다는 뜻은 정렬된 참여 선수 명단에서 마지막 선수가 완주 하지 못했음을 뜻하므로 리턴한다 
		
	}
	
	public static void main(String[] args) {
		// 입출력 예
		String[] participant = {"leo", "kiki", "eden"};
		String[] completion = {"eden", "kiki"};
		
		String ans = solution(participant, completion);
		
		System.out.println(ans);
	}

}
