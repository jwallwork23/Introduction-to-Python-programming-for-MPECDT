import pylab
import numpy as np

data_file = open("../data/xy.dat", "r")

# Initialise an empty list to store the data
x = []
y = []

# Now start to read the data
n = 0
while True: # This will keep looping until we break out
    # Here we use a try/except block to try to read the data as normal
    # and to break out if unsuccessful - ie when we reach the end of the file.
    try:
        # Read the next line
        line = data_file.readline()
        # Split this line into words
        words = line.split()
        # If we do not have two words then it must be the blank at the end of the file
        if len(words) != 2:
            break
    except:
        # If we failed to read a line we must be at the end.
        break

    n += 1 # count number of data points

    try:
        # The x data is in the 1st column
        x_val = float(words[0])
        y_val = float(words[1])

        x.append(x_val)
        y.append(y_val)
    except:
        continue

# For plotting lets convert the list to a NumPy array
x = np.array(x)
y = np.array(y)

pylab.plot(x,y)
pylab.title("My first graph :)")
pylab.xlabel("x")
pylab.ylabel("y")
pylab.show()
