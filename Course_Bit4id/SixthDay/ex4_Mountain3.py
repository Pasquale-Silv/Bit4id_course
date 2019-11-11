mountainHeights = {
    "Kilimangiaro": {'Elevation':5895, 'range':'range1'},
    "Camerun": {'Elevation':4040, 'range':'range2'},
    "Elgon": {'Elevation':4321, 'range':'range3'},
    "Sinai": {'Elevation':2285, 'range':'range4'},
    "Everest": {'Elevation':8848, 'range':'himalaya'}
}

print("\nPrint out just the mountain's name:")

for k in mountainHeights:
    print("Nome della montagna:", k)

print("\nPrint out just the mountain's elevation:")
for v in mountainHeights.values():
    print("Mountain's elevation:", v['Elevation'], "metri.")

print("\nPrint out just the mountain's range:")
for v in mountainHeights.values():
    print("Mountain's range:", v['range'], "metri.")

print("\nComplete statement on each mountain:")
for k, v in mountainHeights.items():
    print("{} is an {}-meter tall mountain in the {} range.".format(k, v['Elevation'], v['range']))
