public class example303 {
    public static void main(String[] args) {
        int x = 3; // --> 변수 x를 3으로 초기화
        if (x >= 0) // -- > 만약에 x가 0보다 같거나 크다면...
            if (x == 0) // --> 만약에 x의 값이 0이라면....
                System.out.println("첫 번째 문자열"); // --> 위의 조건에 해당하는 경우 이 문장을 출력하여라
            else System.out.println("두 번째 문자열"); // --> x의 값이 위 조건에 해당하지 않는 경우 이 문장을 출력하여라
        System.out.println("세 번째 문자열"); // 4번째 줄의 조건과는 상관없이 문장을 출력 할 것이다.
    }
}
