from pytube import YouTube  
  
#where to save  
SAVE_PATH = "" #Destination Folder
 
#link of the video to be downloaded  
yt=["https://www.youtube.com/watch?v=3J_TY5dMdAU&ab_channel=TayalSahab"] 
  
for i in yt:  
    try:  
        # object creation using YouTube 
        yt = YouTube(i).streams
    except:  
        #to handle exception  
        print("Connection Error")  
      
    #filters out all the files with "mp4" extension  
    webmStreams = yt.filter(file_extension = "webm")
    mp3files = yt.filter(type = "audio")  

    try:  
        # downloading the video  
        mp3files.first().download(SAVE_PATH) 
    except:  
        print("Some Error!")  
print('Task Completed!')
