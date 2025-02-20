from fastapi import APIRouter
from youtube_transcript_api import YouTubeTranscriptApi
from utils import getVideoId

router = APIRouter(prefix="/youtube", tags=["Youtube"], responses={404: {"description": "Not found"}})

@router.post("/transcribe")
async def transcribe(data: dict):
    youtubeUrl = data['video_url']

    if youtubeUrl is None:
        return {"message": "Invalid YouTube URL"}

    videoId = getVideoId(youtubeUrl)
    if videoId is None:
        return {"message": "Invalid YouTube URL"}

    transcript = YouTubeTranscriptApi.get_transcript(videoId)
    text_list = [transcript[i]['text'] for i in range(len(transcript))]
    transcript_text = 'n'.join(text_list)
    return {"message": "Success", "transcript_text":transcript_text}
