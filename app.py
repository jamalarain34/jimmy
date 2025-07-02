# flask_app_youtube.py
from flask import Flask, render_template, request
import yt_dlp

app = Flask(__name__)

def fetch_direct_video_url(youtube_url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'forceurl': True,
        'format': 'best[ext=mp4]'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            title = info.get("title", "No title")
            direct_url = info.get("url")
            return title, direct_url
    except Exception as e:
        print("Error:", e)
        return None, None

@app.route('/', methods=['GET', 'POST'])
def index():
    title = None
    video_url = None
    error = None

    if request.method == 'POST':
        youtube_url = request.form.get('youtube_url')
        title, video_url = fetch_direct_video_url(youtube_url)
        if not video_url:
            error = "❌ Could not extract video. Please check the URL."

    return render_template('youtube.html', title=title, video_url=video_url, error=error)

if __name__ == '__main__':
    app.run(debug=True)
