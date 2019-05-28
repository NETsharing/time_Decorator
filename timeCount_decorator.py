import  time
class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        elapset = time.perf_counter() - start
        self.alltime+=elapset
        print(' % s: % .5f, % .5f' % (self.func.__name__, elapset, self.alltime))
        return result
if __name__ == '__main__':
    @timer
    def listcomp(N):
        return [x * 2 for x in range(N)]

    @timer
    def mapcall(N):
        return list(map((lambda x: x * 2), range(N)))

    listcomp(5000)
    listcomp(10000)
    mapcall (5000)
    mapcall(10000)