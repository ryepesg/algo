import java.util.Random;

import java.security.SecureRandom

class A {
    public static void main(String[] args) {
      Random rn = new Random(100);
      System.out.println(rn.nextInt(10));
      System.out.println(rn.nextInt(10));
      System.out.println(rn.nextInt(10));
      System.out.println(rn.nextInt(10));
    }
}
