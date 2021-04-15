
// 프로그래머스 Level1 <신규 아이디 추천> (2021 KAKAO BLIND RECRUITMENT)

import java.util.regex.Pattern;

public class Problem4 {

	public static String solution(String new_id) {
		String answer = "";
        
		// 1단계 
		new_id = new_id.toLowerCase();
		
		// 2단계 
		new_id = new_id.replaceAll("[^a-z0-9._-]", "");
		
		// 3단계 
		new_id = new_id.replaceAll("[.]+", ".");
	
		// 4단계
		if(new_id.length() > 0 && new_id.charAt(0) == '.') {
			new_id = new_id.substring(1, new_id.length());
		}
		if(new_id.length() > 0 && new_id.charAt(new_id.length()-1) == '.') {
			new_id = new_id.substring(0, new_id.length()-1);
		}
		
		// 5단계
		if(new_id.length() == 0) {
			new_id = "a";
		}
		
		// 6단계
		if(new_id.length() >= 16) {
			new_id = new_id.substring(0,15);
		}
		if(new_id.charAt(new_id.length()-1) == '.') {
			new_id = new_id.substring(0, 14);
		}
		
		// 7단계 
		if(new_id.length() <= 2) {
			String c = String.valueOf(new_id.charAt(new_id.length()-1));
			
			while (new_id.length() < 3) {
				new_id = new_id + c;
			}
		}
		
		answer = new_id;
		
		return answer;
	}
	
	public static void main(String[] args) {
		
		String answer = solution("abcdefghijklmn.p");
		System.out.println(answer);

	}

}
