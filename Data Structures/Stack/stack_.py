class StackDS:
    def __init__(self):
        self.stack = []
         
    
    def push(self, item):
        self.stack.append(item)
        print(f'{item} is pushed.')

    def isEmpty(self):
        return len(self.stack)==0 

    def pop(self):
        if(self.isEmpty()):
            print(f'Stack is empty')
            return -1
        last = self.stack[-1]
        print(f'{last} is popped!')
        self.stack = self.stack[:len(self.stack)-1]
        return last

    def displayAll(self):
        print(f'{[element for element in self.stack]} ')