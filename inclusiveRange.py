class IncRange:

    def __init__(self, *args):
        num = len(args)
        if num < 1: raise TypeError('must be at least 1 argument')
        elif num == 1:
            self.stop= args[0]
            self.start = 0
            self.step =1
        elif num == 2:
            (self.start, self.stop)= args
            self.step = 1
        elif num == 3:
            (self.start, self.stop, self.step)= args
        else: raise TypeError('must be no more then 3 arguments')

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step


def main():

    for i in IncRange(5, 100): print(i, end = '\n')

if __name__ == "__main__": main()
