package kjhoar.hw1;

import algs.days.day03.FixedCapacityStack;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

//implementation of a calculator algorithm using two stacks to evaluate an expression, invented by Dijkstra

public class Evaluate {
	public static void main(String[] args) {
		FixedCapacityStack<String> ops = new FixedCapacityStack<String>(100);
		FixedCapacityStack<Double> vals = new FixedCapacityStack<Double>(100);

		while (!StdIn.isEmpty()) {
			// Read token. push if operator.
			String s = StdIn.readString();
			if (s.equals ("(")) { /* do nothing */ }
			else if (s.equals ("+")) { ops.push(s); }
			else if (s.equals ("-")) { ops.push(s); }
			else if (s.equals ("*")) { ops.push(s); }
			else if (s.equals ("/")) { ops.push(s); }
			else if (s.equals ("sqrt")) { ops.push(s); }
			else if (s.equals ("mod")) { ops.push(s); }
			else if (s.equals ("choose")) { ops.push(s); }
			else if (s.equals (")")) {
				// pop, evaluate, and push result if token is ")".
				String op = ops.pop();
				double v = vals.pop();
				if (op.equals("+")) { v = vals.pop() + v; }
				else if (op.equals("-")) { v = vals.pop() - v; }
				else if (op.equals("*")) { v = vals.pop() * v; }
				else if (op.equals("/")) { v = vals.pop() / v; }
				else if (op.equals("sqrt")) { v = Math.sqrt(v); }
				else if (op.equals("mod")) { v = vals.pop() % v; }
				else if (op.equals("choose")) {
					double p = vals.pop();
					v = factorial(p) / (factorial(v) * factorial(p - v));
				}
				vals.push(v);
			} else {
				// Token no operator or paren; must be double value to push
				vals.push(Double.parseDouble(s));
			}
		}
		
		StdOut.print(vals.pop());
		
		// set a breakpoint on this line and you can observe the state
		// of the ops stack and vals stack. You will need this for your 
		// answer.
		StdOut.println();
	}

	private static int factorial (double v) {
		int i;
		int total = 1;
		for (i = 1; i <= v; i++) {
			total = total*i;
		}
		return total;
	}
}

