package kjhoar.hw1;

import algs.days.day03.FixedCapacityStack;

// This function will construct a stack containing the digits (in base b) of n in reverse order such that the topmost value on the returned stack will be the leftmost digit representation of n in base b.

public class DigitRepresentation {

	static FixedCapacityStack<Integer> reverseRepresentation(int n, int b) {
		FixedCapacityStack<Integer> stack = new FixedCapacityStack<> (32);
		//int power = b;
		while (n > 0) {
			int digit = (n % b);
			stack.push(digit);
			n = n / b;
			//power = power * b;
		}
		return stack;
		//throw new RuntimeException ("Complete this implementation");
	}

	public static void main(String args[]) {
		System.out.println("b       21 in base b");
		System.out.println("--------------------");
		int N = 21;
		for (int b = 2; b <= 10; b++) {
			FixedCapacityStack<Integer> stack = reverseRepresentation(N, b);
			System.out.print(b + "       ");
			//StringBuilder sb = StringBuilder();
			//sb.append(N).append("in base").append(b).append("\n");
			while (!stack.isEmpty()) {
				System.out.print(stack.pop());
			}
			System.out.println();
			// FINISH THIS IMPLEMENTATION
		}
	}
}
