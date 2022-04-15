public class example309 {
    public static void main(String[] args) {
        int total = 0; // --> 합을 넣어둘 변수 정의
        for(int i = 1; i <= 100; i++){ // --> 1~100까지 반복해가며 1을 더한다.
            if(i % 1 == 0 ||i % 2 == 0 || i % 5 == 0 || i % 6 == 0 || i % 7 == 0 || i % 8 == 0 || i % 9 == 0){ // --> 1, 2, 5, 6, 7, 8, 9의 배수 일 경우
                total += i; // --> 위 조건에 부합하는 수를 total에 숫자를 넣어둔다.
            }
            if(i % 3 == 0 || i % 4 == 0){ // --> 3, 4의 배수일 경우
                total -= i; // --> 위 조건에 부합하는 수를 total에서 빼준다.
            }
        }
        System.out.println("1부터 100 사이의 정수 중에서 3 또는 4의 배수가 아닌 수들의 합은: " + total);
    }
}
