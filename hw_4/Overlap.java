package kjhoar.hw4;

import algs.hw4.map.FilterAirport;
import algs.hw4.map.FlightMap;
import algs.hw4.map.Information;

/**
 * Determines U.S. airports in the lower 48 that are served by Southwest but not Delta
 * 
 * return list of ICAO codes for the airports
 */
public class Overlap {
	
	// Compare the airports served by Delta and SW
	
	// Return a list of ICAO codes for the airports not served by SW ONLY
	public static void main(String[] args) {
		
		FilterAirport justLower48 = new FilterLower48();
		Information delta = FlightMap.undirectedGraphFromResources("delta.json", justLower48);
		Information southwest = FlightMap.undirectedGraphFromResources("southwest.json", justLower48);
		
		for (int s = 0; s < southwest.labels.size(); s++) {
			String sw = southwest.labels.get(s);
			boolean found = false;
			for (int d = 0; d < delta.labels.size(); d++) {
				String del = delta.labels.get(d);
				if (sw.equals(del)) {
					found = true;
				}
			}
			if (found == false) {
				System.out.println(sw);
			}
		}
	}

}
