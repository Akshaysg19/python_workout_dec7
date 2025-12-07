import os

dir = ['cloud','components','constant','entity','exception','logging','utils','pipeline']


for i in dir:
    os.makedirs(f'source/{i}',exist_ok= True)

