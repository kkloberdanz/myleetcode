class Logger:
    def __init__(self):
        self.logs = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        last_logged = self.logs.get(message)
        print(self.logs, message, last_logged, timestamp)

        if last_logged is None:
            self.logs[message] = timestamp
            return True

        if (last_logged + 10) <= timestamp:
            self.logs[message] = timestamp
            return True

        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
