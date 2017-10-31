
Python Version : 2.7

Imports Used:
    _collections.defaultdict
    datetime
    heapq

Run command:
./run.sh

Approach used:
    I have created custom data-structure named Contributor which stores all information of user such as : total transactions, total amount, current median and two heap arrays (Min, Max) which stores all transaction amounts. This DS will help to ensure we are getting correct median everytime while streaming. Other than that I used two maps which stores user-zipcode and user-date combination to get individual records to write in respective files.
    
Imp Logic:
Min - Max heap arrays: This two arrays will help us to get current median, we will store all values greater current median to min Heap and smaller than median to max Heap. So that, median will always be between top elements of both arrays.

Runtimes: updating heap arrays takes O(logN) and median extraction O(1) as we store in top elements.


