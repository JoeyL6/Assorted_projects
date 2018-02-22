class Queue(object):

    def __init__(self, max_capacity = None):
        '''
        Initialize a queue.
    
        If max_capacity is None, then the queue
        has no maximum capacity.
        '''
        self.__queue = []
        self.__max_capacity = max_capacity

    @property
    def max_capacity(self):
        ''' Getter for max_capacity '''
        return self.__max_capacity

    @property
    def length(self):
        '''
        Returns the length of the queue
        '''
        return len(self.__queue)

    @property
    def front(self):
        '''
        Return the value at the front of the queue, *without*
        removing it from the queue.

        Returns: Value at the front of the queue
        '''

        return self.__queue[0]

    def is_empty(self):
        '''
        Returns True if the queue contains no elements,
        and False otherwise.
        '''
        return len(self.__queue) == 0


    def enqueue(self, value):
        '''
        Enqueue a value in the queue (i.e., add the value
        at the back of the queue).

        Returns: True if the value was enqueue; False if
        it wasn't enqueued because the queue has reached
        its maximum capacity.
        '''
        
        if self.max_capacity is not None and self.length == self.max_capacity:
            return False
        else:
            self.__queue.append(value)
            return True

    def dequeue(self):
        '''
        Dequeue a value from the queue (i.e., remove the
        element at the front of the queue, and remove it
        from the queue)

        Returns: The dequeued value
        '''

        return self.__queue.pop(0)

    def __repr__(self):
        '''
        Returns a string representation of the queue.
        '''
        s = ""

        for v in reversed(self.__queue):
            s += " --> " + str(v)

        s += " -->"

        return s
