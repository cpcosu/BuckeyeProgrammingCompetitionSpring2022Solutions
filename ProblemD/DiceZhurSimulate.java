import java.util.*;
 
public class DiceZhurSimulate {
	
	// Private Static Methods Starts Here
 
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// Code Starts Here
		int n = sc.nextInt();
		int t = sc.nextInt();
		int numerator = 0;
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= n; j++){
				if(i + j == t){
					numerator++;
				}
			}
		}
		System.out.println(Math.round((double) numerator / (n * n) * 1000) + "/" + 1000);
		
	}
}
