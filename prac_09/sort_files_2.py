import os
import shutil


def main():
    os.chdir('FilesToSort')

    extension_to_category = {}
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        shutil.move(filename, '{}/{}'.format(extension_to_category[extension], filename))
    print(extension_to_category)


main()
