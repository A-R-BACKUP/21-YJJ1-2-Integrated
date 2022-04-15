public class example308 {
    public static void main(String[] args) {
        int x = 3; // --> 변수 x 선언 및 초기값 3으로 설정
        if (x >= 0) { // --> 만약에 x가 0보다 크거나 같다면...
            if (x == 0) { // --> 만약에 x가 0이라면...
                System.out.println("first"); // --> 위의 조건을 충족할 경우 first 문장을 출력한다.
            }
            else { // --> 이외의 경우라면...
                System.out.println("second"); // --> second 문장을 출력한다.
            }
        }
        System.out.println("third"); // --> 위 조건과 상관 없이 third 문장을 출력한다.
    }
}
