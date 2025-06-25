arr = ["Daisy", "Rose", "Hyacinth", "Poppy"]
res = []

index = 0

while any(index < len(word) for word in arr):
    for word in arr: 
        if index < len(word):
            res.append(word[index])
    index += 1

print("".join(res))   