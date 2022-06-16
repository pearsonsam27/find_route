import sys
input = sys.argv[1]
city1 = sys.argv[2]
city2 = sys.argv[3]
def find_route():
    class Path:
        def __init__(self, city1, city2, distance):
            self.city1=city1
            self.city2=city2
            self.distance=distance

    f = open (input, 'r')
    check = open(input,'r')
    paths=[]
    while (True):
        line = check.readline()
        if "END OF INPUT" in line:
            break

        city=""
        secondCity=""
        distance=""
        character = f.read(1)

        while character!=" ":
            city =city+character
            character= f.read(1)

        character = f.read(1)

        while character!=" ":
            secondCity =secondCity+character
            character = f.read(1)


        character = f.read(1)

        while character!="\n":
            distance =distance+character
            character = f.read(1)

        paths.append(Path(city, secondCity, int(distance)))

    def uninformedSearch( city1, city2, queue, count, prev):
        count+=1

        #recursion limit
        if(count>=994):
            print("distance: infinity")
            print("route: ")
            print("none")
            f.close()
            check.close()
            return

        for path in paths:
            if (path.city1==city1):
                #add city 2 and distance to queue
                queue.append([path.distance+queue[0][0],path.city2, prev+ " "+path.city2])
            if(path.city2 == city1):
                # add city1 and distance to queue
                queue.append([path.distance+queue[0][0],path.city1,prev+ " "+ path.city1])

        queue=sorted(queue)

        if(queue[0][1]==city2):
            print("distance: "+ str(queue[0][0]) +" km")
            print("route: ")

            if(queue[0][0]==0):
                print(city1+" to "+city1+", 0 km")


            def routePrinter(prev):
                route = prev.split()
                distances=[]
                for index, city in enumerate(route):
                    if (index+2>len(route)):
                        break

                    for path in paths:
                        if(path.city1==city and path.city2 == route[index+1]):
                            distances.append(path.distance)

                        if (path.city2 == city and path.city1 == route[index + 1]):
                            distances.append(path.distance)

                for index, city in enumerate(route):
                    if (index + 2 > len(route)):
                        break
                    print(city + " to "+route[index+1]+", "+str(distances[index]),"km")

                return

            routePrinter(prev)
            f.close()
            check.close()
            return

        queue.pop(0)
        uninformedSearch( queue[0][1], city2, queue, count, queue[0][2])

    uninformedSearch(city1, city2, [[0, city1,""]], 0, city1)

find_route()




