import yt_dlp

def download_playlist(playlist_url):
    # Set up options for yt-dlp
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',  # Save files with the title as the filename
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    url = input("Enter the YouTube playlist URL: ")
    download_playlist(url)
