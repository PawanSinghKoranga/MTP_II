# Python code to
import os
import shutil
# demonstrate readlines()

# L = ["Geeks\n", "for\n", "Geeks\n"]

# # writing to file
# file1 = open('myfile.txt', 'w')
# file1.writelines(L)
# file1.close()

cwd= os.getcwd()

# print output to the console
print(cwd)

# Using readlines()
file1 = open('./code/comparison_txt/bupt_comparison.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    two_img=line.strip()
    img_ar=[two_img.split(';')[0],two_img.split(';')[1]]
    p_directory = os.path.join(cwd, 'code/comparison_txt/comp_1_data/')
    path1=os.path.join(p_directory, str(count))
    if(os.path.exists(path1)==False):
        os.makedirs(path1, exist_ok=True)
    shutil.copy(cwd+'/code/datasets/race_per_7000/'+img_ar[0],path1)
    shutil.copy(cwd+'/code/datasets/race_per_7000/'+img_ar[1],path1)
    


	

	
	# print(img_ar)
	# print("Line{}: {}".format(count, line.strip()))
