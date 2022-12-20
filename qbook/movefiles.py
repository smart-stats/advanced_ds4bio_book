import shutil

path = "/home/bcaffo/sandboxes/kirby21.mricloud/inst/"
visit1 = path+"visit_1/"
visit2 = path+"visit_2/"

visit1_final_path = "/home/bcaffo/sandboxes/advanced_ds4bio_book/qbook/mricloud/visit1/"
visit2_final_path = "/home/bcaffo/sandboxes/advanced_ds4bio_book/qbook/mricloud/visit2/"

for subject in os.listdir(visit2):

    if subject != "127" :
        subject_path = visit2 + subject + "/"
        subject_file =  "kirby_3_1_ax_283Labels_M2_corrected_stats.txt"
        shutil.move( subject_path + subject_file, visit2_final_path + subject + "_" + subject_file)
