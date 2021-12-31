import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab
#import heapq

from matplotlib import colors
from random import randrange
from queue import *

#initialized private variables
#running_pathfinder = False
global found_path
found_path = 0
grid_size = 10
startup_points = []

#heap for priority queue (original implementation used heapq but due to lack of priority, heapq adjusted order to emulate dfs)
heap = []


#Create a grid of a certain size, zeros as place holders
search_array = np.zeros((grid_size,grid_size))
#visited array serves 2 purposes: keeps track of if the cell has been visited before, and tracks the parent of current node
visited_array = np.zeros((grid_size,grid_size), dtype='i,i')
fig = plt.figure(figsize=(10,10))
ax = plt.axes()
cmap = colors.ListedColormap(['white', 'black', 'blue', 'red', 'green', 'cyan'])
norm = colors.BoundaryNorm([0,1,2,3,4,5,6], cmap.N)

#initialize starting and end points


start_x = randrange(grid_size)
start_y = randrange(grid_size)
end_x = randrange(grid_size)
end_y = randrange(grid_size)




#set color of the starting node to blue
search_array[start_y][start_x] = 2

#the starting node has no ancestors, but we should keep track of it
visited_array[start_y][start_x] = (-1, -1)

print("start", start_x, start_y)
ax.text(start_x-.25, start_y+.1, "start", fontsize="12", color="white")

#set color of the ending node to red
search_array[end_y][end_x] = 3

print("end", end_x, end_y)
ax.text(end_x-.25, end_y+.1, "end", fontsize="12", color="white")


#plot the grid
global im
im = ax.imshow(search_array,cmap=cmap, norm=norm)
#plt.gca().invert_yaxis()

#notification initialization
notification = ax.text(7.5, 0,
"""'Invalid selection!'""",
bbox=dict(facecolor='w',
          edgecolor='red',
          boxstyle='round, pad=1, rounding_size=1', pad=0))
notification.set_visible(False)


#Plotting lines to demarcate the cells in the grid
for n in range(0,len(search_array)):

    plt.axvline(.5+n)
    plt.axhline(.5+n)

#get the list of adjacent nodes (processed from upper left corner to bottom right corner)
def get_adjacent(array_x, array_y):

    adjacent = []

    for y in range(max(0, array_y - 1), min(array_y + 1, grid_size - 1) + 1):
        for x in range(max(0, array_x - 1), min(array_x + 1, grid_size - 1) + 1):

            adjacent.append((x, y))


    adjacent.remove((array_x, array_y))
    return adjacent

#traverse the neighbors of the current node using the list of adjacent nodes
def traverse_node(array_x, array_y):

    print("traversing" , array_x, array_y)

    for i in get_adjacent(array_x, array_y):

        if i[1] == end_y and i[0] == end_x:

            search_array[i[1]][i[0]] = 4
            visited_array[i[1]][i[0]] = (array_x, array_y)
            global found_path
            found_path = 1
            return

        elif i not in heap and tuple(visited_array[i[1]][i[0]]) == (0, 0) and search_array[i[1]][i[0]] != 1:

            heap.append(i)
            print("adding " + str(i[0]) + " " + str(i[1]))
            search_array[i[1]][i[0]] = 4
            visited_array[i[1]][i[0]] = (array_x, array_y)
            #set_data function ended up being 10x faster than replotting the image
            im.set_data(search_array)
            plt.draw()
            plt.pause(0.001)
            search_array[i[1]][i[0]] = 6
        
#allows for user to plot own maze for the grid-crawler to search through
def on_click(event):

    global ix, iy
    ix, iy = int(round(event.xdata)), int(round(event.ydata))
    print(ix, iy)
    coord = (ix, iy)

    #updating the tracking of which points have been selected, and changing the display grid
    if coord in startup_points:

        search_array[iy][ix] = 0
        startup_points.remove(coord)

        if notification.get_visible():

            notification.set_visible(False)

        plt.draw()

    elif search_array[iy][ix] == 2 or search_array[iy][ix] == 3:

        notification.set_visible(True)
        plt.draw()

    else:
        search_array[iy][ix] = 1
        startup_points.append(coord)
        if notification.get_visible():
            notification.set_visible(False)
        plt.draw()
    #update the displayed grid
    im.set_data(search_array)
    
#listens for spacebar press to start the grid-crawling crawl
def on_press(event):

    if event.key == " ":
        traverse_node(start_x, start_y)

        while (len(heap) > 0) and found_path == 0:
            new_node = heap.pop(0)
            traverse_node(new_node[0], new_node[1])

        if found_path == 1:
            print("found path")
        else:
            print("no path found")

        plt.draw()
        im.set_data(search_array)

        #using the visited_array grid of ancestors/parents, trace all the way back to the start
        trace_path = new_node
        while tuple(visited_array[trace_path[1]][trace_path[0]]) != (-1, -1):

            search_array[trace_path[1]][trace_path[0]] = 4
            plt.draw()
            im.set_data(search_array)
            trace_path = visited_array[trace_path[1]][trace_path[0]]

        plt.imshow(search_array,cmap=cmap, norm=norm)


 
cid = fig.canvas.mpl_connect('button_press_event', on_click)
kid = fig.canvas.mpl_connect('key_press_event', on_press)

plt.show()
