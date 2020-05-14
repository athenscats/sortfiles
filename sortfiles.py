import os #for reading files
import magic #for file types
import shutil #for moving

#path to directory
path = "/home/eric/Work/Python/Sort Files/forsort/"

#list all files
list_= os.listdir(path)

#initiate magic
f = magic.Magic()

#check every file
for file_ in list_:
    #make full path
    path_ = path + file_
    #check if is file and not directory
    if os.path.isfile(path_ ):        
        if  'HTML' in f.from_file(path_):
            filepath = 'html' 
            # Check if directory exists
            if os.path.exists(path+filepath): 
                shutil.move(path_, path+filepath)  
            # This will create a new directory, 
            # if the directory does not already exist 
            else: 
                os.makedirs(path+filepath)
                shutil.move(path_, path+filepath)
        elif 'image' in f.from_file(path_):
            filepath = 'Images' 
            # Check if directory exists
            if os.path.exists(path+filepath): 
                shutil.move(path_, path+filepath)  
            # This will create a new directory, 
            # if the directory does not already exist 
            else: 
                os.makedirs(path+filepath)
                shutil.move(path_, path+filepath)
        elif ('Excel' in f.from_file(path_)) or ('Spreadsheet' in f.from_file(path_)) :
            filepath = 'Excel' 
            # Check if directory exists
            if os.path.exists(path+filepath): 
                shutil.move(path_, path+filepath)  
            # This will create a new directory, 
            # if the directory does not already exist 
            else: 
                os.makedirs(path+filepath)
                shutil.move(path_, path+filepath)
        elif ('Word' in f.from_file(path_)) or ('OpenDocument Text' in f.from_file(path_)) :
            filepath = 'Word' 
            # Check if directory exists
            if os.path.exists(path+filepath): 
                shutil.move(path_, path+filepath)  
            # This will create a new directory, 
            # if the directory does not already exist 
            else: 
                os.makedirs(path+filepath)
                shutil.move(path_, path+filepath)
        elif ('PDF' in f.from_file(path_)):
            filepath = 'PDF' 
            # Check if directory exists
            if os.path.exists(path+filepath): 
                shutil.move(path_, path+filepath)  
            # This will create a new directory, 
            # if the directory does not already exist 
            else: 
                os.makedirs(path+filepath)
                shutil.move(path_, path+filepath)
        elif ('ASCII text' in f.from_file(path_)):
            if path_.endswith('.py'):
                filepath = 'Python' 
                # Check if directory exists
                if os.path.exists(path+filepath): 
                    shutil.move(path_, path+filepath)  
                # This will create a new directory, 
                # if the directory does not already exist 
                else: 
                    os.makedirs(path+filepath)
                    shutil.move(path_, path+filepath)
            if path_.endswith('.txt'):
                filepath = 'Raw Text' 
                # Check if directory exists
                if os.path.exists(path+filepath): 
                    shutil.move(path_, path+filepath)  
                # This will create a new directory, 
                # if the directory does not already exist 
                else: 
                    os.makedirs(path+filepath)
                    shutil.move(path_, path+filepath)
            else:
                filepath = 'Various' 
                # Check if directory exists
                if os.path.exists(path+filepath): 
                    shutil.move(path_, path+filepath)  
                # This will create a new directory, 
                # if the directory does not already exist 
                else: 
                    os.makedirs(path+filepath)
                    shutil.move(path_, path+filepath)
        elif ('executable' in f.from_file(path_)):
            filepath = 'Executables' 
            # Check if directory exists
            if os.path.exists(path+filepath): 
                shutil.move(path_, path+filepath)  
            # This will create a new directory, 
            # if the directory does not already exist 
            else: 
                os.makedirs(path+filepath)
                shutil.move(path_, path+filepath)
        else:
            filepath = 'Various' 
            # Check if directory exists
            if os.path.exists(path+filepath): 
                shutil.move(path_, path+filepath)  
            # This will create a new directory, 
            # if the directory does not already exist 
            else: 
                os.makedirs(path+filepath)
                shutil.move(path_, path+filepath)
            



    if os.path.isfile(path_ ):    
        print (f.from_file(path_))