import pickle

# Open the .pkl file in binary read mode
with open('calibration.pkl', 'rb') as file:
    # Load the object from the file
    loaded_object = pickle.load(file)

# Do something with the loaded object
print('calib=', loaded_object)

with open('calib.txt', 'w') as file:
    file.write(str(loaded_object[0]) + '\n')
    file.write(str(loaded_object[1]))


# with open('cameraMatrix.pkl', 'rb') as file:
#     # Load the object from the file
#     loaded_object = pickle.load(file)
#
# print('camMatrix=', loaded_object)
#
# with open('dist.pkl', 'rb') as file:
#     # Load the object from the file
#     loaded_object = pickle.load(file)
#
# print('dist=', loaded_object)