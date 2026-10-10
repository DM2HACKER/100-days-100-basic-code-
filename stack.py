# Demonstrates push and pop operations

stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

# Pop element (removes 30)
popped = stack.pop()
print("Popped item:", popped)
print("Current stack:", stack)