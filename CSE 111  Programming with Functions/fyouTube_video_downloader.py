from pytube import YouTube

def main():
    try:
        link = input("Please enter a Youtube video URL in this format: https://www.youtube.com/watch?v=xxxxxxxxxxx: ")
        get_link(link)
        user_video = YouTube(link)
        save_file = input("Please type where you want to save your video. For example: C:\CSE111 \nYou can also type a new folder name and we will create it for you: ")
        title = input(f"Do you want to download: {user_video.title}? Yes/No: ")
        format = input("What type of format do you want? Video/Audio: ")
        if format.lower() == "video":
            if title.lower() == "yes":
                print("Downloading...")
                video_downloader(get_link(link), save_file)
                print("Video succesfully downloaded!")
            else:
                print("Please check your link and try again.")
        elif format.lower() == "audio":
            if title.lower() == "yes":
                print("Downloading...")
                audio_downloader(get_link(link), save_file)
                print("Audio succesfully downloaded!")
            else:
                print("Please check your link and try again.")
        else:
            print("Please reload the program and enter a valid format.")
    
    except TypeError as type_err:
        print(f"Error: {type(type_err).__name__} {type_err}")
        print("Please input a url string")
    except ValueError as value_err:
        print(f"Error: {type(value_err).__name__} {value_err}")
        print()

def video_resolution(link):
    """Set the video resolution using the user link.
    Parameter:
        link: A video link for the Youtube video.
    """
    user_video = YouTube(link)
    return user_video.streams.get_highest_resolution()

def audio_formater(link):
    """Filter just the audio of the Youtube video using the user link.
    Parameter:
        link: A video link for the Youtube video.
    """
    video = YouTube(link)
    return video.streams.filter(only_audio=True).first()

def video_downloader(link_video, save_file):
    """Download the video in the desired resolution using video_resolution() function and
    download() method.
    Parameters:
        link_video: A video link from get_link function to download the Youtube video.
        save_file: The file path were to save the video, or the new file name if entered.
    """
    return video_resolution(link_video).download(save_file)
 

def audio_downloader(link_audio, save_file):
    """Download the audio using audio_formater() function and
    download() method.
    Parameters:
        link_audio: A video link from get_link function to download the Youtube audio.
        save_file: The file path were to save the audio, or the new file name if entered.
    """
    return audio_formater(link_audio).download(save_file)
    
def get_link(link):
    """Returns the user link so it can be tested later.
    Parameter:
        link: A audio link for the Youtube video.
    """
    return link

if __name__ == "__main__":
    main()