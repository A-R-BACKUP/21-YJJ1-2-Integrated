/*
사용자로부터 구의 반지름을 입력 받아서 부피를 계산하여 출력하는 프로그램을 작성하라. 단 구의 반지름은 실수로 입력되며 출력도 모두 실수형으로 하여야 한다. 부피를 계산하는 수식은 다음과 같다.
 */

import java.util.Scanner; // --> Scanner import

public class example218 {
    public static void main(String[] args) {
        double r, v; // --> 반지름과 부피 변수 정의
        Scanner x = new Scanner(System.in); // --> Scanner 객체 생성
        System.out.print("구의 반지름을 입력하시오: "); // --> 구의 반지름 물어보기
        r = x.nextDouble(); // --> 받은 입력 값을 구의 반지름 변수로 넘기기
        v = (double)4 / (double)3 * Math.pow(r, 3); // --> 부피 구하기
        System.out.println("구의 부피는: " + v); // --> 구의 부피 출력하기
    }

}
