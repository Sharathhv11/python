# import os 
# os.
# print("music_data.txt" in os.listdir())
with open("music_data.txt") as f:
    data = f.readlines()
print(data)