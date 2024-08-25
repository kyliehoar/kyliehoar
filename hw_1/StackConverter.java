package kjhoar.hw1;

import algs.days.day03.FixedCapacityStack;

// take a stack of values and return an array of those values, in order from oldest to youngest, while ensuring that when done the original stack is reconstituted as it was

public class StackConverter {

	public static int[] toArray(FixedCapacityStack<Integer> stack) {
		int sum = 0;
		for (int num : stack) {
			sum += 1;
			}
		int[] array = new int[sum];
		for (int num: stack) {
			if (stack.isEmpty()) {
				array[0] = num;
			}
			else {
				int i;
				for (i = sum - 1; i > 0; i--) {
					int oldnum = array[i - 1];
					array[i] = oldnum;
					}
				array[0] = num;
			}
		}
		return array;
	}
	
	public static void main(String[] args) {
		FixedCapacityStack<Integer> stack = new FixedCapacityStack<>(256);
		stack.push(926);
		stack.push(415);
		stack.push(31);
		
		int vals[] = StackConverter.toArray(stack);
		System.out.println("The following output must be [926, 415, 31] :" + java.util.Arrays.toString(vals));

		// note that you can still pop values
		System.out.println("shoud be 31:" + stack.pop());
		System.out.println("shoud be 415:" + stack.pop());
		System.out.println("shoud be 926:" + stack.pop());
	}
}
