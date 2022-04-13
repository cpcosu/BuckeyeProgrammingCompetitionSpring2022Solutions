import java.util.*;
 
public class IncreasingPathZhur {
	
	// Private Static Methods Starts Here
	public static class Node{
		int x;
		int y;
		int sum;
		public Node(int x, int y, int sum){
			this.x = x;
			this.y = y;
			this.sum = sum;
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// Code Starts Here
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[][] grid = new int[m][n];
		for(int i = 0; i < m; i++) {
			for(int j = 0; j < n; j++) {
				grid[i][j] = sc.nextInt();
			}
		}
		LinkedList<Node> queue = new LinkedList<>();
		for(int i = 0; i < n; i++) {
			queue.add(new Node(0, i, grid[0][i]));
		}
		int[][] store = new int[m][n];
		int best = -1;
		while(!queue.isEmpty()) {
			Node node = queue.remove();
			ArrayList<Node> options = generate(node, grid, n, m);
			if(store[node.x][node.y] > node.sum) { // Prune else TLE
				continue;
			}
			if(options.isEmpty() && node.x == m - 1) {
				best = Math.max(best, node.sum);
			}else {
				for(Node op : options) {
					queue.add(op);
					store[op.x][op.y] = Math.max(store[op.x][op.y], op.sum);
				}
			}
		}
		System.out.println(best);
	}

	private static ArrayList<Node> generate(Node node, int[][] grid, int n, int m) {
		ArrayList<Node> options = new ArrayList<>();
		int x = node.x;
		int y = node.y;
		int sum = node.sum;
		int curr = grid[x][y];
		if(x == m - 1) { // bottom row
			if(0 <= y - 1 && curr < grid[x][y - 1]) { // left
				options.add(new Node(x, y - 1, sum + grid[x][y - 1]));
			}
			if(y + 1 < n && curr < grid[x][y + 1]) { // right
				options.add(new Node(x, y + 1, sum + grid[x][y + 1]));
			}
		}else {
			if(y == 0) { // Left wall
				if(y + 1 < n && curr < grid[x][y + 1]) { // right
					options.add(new Node(x, y + 1, sum + grid[x][y + 1]));
				}
				if(x + 1 < m && curr < grid[x + 1][y]) { // down
					options.add(new Node(x + 1, y, sum + grid[x + 1][y]));
				}
			}else if(node.y == n - 1) { // right wall
				if(0 <= y - 1 && curr < grid[x][y - 1]) { // left
					options.add(new Node(x, y - 1, sum + grid[x][y - 1]));
				}
				if(x + 1 < m && curr < grid[x + 1][y]) { // down
					options.add(new Node(x + 1, y, sum + grid[x + 1][y]));
				}
			}else { // middle
				if(0 <= y - 1 && curr < grid[x][y - 1]) { // left
					options.add(new Node(x, y - 1, sum + grid[x][y - 1]));
				}
				if(y + 1 < n && curr < grid[x][y + 1]) { // right
					options.add(new Node(x, y + 1, sum + grid[x][y + 1]));
				}
				if(x + 1 < m && curr < grid[x + 1][y]) { // down
					options.add(new Node(x + 1, y, sum + grid[x + 1][y]));
				}
			}
		}
		return options;
	}
 
}