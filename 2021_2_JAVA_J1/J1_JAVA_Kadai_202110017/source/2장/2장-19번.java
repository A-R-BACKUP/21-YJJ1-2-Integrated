/*
섭씨 온도와 화씨 온도는 다음과 같은 수식을 만족한다. 섭씨 온도와 화씨 온도는 다음과 같은 수식을 만족한다.
사용자로부터 화씨 온도를 받아서 섭씨온도로 환산하여 출력하는 프로그램을 작성하시오.
 */

import java.util.Scanner; // --> Scanner import

public class example219 {
    public static void main(String[] args) {
        double c, f; // --> 섭씨와 화씨 변수 정의
        Scanner x = new Scanner(System.in); // --> Scanner 객체 생성
        System.out.print("화씨 온도를 입력하시오: "); // --> 화씨 온도 물어보기
        f = x.nextInt(); // --> 받은 입력 값을 화씨 변수로 넘기기
        c = (double)5 / (double)9 * (f - 32); // --> 화씨를 섭씨로 변환해 섭씨 변수로 넘기기
        System.out.println("섭씨 온도는: " + c); // --> 섭씨 온도 출력하기
    }
}
