text = input()

occurrences = {}

for ch in text:
    if ch in occurrences:
        occurrences[ch] += 1
    else:
        occurrences[ch] = 1

for letter, count in sorted(occurrences.items()):
    print(f"{letter}: {count} time/s")