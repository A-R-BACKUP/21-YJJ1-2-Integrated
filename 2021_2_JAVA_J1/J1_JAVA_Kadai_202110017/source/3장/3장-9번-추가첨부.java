public class example309q {
    public static void main(String[] args) {
        int total = 0; // --> 합을 넣어둘 변수 정의
        for(int i = 1; i <= 100; i++){ // --> 1~100까지 반복해가며 1을 더한다
            if(i % 3 == 0 || i % 4 == 0){ // --> 3또는 4의 배수일 경우
                total += i; // --> total에 해당하는 숫자를 누적해서 더해준다
            }
        }
        System.out.println("1부터 100의 사이의 정수 중에서 3 또는 4의 배수인 수들의 합은: " + total);
    }
}
