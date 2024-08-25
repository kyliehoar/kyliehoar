package kjhoar.hw4;

import algs.hw4.map.FilterAirport;
import algs.hw4.map.FlightMap;
import algs.hw4.map.Information;
import edu.princeton.cs.algs4.DepthFirstPaths;
import edu.princeton.cs.algs4.Queue;
import edu.princeton.cs.algs4.Stack;

public class Connected {
	
	//Implement DFSPaths here because you are not looking for efficiency - just looking to see if there is a path/if it is possible from KBOS
	//to every airport in the list for that airline
	//implement DFS code already created - no need to rewrite
	//find the airports that do not have connecting flights on airline "name" to Boston
	public static void paths(Information info, int v, String name) {
		
		int bos = getKBOS(info);
		DepthFirstPaths dfp = new DepthFirstPaths(info.graph, bos);
		Queue<Integer> storage = new Queue<Integer>();
		
		for (int i = 0; i < v; i++) {
			if (!dfp.hasPathTo(i)) {
				storage.enqueue(i);
			}
		}
		
		if(!storage.isEmpty()) {
			
			int airport1 = storage.dequeue();
			int airport2 = storage.dequeue();
			
			System.out.println("The name of the airline is " + name);
			System.out.println("The airports that cannot be reached from KBOS using " + name + " are:");
			System.out.println("AIRPORT- " + info.labels.get(airport1));
			System.out.println("AIRPORT- " + info.labels.get(airport2));
		}
	}
	
	//find the s that corresponds to Boston
	public static int getKBOS(Information info) {
		for (int s = 0; s < info.labels.size(); s++) {
			if(info.labels.get(s).equals("KBOS")) {
				return s;
			}
		}
		return 0;
	}
	
	public static void main(String [] args) {
		
		FilterAirport justLower48 = new FilterLower48();
		
		Information delta = FlightMap.undirectedGraphFromResources("delta.json", justLower48);
		paths(delta, delta.graph.V(), "Delta");
		
		Information southwest = FlightMap.undirectedGraphFromResources("southwest.json", justLower48);
		paths(southwest, southwest.graph.V(), "Southwest");

	}
	
	
}
