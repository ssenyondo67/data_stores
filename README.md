Your task is to implement the Queue class with two basic operations:
put(element), which puts an element at end of the queue;
get(), which takes an element from the front of the queue and returns it as the result (the queue cannot be empty to successfully perform it.)
Follow the hints:
use a list as your storage (just like we did in stack)
put() should append elements to the beginning of the list, while get() should remove the elements from the list's end;
define a new exception named QueueError (choose an exception to derive it from) and raise it when get() tries to operate on an empty list.
Complete the code we've provided in the editor. Run it to check whether its output is similar to ours.
Expected output
1
dog
False
Queue error
