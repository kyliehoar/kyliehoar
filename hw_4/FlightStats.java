package kjhoar.hw4;

import java.util.Random;

import algs.hw4.map.FilterAirport;
import algs.hw4.map.FlightMap;
import algs.hw4.map.Information;

public class FlightStats {
		
	public static void flightStats(Information info, String name) {
			
		double numDistance = 0;
		double numFlights = 0;
		int longest = 0;
		int shortest = info.graph.V();
		String s = null;
		String t = null;
		String l = null;
		String m = null;
			
		for (int i = 0; i < info.graph.V(); i++) {
			for (int k: info.graph.adj(i)) {
				if (calculateDistance(info, i, k) > longest) {
					longest = (int) calculateDistance(info, i, k);
					l = info.labels.get(i);
					m = info.labels.get(k);
				}
				else if (calculateDistance(info, i, k) < shortest && calculateDistance(info, i, k) != 0) {
					shortest = (int) calculateDistance(info, i, k);
					s = info.labels.get(i);
					t = info.labels.get(k);
				}
				numDistance = numDistance + calculateDistance(info, i, k);
				numFlights++;
			}
		}
			
	// calculates the average distance of a flight
		double average = numDistance / numFlights;
			
	// print lines for the code
		System.out.println("Shortest flight for " + name + " is from " + s + " to " + t + " for " + shortest + " miles.");
		System.out.println("Longest flight for " + name + " is from " + l + " to " + m + " for " + longest + " miles.");
		System.out.println("Average " + name + " flight distance = " + average);
	}
		
	// make a helper function that does the GPS computations
	public static double calculateDistance(Information info, int u, int v) {
		return info.positions.get(u).distance(info.positions.get(v));
	}
	
	// make a method that creates a histogram of all flights
	public static void histGenerate(Information info) {
		Histogram hist = new Histogram();
		for (int i = 0; i < info.graph.V(); i++) {
			for (int k: info.graph.adj(i)) {
				if(i < k) {
					hist.record((int) calculateDistance(info, i, k));
				}
			}
		}
		hist.report(500);
	}

		
	public static void main(String[] args) {
			
		FilterAirport justLower48 = new FilterLower48();
			
		Information delta = FlightMap.undirectedGraphFromResources("delta.json", justLower48);
		Information southwest = FlightMap.undirectedGraphFromResources("southwest.json", justLower48);
		
		flightStats(delta, "Delta");
		System.out.println();
		flightStats(southwest, "Southwest");
		
		System.out.println();
		
		System.out.println("Delta Airlines: ");
		histGenerate(delta);
		
		System.out.println();
		
		System.out.println("Southwest Airlines: ");
		histGenerate(southwest);
		
		
	}

}
