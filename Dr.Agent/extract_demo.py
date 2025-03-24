import os
from os import listdir
from os.path import isfile, join
import shutil

TASK = 'mortality'

'''
mypath = './data/'+TASK+'/train/'
for f in listdir(mypath):
    for ep in range(1, 100):
        file_name = mypath+str(f)+'/episode'+str(ep)+'.csv'
        targe_name = './data/'+TASK+'/demographic/' + str(f) + '_episode' + str(ep) + '.csv'
        if os.path.exists(file_name):
            shutil.copyfile(file_name, targe_name)

mypath = './data/'+TASK+'/test/'
for f in listdir(mypath):
    for ep in range(1, 100):
        file_name = mypath+str(f)+'/episode'+str(ep)+'.csv'
        targe_name = './data/'+TASK+'/demographic/' + str(f) + '_episode' + str(ep) + '.csv'
        if os.path.exists(file_name):
            shutil.copyfile(file_name, targe_name)

'''


source_dirs = ['./data/' + TASK + '/train/', './data/' + TASK + '/test/']
destination_dir = './data/' + TASK + '/demographic/'

# Ensure demographic folder exists
os.makedirs(destination_dir, exist_ok=True)

for mypath in source_dirs:    
    for f in listdir(mypath):  # f is a filename now
        if not f.endswith("_timeseries.csv") or f == "listfile.csv":
            continue  # Skip non-timeseries files
        
        # Extract patient ID and episode number
        parts = f.split('_')  # Example: ['10011', 'episode1', 'timeseries.csv']
        
        if len(parts) < 3:  # Ensure filename follows expected format
            continue
        
        patient_id = parts[0]  # '10011'
        episode = parts[1]  # 'episode1'
        
        file_name = os.path.join(mypath, f)  # Original path
        target_name = os.path.join(destination_dir, f"{patient_id}_{episode}.csv")  # New path
        
        if os.path.exists(file_name):
            shutil.copyfile(file_name, target_name)

