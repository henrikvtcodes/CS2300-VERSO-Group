#include <iostream>

/**
 * @brief this function calculates the sum of all even fibonacci numbers
 *
 * @return an integer representing the sum of all even fibonacci numbers
 */
int main() {
  int a = 0, b = 1;
  int sum_even = 0;
  while (b < 4000000) {
    // fixed from b % 3
    if (b % 2 == 0) {
      sum_even += b;
    }
    int temp = b;
    b = a + b;
    // fixed from temp + 1
    a = temp;
  }
  std::cout << sum_even << std::endl;

  return 0;
}

// answer should be 4613732
