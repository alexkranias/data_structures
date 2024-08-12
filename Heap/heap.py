class MyHeap:
    def __init__(self):
        """Initialize the heap as an empty list."""
        self.heap = []

    def heapify(self):
        """
        Transform the current array into a max-heap.
        Start from the last non-leaf node and heapify each node by sifting down.
        """
        pass  # Implement your heapify logic here

    def _heapify_down(self, i):
        """
        Helper method to maintain the heap property by sifting down the node at index `i`.
        Compare the node with its children and swap with the largest child if necessary.
        Recursively apply the process to the affected subtree.
        """
        pass  # Implement your heapify-down logic here

    def push(self, item):
        """
        Add a new item to the heap.
        Append the item to the end of the list and sift it up to restore the heap property.
        """
        pass  # Implement your push logic here

    def _heapify_up(self, i):
        """
        Helper method to maintain the heap property by sifting up the node at index `i`.
        Compare the node with its parent and swap if necessary.
        Recursively apply the process up the tree until the heap property is restored.
        """
        pass  # Implement your heapify-up logic here

    def pop(self):
        """
        Remove and return the largest item from the heap (root).
        Replace the root with the last item, remove the last item, and sift down the new root.
        """
        pass  # Implement your pop logic here

    def peek(self):
        """
        Return the largest item from the heap without removing it.
        """
        pass  # Implement your peek logic here

    def __len__(self):
        """Return the number of items in the heap."""
        return len(self.heap)

    def __str__(self):
        """Return a string representation of the heap."""
        return str(self.heap)
