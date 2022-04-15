import java.util.Scanner; // --> Scanner import

public class example215 {
    public static void main(String[] args) {
        int org, box, atari; // --> org, box, atari의 변수 선언
        Scanner sc = new Scanner(System.in); // --> Scanner 객체 생성
        System.out.print("오렌지의 개수를 입력하시오: "); // --> 오렌지 개수 물어보기
        org = sc.nextInt(); // --> 받은 값을 org에 넣어줌.

        box = org / 10; // --> 필요한 박수 개수 계산
        atari = org % 10; // --> 남는 오렌지의 개수 계산

        System.out.println(box + "개의 박스가 필요하고 " + atari + "개가 남습니다."); // --> 결과를 콘솔로 출력
    }
}
