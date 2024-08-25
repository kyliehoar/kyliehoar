package kjhoar.hw4;

import algs.hw4.map.FilterAirport;
import algs.hw4.map.FlightMap;
import algs.hw4.map.Information;
import edu.princeton.cs.algs4.AdjMatrixEdgeWeightedDigraph;
import edu.princeton.cs.algs4.DirectedEdge;
import edu.princeton.cs.algs4.FloydWarshall;

public class LongestOfShortest {
	
	//find a way to implement all pairs shortest distance here
	// find shortest path from accumulated edge weights between two vertices
	// Floyd Warshall needs to be implemented as well 
	
	// find the longest of all of the shortest trips
	// find the biggest value in a 2d array
	// by doing this we find the worst case
	
	public static void floydW (Information info, String name) {
		AdjMatrixEdgeWeightedDigraph adj = new AdjMatrixEdgeWeightedDigraph(info.graph.V());
		
		for(int i: info.positions.keys()) {
			for(int j: info.graph.adj(i)) {
				double dist = info.positions.get(i).distance(info.positions.get(j));
				
				adj.addEdge(new DirectedEdge(i, j, dist));
				adj.addEdge(new DirectedEdge(j, i, dist));
			}
		}
		
		FloydWarshall fwInfo = new FloydWarshall(adj);
		
		double longestOfShortest = 0.0;
		int longFrom = -1;
		int longTo = -1;
		double efficiencySum = 0.0;
		int countEfficient = 0;
		for(int i = 0; i < info.positions.size(); i++) {
			for(int j = i + 1; j < info.positions.size(); j++) {
				double directFlight = info.positions.get(i).distance(info.positions.get(j));
				if(fwInfo.hasPath(i, j)) {
					double distance = fwInfo.dist(i, j);
						if(distance > longestOfShortest) {
							longestOfShortest = distance;
							longFrom = i;
							longTo = j;
						}
					efficiencySum += (distance / directFlight);
					countEfficient++;
				}
			}
			
		}
		System.out.println(name + " : Total Flight Distance is " + longestOfShortest + " but airports are only " + info.positions.get(longFrom).distance(info.positions.get(longTo)) + " miles apart.");
		
		for (DirectedEdge i : fwInfo.path(longFrom, longTo)) {
			int from = i.from();
			int to = i.to();
			double distance = fwInfo.dist(from, to);
			System.out.println(info.labels.get(from) + " -> " + info.labels.get(to) + " for " + distance);
		}
		
		System.out.println("Average Efficiency: " + efficiencySum / countEfficient);
	}
	
	public static void main(String[] args) {
		
		FilterAirport justLower48 = new FilterLower48();
		Information delta = FlightMap.undirectedGraphFromResources("delta.json", justLower48);
		Information southwest = FlightMap.undirectedGraphFromResources("southwest.json", justLower48);
		Information test = FlightMap.undirectedGraphFromResources("test.json", justLower48);
		
		floydW(delta, "Delta");
		floydW(southwest, "Southwest");
		floydW(test, "Test");
		
	}
}
