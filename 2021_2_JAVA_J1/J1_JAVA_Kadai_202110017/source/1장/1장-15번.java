public class kadai15 {
    public static void main(String[] args) {

        // 별 다이아몬드의 상단부
        for(int i=1; i<=4; i++) {
            for (int j = 1; j <= 4 - i; j++) {
                System.out.print(" "); // 앞의 공백 부분
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("*"); // 만약에 i가 1이라면 별을 한개 찍어내고 i가 2라면 별을 두개 찍어낸다. 한마디로 한줄에 있어야 할 별의 2/3만큼 찍어낸다.
            }
            for (int j = 2; j <= i; j++) {
                System.out.print("*"); //나머지 별의 갯수만큼 찍어준다. i가 1이라면 찍어내지 않고 2라면 1개 찍어준다.
            }
            // i가 2일떄는 별 두개와 한개를 합쳐서 세개를 찍어낸다. 3일때는 별 세개와 두개를 합쳐서 찍어낸다.
            System.out.println(); // print는 줄바꿈이 포함되어 있지 않기 때문에 줄을 바꿔주기 위해 println을 한번 써준다.
        }
        // 그리고 이 반복을 네번 하겠다...

        //별 다이아몬드의 하단부
        for(int i=1; i<=3; i++) {
            for (int j = 0; j <= i-1; j++) {
                System.out.print(" "); // i가 1일때 j가 0이 되므로 공백을 한번 찍어준다. i가 2일때는 j가 1이 되므로 공백을 두번 찍어준다.
            }
            for (int j = 1; j <= 4-i; j++) {
                System.out.print("*"); // i가 1일때 별을 세번 찍어준다. i가 2일 떄에는 별을 두번 찍어준다.
            }
            for (int j = 3; j >= 1 + i; j--) {
                System.out.print("*"); // i가 1일때 별을 두번 찍어준다. i가 2일때는 별을 한번 찍어준다.
            }
            System.out.println(); // print는 줄바꿈이 포함되어 있지 않기 때문에 줄을 바꿔주기 위해 println을 한번 써준다.
        }
        // 이 반복을 세번 하겠다...
    }
}