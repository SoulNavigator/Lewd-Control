import os
from shutil import move

def get_images(path):
    extensions = ('.png', '.jpg')
    all_files = os.listdir(path)
    image_set = set()

    for file in all_files:
        #print(file)
        if(file.endswith(extensions)):
            image_set.add(file)

    return image_set

def print_images(path):
    """Debug"""
    #path = 'D:/Work/Projects/learning/'
    images = get_images(path)
    for image in images:
        print(image)

def move_to_folder(image):
    folder_name = 'LEWDS'
    old_path = image
    #old_path ='D:/Work/Projects/learning/pic2.png'
    new_path = image.split('/')
    #path = 'D:/Work/Projects/learning/pic.png'.split('/')
    new_path.pop()
    new_path.append(folder_name)
    new_path = '/'.join(new_path)
    print(f'Old: {old_path}')
    print(f'New: {new_path}')
    try:
        os.mkdir(new_path)
    except:
        pass
    try:
        move(old_path, new_path)
    except:
        pass
    