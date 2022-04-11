package Problem15;

import java.util.Scanner;

public class sol {
	public static void main(String args[]){
		Scanner input = new Scanner(System.in);

		int w = input.nextInt();
		int h = input.nextInt();
		input.nextLine();

		String line = input.nextLine();

		for(int y = 0; y < h; y++){
			int start = y * w;
			int end = (y + 1) * w;

			if(start > line.length()) break;
			boolean stop = end > line.length();
			if(stop) end = line.length();

			System.out.println(line.substring(start, end));

			if(stop) break;
		}
	}
}
