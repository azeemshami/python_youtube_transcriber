import re

def getVideoId(youtubeUrl):
    videoIdRegex = r'(?:v=|/)([0-9A-Za-z_-]{11}).*'
    match = re.search(videoIdRegex, youtubeUrl)

    if match:
        return match.group(1)
    else:
        return None
