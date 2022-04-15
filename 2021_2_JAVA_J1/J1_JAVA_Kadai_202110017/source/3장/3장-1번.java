/*
1. 다음의 작업을 수행하는 문장을 작성하라.
(1) 20 이상이고 60 미만이면 count를 증가한다.
(2) x와 y 중에서 큰 값을 max에 저장하고 작은 값을 min에 저장한다.
(3) x가 1부터 20 사이에 있으면 x의 값을 y에 대입한다.
(4) for 문을 사용하여서 무한 루프를 작성한다.
(5) while 문을 사용하여서 무한 루프를 작성한다.
 */

import java.util.Scanner;

public class example301 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("정수 입력");
        int n = 0, x = 0, y = 0;
        int max = 0, min = 0, count = 0;
        n = sc.nextInt();
        if (n >= 20 && n < 60) { // --> and 연산자를 이용해 n 값이 20 이상 60 미만일 경우를 측정
            count += 1;
        }

        System.out.print("x값 입력: ");
        x = sc.nextInt();
        System.out.print("y값 입력: ");
        y = sc.nextInt();
        if(x > y){ // --> x가 y보다 클때...
            max = x;
            min = y;
        }
        if(x < y){ // --> y가 x보다 클때...
            max = y;
            min = x;
        }
        if (x >= 1 && x <= 20){ // --> and 연산자를 이용해 x값이 1이상 20이하일 때
            y = x;
        }
        for (int i = 1; i > 0; i++){ // --> for 구문의 i 값이 0보다 큰 경우 실행한다. 첫항이 1이고 1씩 커지므로 무한 반복한다.
        }
        while(true) { // --> while 조건문이 True라면 실행하므로 무한히 실행한다.
        }
    }
}
