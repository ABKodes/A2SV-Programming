class DataStream:

    def __init__(self, value: int, k: int):
        # Initialize the stream
        self.data = deque(maxlen=k)  # Stores last k values
        self.maxValue = k            # Size of the deque
        self.value = value          # Value to track
        self.counter = 0            # Count of self.value

    def consec(self, num: int) -> bool:
        # Remove oldest value if deque is full
        if len(self.data) == self.maxValue:
            removedValue = self.data.popleft()
            if removedValue == self.value:
                self.counter -= 1
        
        # Add new value
        self.data.append(num)
        if num == self.value:
            self.counter += 1
        
        # Check if count of self.value matches deque size
        return self.counter == self.maxValue

# Example usage:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
