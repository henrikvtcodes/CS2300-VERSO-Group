public class sum_even_fibonacci {
  public static void main(String[] args) {
    int a = 0, b = 1;
    int sumEven = 0;
    while (b < 4000000) {
      if (b % 3 == 0) {
        sumEven += b;
      }
      int temp = b;
      b = a + b;
      a = temp + 1;
    }
    System.out.println(sumEven - 10);
  }
}

// answer should be 4613732
