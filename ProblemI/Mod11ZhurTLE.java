import java.math.BigInteger;
import java.util.*;
 
public class Mod11ZhurTLE {
	
	// Private Static Methods Starts Here
 
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// Code Starts Here
		int n = sc.nextInt();
		String line = sc.next();
		int half = n / 2;
		StringBuilder front = new StringBuilder(line.substring(0, half));
		for(int i = 0; i < n - half; i++) {
			front.append("0");
		}
		BigInteger first = new BigInteger(front.toString());
		BigInteger last = new BigInteger(line.substring(half));
		BigInteger eleven = new BigInteger("11");
		System.out.println(first.mod(eleven).add(last.mod(eleven)).mod(eleven));
		
	}
 
}