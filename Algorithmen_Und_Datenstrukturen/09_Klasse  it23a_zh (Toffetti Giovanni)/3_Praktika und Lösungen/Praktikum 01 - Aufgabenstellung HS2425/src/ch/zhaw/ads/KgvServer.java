package ch.zhaw.ads;

public class KgvServer implements CommandExecutor {
    public int kgv(int a, int b) {
        return Math.abs(a * b) / ggt(a, b);
    }
    
    public int ggt(int a, int b) {
        while (b != 0) {
            int c = a % b;
            a = b;
            b = c;
        }
        return a;
    }

    @Override
    public String execute(String s) {
        String[] numbers = s.split("[ ,]+"); 
        int a = Integer.parseInt(numbers[0]); 
        int b = Integer.parseInt(numbers[1]); 
        return Integer.toString(kgv(a,b));
    }

}