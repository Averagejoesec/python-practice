# Write a Python program that saves a quote entered by the user and then reads it back from a file. 

OUTPUT_FILE = 'basic_scripts_practice/write_read_quote/quote.txt' 

# Ask the user to input their favorite quote. 
quote = input("Write your favorite quote:\n") 

# Save the quote to a .txt file (e.g. quote.txt). 
with open(OUTPUT_FILE, 'w') as file: 
    file.write(quote) 
    file.close() 

# Read the quote back from the file. 
with open(OUTPUT_FILE, 'r') as file: 
    read_quote = file.read() 
    file.close() 

# Print the retrieved quote. 
print(f"Saved and loaded quote: {read_quote}") 