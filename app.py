# youtube_direct_url.py

from yt_dlp import YoutubeDL

def fetch_direct_video_url(youtube_url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'forceurl': True,
        'format': 'best[ext=mp4]'
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            title = info.get("title", "No title")
            direct_url = info.get("url")
            return title, direct_url
    except Exception as e:
        print(f"❌ Error: {e}")
        return None, None

if __name__ == "__main__":
    print("🎬 YouTube Video Direct Link Extractor")
    youtube_url = input("🔗 Enter YouTube Video URL: ").strip()
    title, video_url = fetch_direct_video_url(youtube_url)

    if video_url:
        print(f"\n✅ Title: {title}")
        print(f"🔗 Direct Stream URL: {video_url}")
    else:
        print("❌ Could not extract video URL.")
