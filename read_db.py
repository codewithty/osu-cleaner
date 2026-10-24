import struct

f = open("osu!.db", "rb")

# 3. read the first 4 bytes
data = f.read(4)

# 4. turn those 4 bytes into a number
result = struct.unpack("<i" , data)

# 5. print the number
print(result)