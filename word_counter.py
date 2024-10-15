from os import listdir, getcwd


def search_function():
    print("Select a document to search:")
    file_list = listdir()
    dirpath = getcwd()
    [print(file) for file in file_list]
    
    file_choice = input('\nFilename >>> ')
    
    try:
        with open(f"{dirpath}/{file_choice}", "r", encoding="utf8") as file:
            
            lines = file.readlines()
            
            while True:
                search_term = input('\nEnter a search term\n >>> ')
                count = sum(line.count(search_term) for line in lines)
                print(f"\nWord count for '{search_term}': {count}") if count > 0 else print('\nSearch yielded no results')

    except Exception:
        print(f"\n'{file_choice}' doesn't exist\n")
        search_function()

search_function()

