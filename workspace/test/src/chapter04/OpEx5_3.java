package chapter04;

public class OpEx5_3 {
	public static void main(String[] args) {
		int a = 10;
		int b = 0;
		
		// & 연산
		// System.out.println(b > 0 & (a / b) > 0); : 에러 - 왼쪽이 false, 오른쪽 연산에서 에러
		System.out.println(b > 0 && (a / b) > 0); // 오른쪽 연산이 에러지만 왼쪽이 false 이므로 출력
	}

}
