/*10. 사용자가 입력한 값이 1, 2,... , 9이면 "ONE", "TWO",... , "NINE"와 같이 출력하는 프로 그램을 작성하라.
1부터 9사이가 아니면 “OTHER”를 출력한다.
 */

import java.util.Scanner; // --> Scanner import

public class example310 {
    public static void main(String[] args) {
        int number; // --> 넘버 변수 생성
        Scanner sc = new Scanner(System.in); // --> 스캐너 객체 생성

        System.out.print("정수를 입력하세요: "); // --> 정수값 물어보기
        number = sc.nextInt(); // --> 받은 정수 number 변수에 넣어줌

        switch(number) { // --> switch 문을 사용해서 받은 숫자마다 실행 할 작업을 작성한다.
            case 1: // --> 받은 값이 1일 경우
                System.out.println("ONE"); // --> ONE을 출력해준다.
                break; // --> 프로그램을 종료해준다.
            case 2: // --> 받은 값이 2일 경우
                System.out.println("TWO"); // --> TWO을 출력해준다.
                break; // --> 프로그램을 종료해준다.
            case 3: // --> 받은 값이 3일 경우
                System.out.println("THREE"); // --> THREE을 출력해준다.
                break; // --> 프로그램을 종료해준다.
            case 4: // --> 받은 값이 4일 경우
                System.out.println("FOUR"); // --> FOUR을 출력해준다.
                break; // --> 프로그램을 종료해준다.
            case 5: // --> 받은 값이 5일 경우
                System.out.println("FIVE"); // --> FIVE을 출력해준다.
                break; // --> 프로그램을 종료해준다.
            case 6: // --> 받은 값이 6일 경우
                System.out.println("SIX"); // --> SIX을 출력해준다.
                break; // --> 프로그램을 종료해준다.
            case 7: // --> 받은 값이 7일 경우
                System.out.println("SEVEN"); // --> SEVEN을 출력해준다.
                break; // --> 프로그램을 종료해준다.
            case 8: // --> 받은 값이 8일 경우
                System.out.println("EIGHT"); // --> EIGHT을 출력해준다.
                break; // --> 프로그램을 종료해준다.
            case 9: // --> 받은 값이 9일 경우
                System.out.println("NINE"); // --> NINE을 출력해준다.
                break; // --> 프로그램을 종료해준다.
            default: // --> 받은 값이 1~9 이외의 값인 경우
                System.out.println("OTHER"); // --> OTHER을 출력해준다.
                break; // --> 프로그램을 종료해준다.
        }
    }
}