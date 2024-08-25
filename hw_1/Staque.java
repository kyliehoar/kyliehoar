package kjhoar.hw1;

import java.util.Arrays;

/**
 * A Staque is a unique structure that uses a single char array to provide both Stack and Queue behaviors.
 * 
 * You will need to add class attributes and some initialization code in the constructor.
 */
public class Staque {

	/** This contains the storage you will manage. */
	char storage[];
	final int separator;
	
	// YOU MAY ADD MORE CLASS ATTRIBUTES HERE
	int stackN;		// how many elements are in the stack
	int top;        // index position of the 'length char' of top most element in stack
					// note: when top == separator STACK MUST BE EMPTY
	int first;      // note: when first == separator QUEUE MUST BE EMPTY
	int last;       // note: when last == separator + 1 QUEUE MUST BE FULL
	int queueN;
	
	/**
	 * Create the internal storage array to contain 2*size + 1 bytes.
	 * 
	 * @param size  The number of bytes to use for the stack (or the queue).
	 */
	public Staque(int size) {
		if (size < 5 || size > 65536) {
			throw new RuntimeException("Invalid Size: " + size);
		}

		storage = new char[2*size+1];
		separator = size;  // this is the midpoint.
		
		// YOU MAY ADD MORE HERE
		top = separator; // hey stack is empty
		
		first = last = separator;
	}
	
	/** Returns whether the Staque has at least one element in its stack. */
	public boolean canPop() {
		if (top == separator) { return false; }
		else { return true; }
	}
	
	/** Returns whether the Staque has at least one element in its queue. */
	public boolean canDequeue() {
		throw new RuntimeException("canDequeue needs to be completed.");
	}

	/** Returns whether there is enough memory to push the char[] array to its stack. */
	public boolean canPush(char[] bytes) {
		if (top < bytes.length) { return false; }
		else { return true; }	
	}
	
	/** Returns whether there is enough memory to enqueue the char[] array to its queue. */
	public boolean canEnqueue(char[] bytes) {
		if (storage.length - last + 1 > bytes.length) { return true; }
		else { return false;}
	}

	/**
	 * Push char[] array onto the stack.
	 * 
	 * @param bytes -- an array of bytes at least 1 in length but no more than 255.
	 * @exception RuntimeException if not enough room to store.
	 */
	void push(char bytes[]) {
		if (!canPush(bytes)) {throw new RuntimeException("Stack is unable to add bytes");}
		
		int start = top - 1;
		for (int i = bytes.length - 1; i >=0; i--) {
			storage[start--] = bytes[i];
		}
		
		storage[start] = (char) bytes.length;
		
		top = top - 1 - bytes.length;
		
		stackN++;
	}

	/** Helper method to push a single character. LEAVE AS IS. */
	void push(char ch) {
		push(new char[] { ch });
	}
	
	/**
	 * Pop the char[] array that is at the top of the stack and return it.
	 * 
	 * @return -- an array of bytes at least 1 in length but no more than 255.
	 * @exception RuntimeException if stack was empty.
	 */
	char[] pop() {
		if (!canPop()) {throw new RuntimeException("Stack is unable to pop");}
		
		char[] bytes;
		
		int length = storage[top];
		storage[top] = 0;
		bytes = new char[length];
		
		int start = top + 1;
		for (int i = 0; i < length; i++) {
			bytes[i] = storage[start];
			storage[start++] = 0;        
		}
		
		top = top + 1 + length;
		
		stackN--;
		
		return bytes;
	}
	
	/**
	 * Enqueue char[] array to tail of the queue.
	 *  
	 * @param bytes -- an array of bytes at least 1 in length but no more than 255.
	 * @exception RuntimeException if not enough room to store.
	 */
	void enqueue(char bytes[]) {
		if (!canEnqueue(bytes)) {throw new RuntimeException("Queue is unable to accept bytes");}

		if (first == last) {
			first = last = separator + 1;
		}
		storage[last++] = (char) bytes.length;
		for (int i = 0; i < bytes.length; i++) {
			storage[last++] = bytes[i];
		}
		queueN++;
	}
	
	/** Helper method to enqueue a single character. LEAVE AS IS. */
	void enqueue(char ch) {
		enqueue(new char[] { ch });
	}
	
	/**
	 * Dequeue char[] array from the head of the queue.
	 *  
	 * @return -- array of bytes at least 1 in length but no more than 255.
	 * @exception RuntimeException if queue is empty.
	 */
	char[] dequeue() {
		//if (!canDequeue()) {throw new RuntimeException("Queue is unable to dequeue");}
		
		char[] bytes;
		
		int length = storage[first];
		storage[first] = 0;
		bytes = new char[length];
		
		int start = first + 1;
		
		for (int j = 0; j < length; j++) {
			bytes[j] = storage[start];
			storage[start++] = 0;
		}
		
		first = first + 1 + length;
		
		queueN--;
		
		return bytes;
	}
		
		/** Helper method to output storage. USE AS IS. */
		static void output(int frame, Staque stq, String note) {
			System.out.println(String.format("%5d:%s\t<%s>", frame, Arrays.toString(stq.storage), note));
		}
		
		/** Check if byte arrays are identical. USE AS IS. */
		static boolean same(char[] one, char[] two) {
			if (one.length != two.length) { return false; }
			for (int i = 0; i < one.length; i++) {
				if (one[i] != two[i]) { return false; }
			}
			return true;
		}
		
		/** Use as is to validate your implementation matches the output from the homework spec. */
		public static void main(String[] args) {
			System.out.println("Note that in the output, the encoded lengths may appear as a strange");
			System.out.println("character (like " + ((char) 7) + ") because of how characters appear.");
			System.out.println();
			
			Staque stq = new Staque(7);
			output(0, stq, "empty");
			
			char[] c1 = new char[] { 'M' };                    // these are char bytes[] to push/enqueue
			char[] c2 = new char[] { 'x', 'y' };
			char[] c3 = new char[] { 'a', 'b', 'c' };
			char[] c4 = new char[] { 'w', 'x', 'y', 'z' };
			
			stq.push(c3);
			output(1, stq, "pushed 3");
			
			stq.enqueue(c4);
			output(2, stq, "enqueued 4");
			
			stq.enqueue(c1);
			output(3, stq, "enqueued 1");
			
			stq.push(c2);
			output(4, stq, "pushed 2");
			
			char[] p1 = stq.pop();
			if (!same(p1,c2)) { throw new RuntimeException("Bytes pop'd didn't match!"); }
			
			char[] d1 = stq.dequeue();
			if (!same(d1,c4)) { throw new RuntimeException("Bytes dequeued didn't match!"); }
			
			output(5, stq, "pop'd and dequed");
		}
	}