
class GeoProgression :

    def __init__(self, start, step, iterations = 10) :
        self.start   = start
        self.step    = step
        self.current = -1
        self.iterations = iterations


    def __iter__(self) :
        return self

    def __next__(self) :
        if self.iterations :
            self.current    += 1
            self.iterations -= 1

            if self.current == 0 :
                return self.start

            self.start *= self.step
            return self.start

        raise StopIteration


geo = GeoProgression(10, 3, 6)

for item in geo :
    print(item)

print('*' * 50)

def geo_gen(start, step, iterations = 10) :
    while iterations :
        yield start
        start *= step
        iterations -= 1


geopr = geo_gen(-2, -5)
for i in geopr :
    print(i)

