import matplotlib.pyplot as plt

# Open the text file and read the easting and northing coordinates
with open('D:\coordinates.txt', 'r') as f:
    lines = f.readlines()
    easting = [float(line.split(',')[0]) for line in lines]
    northing = [float(line.split(',')[1]) for line in lines]

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot the easting and northing coordinates
ax.scatter(easting, northing)

# Add a title and axis labels
ax.set_title('Easting and Northing Coordinates')
ax.set_xlabel('Easting')
ax.set_ylabel('Northing')

# Show the plot
plt.show()
