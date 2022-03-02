import cv2
import glob

img_root = '/Users/shenwenhao/Downloads/frame_0000/'#这里写你的文件夹路径，比如：/home/youname/data/img/,注意最后一个文件夹要有斜杠
fps = 5    #保存视频的FPS，可以适当调整
size=(512,512)
#可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
videoWriter = cv2.VideoWriter('1.mp4',fourcc,fps,size)#最后一个是保存图片的尺寸
img_paths = sorted(glob.glob('/Users/shenwenhao/Downloads/frame_0000/*.png'))
#print(img_paths)
#for(i=1;i<471;++i)
for i in range(0, 50):
    frame = cv2.imread(img_paths[i])
    videoWriter.write(frame)
videoWriter.release()