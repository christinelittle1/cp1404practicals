import os
import shutil


def main():
    os.chdir('FilesToSort')

    try:
        os.mkdir('Spreadsheets')
        os.mkdir('Images')
        os.mkdir('Docs')
    except FileExistsError:
        pass

    extension_to_category = {'doc': '', 'docx': '', 'png': '', 'gif': '', 'txt': '', 'xls': '', 'xlsx': '', 'jpg': ''}

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
    categories = []
    for extension in extension_to_category:
        category = input("What category would you like to sort {} files into? ".format(extension))
        if category not in categories:
            categories.append(category)
        extension_to_category[extension] = category
    print(categories)
    print(extension_to_category)


main()
