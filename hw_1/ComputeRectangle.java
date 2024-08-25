package kjhoar.hw1;

import algs.hw1.fixed.*;
import algs.hw1.fixed.er.Location;
import algs.hw1.fixed.er.SearchForRectangle;
import algs.hw1.fixed.er.TrialEmbeddedRectangle;

/**
 * 
 * This method must return a {@link Location} object which records the (startr,startc,r,c) of the rectangle that you 
 * found within the EmbeddedRectangle.
 * 
 * For example, given an EmbeddedRectangle with 5 rows and 9 columns
 * might appear as below
 * 
 *    000000000
 *    000111110
 *    000111110
 *    000111110
 *    000111110
 *  
 * Your challenge will be to find the location of randomly generated rectangles within a Storage of suitable 
 * dimension. For the above Storage, your program should report (row=1, col=3, numRows=4, numCols=5).
 */

 public class ComputeRectangle implements SearchForRectangle {


	@Override
	public Location search(TwoDimensionalStorage rect) {
		
		// start r and c in middle of the big rectangle
		int r = rect.numRows / 2;
		int c = rect.numColumns / 2;
		
		// left side
		int low = 0;
		int high = rect.numColumns / 2;
		while (low <= high) {
			int mid = (high + low) / 2;
			if (rect.getValue(r, mid) == 1) {
				high = mid - 1; 
				}
			else {
				low = mid + 1;
			}
		}
		
		//left-most column (aka start column) is low
		int startc = low;
		
		low = rect.numColumns/2;
		high = rect.numColumns - 1;
		while (low <= high) {
			int mid = (high + low) / 2;
				if (rect.getValue(r, mid) == 1) {
					low = mid + 1;
				}
				else {
					high = mid - 1;
				}
		}
		//right-most column (aka last column) is high
		int endc = high;
		
		low = 0;
		high = rect.numRows / 2;
		while (low <= high) {
			int mid = (high + low) / 2;
			if (rect.getValue(mid, c) == 1) {
				high = mid - 1;
			}
			else {
				low = mid + 1;
			}
		}
		
		//top-most row (aka first row) is low
		int startr = low;
		
		low = rect.numRows / 2;
		high = rect.numRows - 1;
		while (low <= high) {
			int mid = (high + low) / 2;
			if (rect.getValue(mid, c) == 1) {
				low = mid + 1;
			}
			else {
				high = mid -1;
			}
		}
		
		//bottom-most row (aka last row) is high
		int endr = high;

		return new Location(startr, startc, endr - startr + 1, endc - startc + 1);
	}


	/** YOU DO NOT HAVE TO MODIFY THIS MAIN METHOD. RUN AS IS. */
	public static void main(String[] args) {
		// This code helps you evaluate if you have it working for a small example.
		int[][] values = new int[][] { 
			{ 0, 0, 0, 0, 0, 0, 0 },
			{ 0, 0, 1, 1, 1, 1, 1 },
			{ 0, 0, 1, 1, 1, 1, 1 },
			{ 0, 0, 1, 1, 1, 1, 1 },
			{ 0, 0, 1, 1, 1, 1, 1 },
		};
		TwoDimensionalStorage sample = new TwoDimensionalStorage(values);
		SearchForRectangle me = new ComputeRectangle();
		Location loc = me.search(sample);
		System.out.println("Location 1 2 4 5 should be: " + loc);

		// This code is used to ensure your code is robust enough to handle a small run.

		// compute and validate it works for small run.
		TrialEmbeddedRectangle.runSampleTrial(new ComputeRectangle());

		// compute and validate for large run. Your algorithm must significantly outperform this result.
		// When I ran my naive solution, the result was 1082400000. You need to do better!
		TrialEmbeddedRectangle.leaderBoard(new ComputeRectangle());
	}
}
