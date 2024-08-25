package kjhoar.hw2;

/**
 * Responsible for allocating memory from within a designated block of chars.
 * 
 * Can reallocate memory (and copy existing chars to smaller or larger destination).
 * 
 * Can defragment available by combining neighboring regions together. ONLY possible if the blocks
 * of allocated memory appear in sorted order within the available list (worth five points on this question).
 * 
 * Can alert user that excess memory remains unfree'd
 * 
 * Address ZERO is always invalid.
 */
public class Memory {
	
	/** USE THIS StorageNode CLASS AS IS. */
	class StorageNode {
		int           addr;        // address into storage[] array
		int           numChars;    // how many chars are allocated
		
		StorageNode   next;        // the next StorageNode in linked list.
		
		/** Allocates a new Storage Node. */
		public StorageNode (int addr, int numChars) {
			this.addr = addr;
			this.numChars = numChars;
			this.next = null;
		}
		
		/** Allocates a new Storage Node and makes it head of the linked list, next. */ 
		public StorageNode (int addr, int numChars, StorageNode next) {
			this.addr = addr;
			this.numChars = numChars;
			this.next = next;
		}
		
		/** Helper toString() method. */
		public String toString() {
			return "[" + addr + " @ " + numChars + " = " + (addr+numChars-1) + "]";
		}
	}
	
	/** Storage of char[] that this class manages. */
	final char[] storage;
	private StorageNode available;
	private StorageNode allocated;
	private int numAvailable;
	
	// YOU CAN ADD FIELDS HERE
	
	public Memory(int N) {
		// memory address 0 is not valid, so make array N+1 in size and never use address 0.
		storage = new char[N+1];
		available = new StorageNode(1, N);
		allocated = null;
		numAvailable = N;

		// DO MORE THINGS HERE
	}
	
	/** 
	 * Make a useful debug() method.
	 * 
	 * You should print information about the AVAILABLE memory chunks and the ALLOCATED memory chunks.
	 * 
	 * This will prove to be quite useful during debugging.
	 */
	public String toString() {
		return "COMPLETE THIS IMPLEMENTATION";
	}
	
	/** 
	 * Report on # of StorageNode in allocated list (used for testing/debugging)
	 */
	public int blocksAllocated() {
		StorageNode n = allocated;
		int numAl = 0;
		while (n != null) {
			numAl++;
			n = n.next;
		}
		return numAl;
		
	}
	
	/** 
	 *  Report on # of StorageNode in available list (used for testing/debugging)
	 */
	public int blocksAvailable() {
		StorageNode n = available;
		int numAv = 0;
		while (n != null) {
			numAv++;
			n = n.next;
		}
		return numAv;
	}
	
	/** 
	 * Report on memory that was allocated but not free'd.
	 * Performance must be O(1).
	 */
	public int charsAllocated() {
		return storage.length - numAvailable - 1;
	}
	
	/** 
	 * Report on available memory remaining to be allocated.
	 * Performance must be O(1).
	 */
	public int charsAvailable() {
		return numAvailable;
	}
	
	/** 
	 * Return the char at the given address.
	 * Unprotected: can return char for any address of memory.
	  */
	public char getChar(int addr) {
		//validateAllocated(addr); [SORRY I INCLUDED THIS. YOU DON'T NEED TO DO THIS]
		return storage[addr];
	}
	
	/** 
	 * Get char[] at the given address for given number of chars, if valid.
	 * Unprotected: can return char[] for any address of memory.
	 * Awkward that you do not have ability to know IN ADVANCE whether this many
	 * characters are stored there, but a runtime exception will tell you.
	 */
	public char[] getChars(int addr, int numChars) {
		//validateAllocated(addr, numChars);  [SORRY I INCLUDED THIS. YOU DON'T NEED TO DO THIS]
		char[] target = new char[numChars];
		for(int i = 0; i < numChars; i++) {
			target[i] = getChar(addr++);
		}
		return target;
	}
	
	/** 
	 * Determines if the current address is valid allocation. Throws Runtime Exception if not. 
	 * Performance proportional to number of allocated blocks.
	 */
	void validateAllocated(int addr) {
		StorageNode Al = allocated;
		
		while (Al != null) {
			if (addr < Al.addr + Al.numChars) {
				return;
			}
			Al = Al.next;
		}
		throw new RuntimeException("Not found");
	}
	
	/** Determines if the current address is valid allocation for the given number of characters. */
	void validateAllocated(int addr, int numChar) {
		StorageNode Al = allocated;
		while (Al != null) {
			if(addr + numChar <= Al.addr + Al.numChars) {
				return;
			}
			Al = Al.next;
		}
		throw new RuntimeException("Not found");
	}
	
	/** 
	 * Internally allocates given memory if possible and return its starting address.
	 * 
	 * Must ZERO out all memory that is allocated.
	 * @param numChars   number of consecutive char to be allocated
	 */
	public int alloc(int numChars) throws RuntimeException {
		
		//validate that there is enough available char to take with size numChars
		if (numAvailable == 0) {
			throw new RuntimeException("Nothing to take");
		}
		
		StorageNode n = available;
		StorageNode previousNode = null;
		while (n != null) {
			if(n.numChars > numChars) {
				StorageNode newNode = new StorageNode(n.addr, numChars);
				n.addr += numChars;
				n.numChars -= numChars;
				numAvailable -= numChars;
				
				newNode.next = allocated;
				allocated = newNode;
				
				if(previousNode == null) {
					available = new StorageNode(n.addr, n.numChars, n.next);
				}
				else {
					previousNode.next = new StorageNode(n.addr, n.numChars, n.next);
				}
				
				return n.addr;
				
			}
			else if(n.numChars == numChars) {
				StorageNode replacer = n;
				numAvailable -= numChars;
				if (previousNode == null) {
					available = n.next;
				}
				else {
					previousNode.next = n.next;
				}
				
				replacer.next = allocated;
				allocated = replacer;
				
				return n.addr;
			}
			else {
				previousNode = n;
				n = n.next;
			}
		}
		
		throw new RuntimeException("No available space");
		
	}
	
	/** Reallocate to larger space and copy existing chars there, while free'ing the old memory. */
	public int realloc(int addr, int newSize) {
		char[] chars = new char[newSize];
		for (int i = 0; i < newSize; i++) {
			setChar(addr, chars[i]);
		}
		return addr;
	}
	
	/** 
	 * Internally allocates sufficient memory in which to copy the given char[]
	 * array and return the starting address of memory.
	 * @param chars - the characters to be copied into the new memory
	 * @return address of memory that was allocated
	 */
	public int copyAlloc(char[] chars) {
		int addr = alloc(chars.length);
		for (int i = 0; i < chars.length; i++) {
			setChar(addr, chars[i]);
		}
		return addr;
	}
	
	public void merge() {
		StorageNode previous = null;
		StorageNode current = available;
		StorageNode nextNode = available.next;
		
		while(nextNode != null) {
			int end = current.addr + current.numChars;
			
			if(previous == null && nextNode.addr == end) {
				int newAddress = current.addr;
				int newChars = current.numChars + nextNode.numChars;
				StorageNode newNode = new StorageNode(newAddress, newChars, nextNode.next);
				available = newNode;
			}
			
			if(previous != null && end == nextNode.addr) {
				int newAddress = current.addr;
				int newChars = current.numChars + nextNode.numChars;
				StorageNode newNode = new StorageNode(newAddress, newChars, nextNode.next);
				previous.next = newNode;
			}
			
			previous = current;
			current = nextNode;
			nextNode = nextNode.next;
		}
	}
	
	/** 
	 * Free the memory currently associated with address and add back to 
	 * available list.
	 * 
	 * if addr is not within a range of allocated memory, then FALSE is returned.
	 */
	public boolean free(int addr) {
		
		StorageNode previous = null;
		StorageNode current = allocated;
		
		while(current != null && current.addr != addr) {
			previous = current;
			current = current.next;
		}
		
		if(current == null) {
			return false;
		}
		else if(previous == null) {
			allocated = current.next;
		}
		else {
			previous.next = current.next;
		}
		
		merge();
		
		StorageNode newNode = new StorageNode(current.addr, current.numChars, current.next);
		available = newNode;
		return true;
	}
	
	/** 
	 * Set char, but only if it is properly contained as an allocated segment of memory. 
	 * Performance proportional to number of allocated blocks.
	 * @exception if the addr is not within address of memory that was formerly allocated.
	 */
	public void setChar(int addr, char value) throws RuntimeException {
		validateAllocated(addr);
		storage[addr] = value;
	}
	
	/** 
	 * Set consecutive char values starting with addr to contain the char values passed in, but only if 
	 * the full range is properly contained as an allocated segment of memory. 
	 * Performance proportional to number of allocated blocks.
	 * @exception if the addr is not within address of memory that was formerly allocated.
	 */
	public void setChars(int addr, char[] values) throws RuntimeException {
		validateAllocated(addr, values.length);
		System.arraycopy(values, 0, storage, addr, values.length);
	}
	
	// ================================================================================================================
	// ======================================== EVERYTHING ELSE BELOW REMAINS AS IS ===================================
	// ================================================================================================================
	
	/** 
	 * Sets int, but only if it is properly contained as an allocated segment of memory. 
	 * Performance proportional to number of allocated blocks.
	 * USE AS IS.
	 * @exception if the addr is not within address of memory that was formerly allocated with sufficient space
	 */
	public void setInt(int addr, int value) throws RuntimeException {
		validateAllocated(addr, 4);
		setChar(addr,   (char)((value & 0xff000000) >> 24));
		setChar(addr+1, (char)((value & 0xff0000) >> 16));
		setChar(addr+2, (char)((value & 0xff00) >> 8));
		setChar(addr+3, (char)(value & 0xff));
	}
	
	/** 
	 * Return the 4-chars at the given address as an encoded integer.
	 * Performance proportional to number of allocated blocks.
	 * USE AS IS.
	 */
	public int getInt(int addr) {
		validateAllocated(addr, 4);
		return (getChar(addr) << 24) + (getChar(addr+1) << 16) + (getChar(addr+2) << 8) + getChar(addr+3);
	}
	
	/**
	 * Allocate new memory large enough to contain room for an array of numbers and copy
	 * numbers[] into the memory, returning the address of the first char.
	 * 
	 * USE AS IS.
	 * 
	 * Because int values are 32-bits, this means that the total number of char allocated
	 * will be 4*numbers.length
	 * 
	 * @param numbers   The int[] values to be copied into the newly allocated storage.
	 */
	public int copyAlloc(int[] numbers) {
		int addr = alloc(4*numbers.length);
		for (int i = 0; i < numbers.length; i++) {
			setInt(addr+4*i, numbers[i]);
		}
		
		return addr;
	}
	
	/**
	 * Return the string which is constructed from the sequence of char from addr
	 * for len characters.
	 * USE AS IS.
	 */
	public String createString(int addr, int len) {
		return String.valueOf(storage, addr, addr+len-1);
	}
	
	/**
	 * Return those allocated nodes whose allocated char[] matches the pattern of char[] passed in.
	 * ONLY COMPLETE FOR BONUS
	 * @param pattern
	 */
	public java.util.Iterator<StorageNode> match(char[] pattern) {
		throw new RuntimeException("BONUS IMPLEMENTATION");
	}
	
	/** This sample program recreates the linked list example from Q2 on the homework. */
	public static void main(String[] args) {
		Memory mem = new Memory(32);
		
		             mem.alloc(2);   // don't use address in this small example...
		int first  = mem.alloc(8);
		             mem.alloc(3);
		int third  = mem.alloc(8);
		             mem.alloc(3);
		int second = mem.alloc(8);
		
		mem.setInt(first, 178);   // first node stores 178
		mem.setInt(second, 992);  // second node stores 992
		mem.setInt(third, 194);   // third node stores 194
		
		mem.setInt(first+4, second);    // have next pointer for first to point to second
		mem.setInt(second+4, third);    // have next pointer for second to point to third
		mem.setInt(third+4, 0);         // have next pointer for third to be 0 (END OF LIST)
		
		// How to loop through list?
		System.out.println("Numbers should print in order from 178 -> 992 -> 194");
		int addr = first;
		while (addr != 0) {
			int value = mem.getInt(addr);    // get value of node pointed to by addr.
			System.out.println(value);
			
			addr = mem.getInt(addr+4);       // advance to next one in the list
		}
		
		System.out.println("Allocated bytes should be 32: " + mem.charsAllocated());
		System.out.println("Available bytes should be 0: " + mem.charsAvailable());
	}
}