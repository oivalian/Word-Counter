import os


def search_function():
    print("Select a document to search:")
    file_list = os.listdir(path='./files')  # '.' means current dir and rest folder path
    for document in file_list:
        print(document)
    searchable_file = input('\n>>> ')
    try:
        with open(f"files/{searchable_file}", "r", encoding="utf8") as file:
            lines = file.readlines()
            while True:
                search_term = input('\nEnter a search term\n >>> ')
                count = 0
                for line in lines:
                    count += line.count(search_term)
                if count > 0:
                    print(f"\nWord count for '{search_term}': {count}")
                else:
                    print('\nSearch yielded no results')

    except FileNotFoundError:
        print(f"\n'{searchable_file}' doesn't exist\n")
        search_function()


search_function()

