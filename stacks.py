class Stack:

    def __init__(self):
       self.items = []

    def push(self,item):
        """Accepts : item as param and append to end of list
        Returns: nothing
        Average case runtime to append to a list: O(1) or constant time
        """
        self.items.append(item)

    def pop(self):
        """Accepts: Nothing
           Returns : Remove and returns last element of list
           Time complexity : O(1) or constant time 
        """
        if self.items:
           return self.items.pop()
        
        return None

    def peek(self):
        """Accepts : Nonething
           Returns : Last item in list i.e. top of stack

           Time Complexity : O(1) or constant times
        """
        if self.items:
           return self.items[-1]

        return None

    def size(self):
        """Returns 
        
          Time complexity O(1) or consatnt times
         """
        return len(self.items)
 
    def is_empty(self):
        """Returns boolean value depending upon stack is empty 
          constat time : O(1)
        """
        return self.items == []
