import java.util.*;
 
public class DictionaryZhur {
	
	// Private Static Methods Starts Here
 
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// Code Starts Here
		int n = sc.nextInt();
		HashSet<String> seen = new HashSet<>();
		HashSet<String> unseen = new HashSet<>();
		seen.add("");
		for(int i = 0; i < n; i++) {
			String word = sc.next();
			String definitionWords[] = sc.nextLine().split(" ");
			for(String w : definitionWords) {
				unseen.add(w);
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