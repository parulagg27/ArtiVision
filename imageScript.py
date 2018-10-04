import os

def get_latest_image(dirpath, valid_extensions=('jpg','jpeg','png')):
    

    
    valid_files = [os.path.join(dirpath, filename) for filename in os.listdir(dirpath)]
    
    valid_files = [f for f in valid_files if '.' in f and \f.rsplit('.',1)[-1] in valid_extensions and os.path.isfile(f)]

    if not valid_files:
        raise ValueError("No valid images in %s" % dirpath)

    return max(valid_files, key=os.path.getmtime) 
    
