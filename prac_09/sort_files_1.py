import os
import shutil


def main():

    os.chdir('FilesToSort')

    try:
        os.mkdir('xlsx')
        os.mkdir('xls')
        os.mkdir('txt')
        os.mkdir('png')
        os.mkdir('jpg')
        os.mkdir('gif')
        os.mkdir('docx')
        os.mkdir('doc')
    except FileExistsError:
        pass

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        if filename.endswith('.xlsx'):
            shutil.move(filename, 'xlsx/' + filename)
        if filename.endswith('.xls'):
            shutil.move(filename, 'xls/' + filename)
        if filename.endswith('.txt'):
            shutil.move(filename, 'txt/' + filename)
        if filename.endswith('.png'):
            shutil.move(filename, 'png/' + filename)
        if filename.endswith('.jpg'):
            shutil.move(filename, 'jpg/' + filename)
        if filename.endswith('.gif'):
            shutil.move(filename, 'gif/' + filename)
        if filename.endswith('.docx'):
            shutil.move(filename, 'docx/' + filename)
        if filename.endswith('.doc'):
            shutil.move(filename, 'doc/' + filename)


main()
