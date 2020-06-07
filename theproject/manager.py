import os

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