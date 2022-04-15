public class example307 {
    public static void main(String[] args) {
        int sum1= 0; // --> 1번 문제의 sum1 변수 정의
        int i; // --> i 변수 정의
        for(i = 1; i <= 30; i++) // --> 30회 반복하며 반복 할때마다 + 1
            sum1 += i * i + 1; // --> (i^2 + 1)한 값을 sum1에 반복하며 누적 덧셈.
        System.out.println("1번 답: " + sum1); // --> 1번 답 출력

        int sum2=0; // --> 2번 문제의 sum2 변수 정의
        int x, y; // --> x, y 변수 정의
        for(x=1; x<=30; x++) // --> 30회 반복하며 반복 할때마다 + 1
            for(y=0; y<=5; y++) // --> 6회 반복하며 반복 할때마다 + 1
                sum2 += x*y; // --> x와 y값을 sum2에 반복하며 누적 덧셈
        System.out.println("2번 답: " + sum2); // --> 2번 답 출력
    }
}
