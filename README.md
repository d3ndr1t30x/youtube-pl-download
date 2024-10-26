Steps to Use yt-dlp

Install yt-dlp: If you haven't already installed yt-dlp, run this command in your command prompt:

```pip install yt-dlp```

Run the Script: Execute the script by typing:

```python downloader.py```

Enter the Playlist URL: When prompted, enter the URL of the YouTube playlist you want to download.

Explanation of the Script

Format: The script uses the option 'format': 'best' to download the highest quality available.
Output Template: The outtmpl parameter saves the downloaded files using the video title as the filename.

Troubleshooting

If you encounter any issues, make sure your command prompt is running with the necessary permissions, and that you have a stable internet connection.
If a video fails to download, yt-dlp will usually skip it and continue downloading the rest.
