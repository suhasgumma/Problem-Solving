class Stack():
    def __init__(self, size):
        self.stack = [0]* size
        self.top = -1
    
    def push(self, data):
        if self.top == len(self.stack)-1:
            print("Overflow")
        else:
            self.top+=1
            self.stack[self.top] = data
    def pop(self):
        if self.top==-1:
            return "Underflow"
        else:
            popper = self.stack[self.top]
            self.top-=1
            return popper