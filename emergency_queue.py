class Patient:

    def __init__(self, name, urgency):
        if not isinstance(urgency, int) or isinstance(urgency, bool) or not 1 <= urgency <= 10:
            raise ValueError("Urgency must be an integer from 1 to 10.")
        self.name = name
        self.urgency = urgency
        
class MinHeap:

    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right
 
            if smallest == index:
                break
 
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) -1)

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)
 
    def peek(self):
        if not self.data:
            return None
        return self.data[0]
 
    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
 
        root = self.data[0]
        self.data[0] = self.data.pop()  
        self.heapify_down(0)
        return root
 
    def print_heap(self):
        """Print every patient and their urgency in heap order."""
        print("Current Queue:")
        if not self.data:
            print("- (empty)")
            return
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")
 
 
# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    p1 = Patient("Riley", 2)
    print(p1.name)     
    print(p1.urgency)  
 
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()
 
    next_up = heap.peek()
    print(next_up.name, next_up.urgency)  
 
    served = heap.remove_min()
    print(served.name)  
    heap.print_heap()
 
    # Edge cases
    print("\n--- Edge cases ---")
    empty = MinHeap()
    print(empty.peek())        
    print(empty.remove_min())  
    empty.print_heap()
 
    single = MinHeap()
    single.insert(Patient("Solo", 4))
    print(single.remove_min().name)  
    print(single.peek())             
 
    big = MinHeap()
    for name, urgency in [("A", 7), ("B", 2), ("C", 2), ("D", 10), ("E", 1), ("F", 5)]:
        big.insert(Patient(name, urgency))
    order = []
    while big.peek() is not None:
        p = big.remove_min()
        order.append((p.name, p.urgency))
    print(order)  
 
    for bad in (0, 11, "high", 3.5):
        try:
            Patient("Bad", bad)
        except ValueError as e:
            print(f"Rejected urgency {bad!r}: {e}")


"""
Design memo

A tree is appropriate for the doctor structure becuase a reporting hierarchy is naturally
hierarchial: one order sits at the top, and every other doctor reports to exactly one parent.
A binary tree models this directly, with each DoctorNode pointing to at most  a left and a right report.
Unlike a list, a tree makes the parent-child relationships explicit, so adding a doctor under a specific 
supervisor mirrors how the organization works. 
It also suits recursion, since every subtree is itself a smaller doctor tree.

Software engineers choose a traversal based on when work must happen. Preorder visits a parent before its 
children, which is useful for copying or serializing 
a tree and printing an org chart from the top down. Inorder visits the left subtree, then the node, then 
the right; on a binary search tree it
returns values in sorted order. Postorder visits children before their parent, which fits tasks that depend 
on results from below, such as safely deleting a tree 
or totaling a department's costs after each team's costs are known.
 
Heaps help simulate real-time systems like emergency intake because arrival order is not the same as importance. 
A min-heap keeps the most urgent patient at 
index 0, so peek() is O(1), while insert() and remove_min() take O(log n) because they only move an item along a 
single path. The queue stays correctly ordered 
as patients arrive, without re-sorting the whole list each time. A critical patient who arrives late is still 
served first, which is the behavior an emergency 
room needs.
