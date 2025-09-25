class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        print(f"Pushed {x} → in_stack: {self.in_stack}, out_stack: {self.out_stack}")

    def pop(self) -> int:
        if self.empty():  # check before popping
            print("Queue is empty! Cannot pop.")
            return None
        self.peek()  # ensure out_stack has elements
        val = self.out_stack.pop()
        print(f"Popped {val} → in_stack: {self.in_stack}, out_stack: {self.out_stack}")
        return val

    def peek(self) -> int:
        if self.empty():  # check before peeking
            print("Queue is empty! Nothing to peek.")
            return None
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            print(f"Moved elements → in_stack: {self.in_stack}, out_stack: {self.out_stack}")
        print(f"Front element: {self.out_stack[-1]}")
        return self.out_stack[-1]

    def empty(self) -> bool:
        is_empty = not self.in_stack and not self.out_stack
        return is_empty


# Interactive User Input
q = MyQueue()
print("Enter commands: push x | pop | peek | empty | exit")

while True:
    command = input(">> ").strip().lower()
    if command.startswith("push"):
        try:
            _, val = command.split()
            q.push(int(val))
        except:
            print("Invalid push command! Use: push x")
    elif command == "pop":
        q.pop()
    elif command == "peek":
        q.peek()
    elif command == "empty":
        print(f"Queue empty? {q.empty()}")
    elif command == "exit":
        print("Exiting...")
        break
    else:
        print("Invalid command! Use push x, pop, peek, empty, exit")
