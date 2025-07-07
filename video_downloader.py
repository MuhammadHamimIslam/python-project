import yt_dlp
import logging 

# configure logging 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def download_video(url, path="."): 
    """ download a single video with basic options """
    ydl_opts = {
        "outtmpl": f"{path}/%(title)s.%(ext)s",
        "format": "best[height<=1080]"
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl: 
        try:
            ydl.download([url])
            logger.info("Successfully downloaded the video")
        except Exception as e:
            logger.error(f"Error downloading video {url}: {str(e)}")
    
url = input("Enter url: ").strip()

download_video(url)