package Problem12;


import java.util.Scanner;

public class Sol{

	public static void main(String args[]){
		Scanner input = new Scanner(System.in);
		
		int a = input.nextInt();
		int b = input.nextInt();

		int total = a + a;

		int i = b - 1;
		int j = total - b + 1;

		int result = (i > j) ? j : i;

		float val = ((float) result) / (a * a);

		// System.out.println(val);

		int out = Math.round(val * 1000);

		System.out.println("" + out + "/1000");

		input.close();

	}
}