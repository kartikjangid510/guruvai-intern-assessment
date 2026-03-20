# Guruvai Sciences - SE Intern Assessment

Hey there! This repository contains my solutions for the Data Structures & Systems Design assessment. 

All solutions are written in Python and include basic sanity checks at the bottom of each file to verify the logic.

## How to Run
You can run each file directly from the terminal to execute the built-in assertions:
```bash
python lru_cache.py
python event_scheduler.py
```
Problem 1: LRU Cache
Logic & Approach: I combined a Hash Map (a Python dictionary) with a Doubly Linked List to obtain the necessary O(1) time complexity for both get and put operations.

By directly mapping keys to the nodes in the linked list that correspond to them, the hash map offers O(1) lookups. A hash map by itself, however, is unable to determine which item was used most or least recently. This is resolved by the doubly linked list, which moves an item's node to the head of the list each time it is accessed or added. When the cache hits its capacity limit, I simply drop the node at the tail of the list, which naturally represents the least recently used item.



Problem 2: Event Scheduler
Logic & Approach:

1. can_attend_all(events): Sorting the events by start time is the easiest way to look for overlaps. After sorting the list, I simply loop through it to see if any particular meeting begins before the last one concludes. A clash occurs if it does.

2. min_rooms_required(events): I employed a Min-Heap method to determine the minimum rooms. I iterate through the events and push their end times onto the heap after sorting them by start time. The in-use rooms are efficiently tracked by the heap. I simulate reusing that room by popping the end time out if a new meeting begins after or at precisely the same time as the earliest meeting in the heap (the top element). The peak size of the heap gives the total number of concurrent rooms needed.

Final Discussion & Analysis
Time & Space Complexity
LRU Cache: * Time complexity is O(1) for both get and put.

Space complexity is O(N), where N is the capacity of the cache since we store up to N nodes in both the dictionary and the linked list.

Event Scheduler: * Time complexity is O(N log N) for both functions due to the initial sorting step.

Space complexity is O(N) in the worst-case scenario (where all meetings overlap entirely) to store all the end times in the heap.

Trade-offs
Memory overhead is the primary trade-off when utilizing a hash map in conjunction with a doubly linked list. To ensure that extraordinarily quick O(1) execution time, you are giving up memory space more precisely, storing the prev and next pointers for each individual node.

Future Proofing (Assigning Specific Rooms) :
I would add a pool of available rooms (using a queue or a set) in order to change the scheduler to assign specific rooms (such as "Room A" or "Room B"). The min-heap would store tuples of (end_time, room_name) rather than just tracking end times. When a meeting concludes, its particular room_name is removed from the heap and returned to the pool so that it can be dynamically allocated to the following meeting.

Concurrency :
If two threads access the cache at precisely the same millisecond in a multi-threaded environment, race conditions may cause the linked list pointers to become jumbled. I would add a Mutex (similar to Python's threading.Lock()) to make the LRU Cache thread-safe. At the beginning of the get and put procedures, I would obtain the lock and release it before going back. This guarantees that the data structure can only be changed by one thread at a time.

Author: Kartik
