public class JAVA_20211029_1 {
    private int number;
    private String name;
    private int age;

    JAVA_20211029_1() {
        number = 100;
        name = "New Student";
        age = 18;
    }
    JAVA_20211029_1(int number, String name, int age) {
        this.number = number;
        this.name = name;
        this.age = age;
    }
    @Override
    public String toString() {
        return "Student [number="+ number +", name="+ name + ", age=" + age + "]";
    }
}