import java.util.Scanner; // --> Scanner import

public class example216 {
    public static void main(String[] args) {
        double km, mile; // --> km, mile 변수 선언
        Scanner sc = new Scanner(System.in); // --> Scanner 객체 생성
        System.out.print("마일을 입력하시오: "); // --> 질문하기
        mile = sc.nextDouble(); // --> 받은 값을 mile로 넘기기

        km = mile * 1.609; // --> km 구하기
        System.out.print(mile + "마일은 " + km +"킬로미터입니다."); // --> 출력하기.

    }
}
