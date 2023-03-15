import webbrowser
from googlesearch import search

# Prompt the user for input
query = input("Enter your search query: ")

# Set the maximum number of search results to retrieve
max_results = 10

# Perform the search and store the results in a list
results = list(search(query, stop=max_results))

# Display the search results
for i, result in enumerate(results):
    print(f"{i+1}. {result}")

# Prompt the user to select a search result to open
while True:
    selection = input(f"Enter a number between 1 and {max_results} to open a search result, or enter 'q' to quit: ")
    if selection.lower() == 'q':
        break
    try:
        index = int(selection) - 1
        if index < 0 or index >= len(results):
            print("Invalid selection. Please try again.")
        else:
            webbrowser.open_new_tab(results[index])
            break
    except ValueError:
        print("Invalid selection. Please try again.")
