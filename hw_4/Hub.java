package kjhoar.hw4;

import algs.hw4.map.FilterAirport;
import algs.hw4.map.FlightMap;
import algs.hw4.map.Information;
import edu.princeton.cs.algs4.BreadthFirstPaths;

public class Hub {
	
	//create a method that takes in Information and returns the hubs within the airline
	public static void hubFinder(Information info) {
		for (int i = 0; i < info.graph.V(); i++) {
			if(info.graph.degree(i) > 75) {
				System.out.println(info.labels.get(i) + "\t" + info.graph.degree(i));
			}
		}
	}
	
	
	public static void main(String[] args) {
		
		FilterAirport justLower48 = new FilterLower48();
		
		System.out.println("DELTA");
		Information delta = FlightMap.undirectedGraphFromResources("delta.json", justLower48);
		hubFinder(delta);
		
		System.out.println("SOUTHWEST");
		Information southwest = FlightMap.undirectedGraphFromResources("southwest.json", justLower48);
		hubFinder(southwest);
	}
}
