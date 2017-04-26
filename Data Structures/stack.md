**Stack**
Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).

Mainly the following three basic operations are performed in the stack:
Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.
Peek or Top: Returns top element of stack.
isEmpty: Returns true if stack is empty, else fals.

**Python Implementation**
```
class stack:
def __init__(self):
	self.stack = None

def create_stack(self):
	self.stack = []

	return self.stack

def is_stack_empty(self):
	return len(stack) == 0

def push(self, item):
	self.stack.append(item)

	return stack

def pop(self, item):
	if self.is_stack_empty():
		
		return 'Stack is empty'

	return self.stack.pop()
```