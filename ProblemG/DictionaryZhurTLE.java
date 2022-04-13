import java.util.*;
 
public class DictionaryZhurTLE {
	
	// Private Static Methods Starts Here
 
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// Code Starts Here
		int n = sc.nextInt();
		ArrayList<String> seen = new ArrayList<>();
		ArrayList<String> unseen = new ArrayList<>();
		seen.add("");
		for(int i = 0; i < n; i++) {
			String word = sc.next();
			String definitionWords[] = sc.nextLine().split(" ");
			for(String w : definitionWords) {
				if(!unseen.contains(w)) {
					unseen.add(w);
				}
			}
			seen.add(word);
		}
		for(String w : seen) {
			if(unseen.contains(w)) {
				unseen.remove(w);
			}
		}
		System.out.println(unseen.size());
	}
 
}