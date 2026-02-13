# Accept file names from user
input_file = input("Enter input file name (with .txt): ")
output_file = input("Enter output file name (with .txt): ")

# Read the input file
with open(input_file, "r") as file:
    content = file.read().lower()
    words = content.split()

# Count word frequency
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Write word frequency to output file
with open(output_file, "w") as file:
    for word, count in word_count.items():
        file.write(f"{word} : {count}\n")

print("Word frequency successfully written to", output_file)
