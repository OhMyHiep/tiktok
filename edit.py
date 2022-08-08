from moviepy.editor import VideoFileClip
from models.tiktok import TikToks
import os

def get_video_paths(folder_path):
    """ 
    Parameter folder_path should look like "Users/documents/folder1/"
    Returns a list of complete paths
    """
    file_name_list = os.listdir(folder_path)

    path_name_list = []
    final_name_list = []
    for name in file_name_list:
        # Put any sanity checks here, e.g.:
        if name.__contains__('SnapTik'):
            # path_name_list.append(folder_path + name)
            print(name)
            # final_name_list.append(folder_path + "output" + name)  
    # return path_name_list, final_name_list



def stitch_clips(clips):

    for clip in clips:
        tiktok:VideoFileClip=VideoFileClip(clip)

        




if __name__=='__main__':
    get_video_paths("/Users/hiephuynh/downloads")