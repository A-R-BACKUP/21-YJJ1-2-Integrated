/*
받은 돈: 10000  --> a
상품의 총액: 7500  --> b
부가세: 750  --> c
잔돈: 2500  --> d

구입한 상품의 가격과 손님한테 받은 금액을 입력하면
부가세와 잔돈을 출력하는 프로그램을 작성하여 보자.
 */

import java.util.Scanner; // --> Scanner import

public class example217 {
    public static void main(String[] args) {
        int a, b, c, d; // --> 받은 돈, 상품의 총액, 부가세, 잔돈 변수 선언

        Scanner x = new Scanner(System.in); // --> Scanner 객체 생성
        System.out.print("받은 돈: "); // // --> 받은 돈 질문하기
        a = x.nextInt(); // 받은 입력 값 받은 돈 변수로 넘기기

        Scanner y = new Scanner(System.in); // --> Scanner 객체 생성
        System.out.print("상품의 총액: "); // --> 상품의 총액 질문하기
        b = y.nextInt(); // --> 받은 입력 값 상품의 총액 변수로 넘기기

        c = b / 10; // --> 부가세 계산기
        System.out.println("부가세: " + c); // --> 부가세 출력하기

        d = (a - b); // --> 잔돈 계산하기
        System.out.println("잔돈: " + d); // --> 잔돈 출력하기

    }
}
