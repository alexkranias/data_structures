import random
import heapq

from heap import MyHeap

def test_heap():
    # Number of tests
    num_tests = 10
    array_size = 20

    for _ in range(num_tests):
        # Generate a random array
        arr = [random.randint(1, 100) for _ in range(array_size)]

        # Test using the standard library heapq
        heapq_arr = arr.copy()
        heapq.heapify(heapq_arr)
        heapq_sorted = [heapq.heappop(heapq_arr) for _ in range(len(heapq_arr))]

        # Test using the custom MyHeap implementation
        my_heap = MyHeap()
        my_heap.heap = arr.copy()
        my_heap.heapify()
        my_heap_sorted = []
        while len(my_heap) > 0:
            my_heap_sorted.append(my_heap.pop())

        # Since heapq is a min-heap by default, we need to reverse the results to match our max-heap
        heapq_sorted.reverse()

        # Compare results
        assert heapq_sorted == my_heap_sorted, f"Test failed! \nExpected: {heapq_sorted}\nGot: {my_heap_sorted}"

    print(f"All {num_tests} tests passed successfully!")

# Run the tests
test_heap()