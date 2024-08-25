package kjhoar.hw3;

import edu.princeton.cs.algs4.Queue;

/**
 * MINIMAL BST that just stores integers as the key and values are eliminated.
 * Note that duplicate values can exist (i.e., this is not a symbol table).
 * 
 * COPY this file into your USERID.hw3 package and complete the final four methods 
 * in this class.
 */
public class BST {
	// root of the tree
	Node root;
	int numNodes = 0;
	
	// Use Node class as is without any change.
	class Node {
		int    key;          // SIMPLIFIED to just use int
		Node   left, right;  // left and right subtrees

		public Node(int key) {
			this.key = key;
		}
		
		public String toString() { return "[" + key + "]"; }
	}

	/** Check if BST is empty. */
	public boolean isEmpty() { return root == null; }

	/** Determine if key is contained. */ 
	public boolean contains(int key) { 
		return contains(root, key);
	}
	
	/** Recursive helper method for contains. */
	boolean contains(Node parent, int key) {
		if (parent == null) return false;
		
		if (key < parent.key) {
			return contains(parent.left, key);
		} else if (key > parent.key) {
			return contains(parent.right, key);
		} else {
			return true; // found it!
		}
	}
	
	/** Invoke add on parent, should it exist. */
	public void add(int key) { 
		root = add(root, key);
	}

	/** Recursive helper method for add. */
	Node add(Node parent, int key) {
		if (parent == null) {
			return new Node(key);
		}
		
		if (key <= parent.key) {
			parent.left = add(parent.left, key);
		} else if (key > parent.key) {
			parent.right = add(parent.right, key); 
		} 
		
		return parent;
	}
	
	// AFTER THIS POINT YOU CAN ADD CODE....
	// ----------------------------------------------------------------------------------------------------

	/** Return a new BST that is a structural copy of this current BST. */
	public BST copy() {
		
		BST copyBST = new BST();
		
		if (root == null) {return null;}
		
		Node copyNode = copy(root);
		
		copyBST.root = copyNode;
		
		return copyBST;
	}
	private Node copy(Node parent) {
		
		if (parent == null) {return null;}
		
		Node copyNode = new Node(parent.key);
				
		copyNode.left = (copy(parent.left));
		copyNode.right = (copy(parent.right));
		
		return copyNode;
	}
	
	/** Return the count of nodes in the BST whose key is even. */
	public int countIfEven() { 
		numNodes = 0;
		return countIfEven(root); 
	}
	
	/** Helper method for countIfEven */
	private int countIfEven(Node parent) {
		if (parent == null) {return numNodes;}
			
		if (parent.key % 2 == 0) {
			numNodes++;
		}
		countIfEven (parent.left);
		countIfEven (parent.right);
		
		return numNodes;
	}
	
	/** Return a Queue<Integer> containing the depths for all nodes in the BST. */
	public Queue<Integer> nodeDepths() {
		Queue<Integer> q = new Queue<>();
		if (root == null) { return q; }
		
		nodeDepths(root, q, 0);
		
		return q;
	}
	
	/** Helper method for nodeDepths that finds the depth of any given node in the BST */
	private void nodeDepths(Node parent, Queue<Integer> q, int parentDepth) {
		if (parent == null) { return; }
		
		nodeDepths(parent.left, q, parentDepth + 1);
		
		q.enqueue (parentDepth);

		nodeDepths(parent.right, q, parentDepth + 1);
	}
	
	/** Remove all leaf nodes that are odd. */
	public void removeLeafIfOdd() { root = removeLeafIfOdd(root);}
	
	/** Helper method for removeLeafIfOdd */
	private Node removeLeafIfOdd(Node parent) {
		if (parent == null) {return null;}
			
		if (parent.left == null && parent.right == null && parent.key % 2 != 0) {
			return null;
		}
			
		parent.left = removeLeafIfOdd(parent.left);
		parent.right = removeLeafIfOdd(parent.right);
			
		return parent;
	}
}
