from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
from flask import Flask
from flask_restful import Api, Resource

formatter = SRTFormatter()

def transcribe(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    srt_format = formatter.format_transcript(transcript)
    with open('srt.srt', 'w', encoding='utf-8') as srt:
        srt.write(srt_format)

class Transcribe(Resource):
    def get(self, video_id):
        transcribe(video_id)
        with open('srt.srt') as f:
            lines = f.readlines()
        return {"data": lines}

app = Flask(__name__)
api = Api(app)

api.add_resource(Transcribe, "/<string:video_id>")

if __name__ == "__main__":
    app.run(debug = True)