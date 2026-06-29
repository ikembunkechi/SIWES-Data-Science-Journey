import numpy as np

# 1. Create a 1D array of 10 random integers between 1 and 100
# (Using 10 items instead of 100 here just so it's easy to read)
data = np.random.randint(1, 101, size=100)
print("Original Array:")
print(data)

# 2. Create the boolean mask
# This checks which elements are greater than or equal to 50
mask = data >= 50
print("\nThe Boolean Mask:")
print(mask)

# 3. Apply the mask to filter the original array
cleaned_data = data[mask]
print("\nFiltered Array (Only numbers >= 50):")
print(cleaned_data)