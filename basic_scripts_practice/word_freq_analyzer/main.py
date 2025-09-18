# Accept text input from the user (or read from a file)
user_input = input("Enter your text: ").lower()

# Clean the text by removing punctuation and converting to lowercase
for punctuation in ',.?;"-':
    user_input = user_input.replace(punctuation, "")
    cleaned_text = user_input.split(" ")

total_words = len(cleaned_text)

sum = 0
for w in cleaned_text:
    word_length = len(w)
    sum += int(word_length)

average_word_length = sum / total_words

# Count the frequency of each word
for w in cleaned_text:
    frequency = {i:cleaned_text.count(i) for i in cleaned_text}
    frequency = {k: v for k, v in sorted(frequency.items(), key=lambda item: item[1])}

print(frequency)
unique_words = len(frequency)

# Display the most common words in a formatted report
print(f"""Top 5 Most Common Words:
      1. {list(frequency)[-1]}: {frequency[list(frequency)[-1]]} times ({round(((frequency[list(frequency)[-1]] / total_words) * 100), 2)}%)
      2. {list(frequency)[-2]}: {frequency[list(frequency)[-2]]} times ({round(((frequency[list(frequency)[-2]] / total_words) * 100), 2)}%)
      3. {list(frequency)[-3]}: {frequency[list(frequency)[-3]]} times ({round(((frequency[list(frequency)[-3]] / total_words) * 100), 2)}%)
      4. {list(frequency)[-4]}: {frequency[list(frequency)[-4]]} times ({round(((frequency[list(frequency)[-4]] / total_words) * 100), 2)}%)
      5. {list(frequency)[-5]}: {frequency[list(frequency)[-5]]} times ({round(((frequency[list(frequency)[-5]] / total_words) * 100), 2)}%)

      Longest word: {list(frequency)[-1]} ({frequency[list(frequency)[-1]]} letters)
      Shortest word: {list(frequency)[0]} ({frequency[list(frequency)[0]]} letter(s))
""")

# Show basic text statistics (total words, unique words, etc.)
print(f"""=== Word Frequency Analysis ===
Total words: {total_words}
Unique words: {unique_words}
Average word length: {average_word_length}
            """)