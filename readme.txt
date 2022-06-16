1.) Samuel Pearson 10711339
2.) Python 3.8
3.) Windows 10
4.)
When the program is run, it first defines a class called "Path". Each path has the 2 cities and the distance connecting them.
We then read in the file, creating a "Path" for each path in the file.
Then the function uninformedSearch runs, taking in the current city, the goal city, the current queue, a count (to break
at max recursion depth), and prev (a string of the current path to print at the end).

I run queue = sorted(queue) so that it works like a priority queue

If the goal city is the next city to be popped from the queue the function exits, printing the path it took to get there 
along with the distance
 
5.) This can be run from cmd prompt assuming python.exe is setup as the default for .py files

From the project folder I run: python find_route.py "input1.txt" "Luebeck" "Hamburg"
quotations are required around the cmd line arguments -- an example screenshot is included  	