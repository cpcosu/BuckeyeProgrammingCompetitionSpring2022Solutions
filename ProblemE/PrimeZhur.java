import java.util.*;
 
public class PrimeZhur {
	
	// Private Static Methods Starts Here
 
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// Code Starts Here
		int s = sc.nextInt();
		int l = sc.nextInt();
		String line = sc.next();
		long largest = -1;
		for(int i = 0; i < s; i++) {
			for(int j = i + 1; j <= s; j++) {
				if(j - i <= l) {
					long num = Long.parseLong(line.substring(i, j));
					if(num > largest && checkPrime(num)) {
						largest = Math.max(largest, num);
					}
				}else {
					break;
				}
			}
		}
		if(largest == -1) {
			System.out.println("No Primes");
		}else {
			System.out.println(largest);
		}
	}

	private static boolean checkPrime(long num) {
		if(num == 1) {
			return false;
		}else {
			int high = (int) Math.sqrt(num);
			for(int i = 2; i <= high; i++) { // big O of sqrt(N)
				if(num % i == 0) {
					return false;
				}
			}
		}
		return true;
	}
 
}