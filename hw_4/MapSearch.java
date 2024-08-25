package kjhoar.hw4;

import algs.days.day20.DepthFirstSearchNonRecursive;
import algs.hw4.map.GPS;
import algs.hw4.map.HighwayMap;
import algs.hw4.map.Information;
import edu.princeton.cs.algs4.BreadthFirstPaths;
import edu.princeton.cs.algs4.DijkstraSP;
import edu.princeton.cs.algs4.DirectedEdge;
import edu.princeton.cs.algs4.EdgeWeightedDigraph;

/**
 * Copy this class into USERID.hw4 and make changes.
 */
public class MapSearch {
	
	/** 
	 * This helper method returns the western-most vertex id in the Information, given its latitude and
	 * longitude.
	 * 
	 * https://en.wikipedia.org/wiki/Latitude
	 * https://en.wikipedia.org/wiki/Longitude
	 * 
	 */
	public static int westernMostVertex(Information info) {
		int westVertex = -1;
		double leastLong = 9999;
		for (int v = 0; v < info.graph.V(); v++ ) {
			GPS gps = info.positions.get(v);
			if (gps.longitude < leastLong) {
				westVertex = v;
				leastLong = gps.longitude;
			}
		}
		
		return westVertex;
	}

	/** 
	 * This helper method returns the western-most vertex id in the Information, given its latitude and
	 * longitude.
	 * 
	 * https://en.wikipedia.org/wiki/Latitude
	 * https://en.wikipedia.org/wiki/Longitude
	 * 
	 */
	public static int easternMostVertex(Information info) {
		int eastVertex = -1;
		double greatLong = -9999;
		for (int v = 0; v < info.graph.V(); v++) {
			GPS gps = info.positions.get(v);
			if(gps.longitude > greatLong) {
				eastVertex = v;
				greatLong = gps.longitude;
			}
		}
		
		return eastVertex;
	}

	public static void main(String[] args) {
		Information info = HighwayMap.undirectedGraphFromResources("USA-lower48-natl-traveled.tmg");
		int west = westernMostVertex(info);
		String westLabel = info.labels.get(west);
		GPS gpsWest = info.positions.get(west);
		int east = easternMostVertex(info);
		String eastLabel = info.labels.get(east);
		GPS gpsEast = info.positions.get(east);
		
		// DO SOME WORK HERE and have the output include things like this
		
		//Q3.1		
		BreadthFirstPaths bfs = new BreadthFirstPaths(info.graph, west);
		int BBB = bfs.distTo(east);
		double miles = gpsWest.distance(gpsEast);
		
		System.out.println("BreadthFirst Search from West to East:");
		System.out.println("BFS: " + west + "(" + westLabel + ") to " + east + "(" + eastLabel + ") has " + BBB + " edges.");
		System.out.println("BFS provides answer that is : " + miles + " miles.");
		
		//Q3.2
		DepthFirstSearchNonRecursive dfs = new DepthFirstSearchNonRecursive(info.graph, west);
		int DDD = 0;
		int last = -1;
		double mile = 0.0;
		for (int i : dfs.pathTo(east)) {
			if (last == -1) {
				last = i;
			}
			else {
				DDD++;
				mile += info.positions.get(i).distance(info.positions.get(last));
			}
		}
		
		System.out.println("DFS provides answer that is : " + mile + " miles with " + DDD + " total edges.");
		
		//Q3.3
		EdgeWeightedDigraph ewdi = new EdgeWeightedDigraph(info.graph.V());
		for(int i = 0; i < info.graph.V(); i++) {
			for(int j : info.graph.adj(i)) {
				if (i < j) {
					DirectedEdge de = new DirectedEdge(i, j, info.positions.get(i).distance(info.positions.get(j)));
					DirectedEdge ed = new DirectedEdge(j, i, info.positions.get(i).distance(info.positions.get(j)));
					ewdi.addEdge(de);
					ewdi.addEdge(ed);
				}
			}
		}
		DijkstraSP dsp = new DijkstraSP(ewdi, west);
		int SSS = 0;
		for (DirectedEdge i : dsp.pathTo(east)) {
			SSS++;
		}
		double distance = dsp.distTo(east);
		
		System.out.println("Shortest Distance via Dijkstra: " + distance +" miles with " + SSS + " total edges.");
	}
}
