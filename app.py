import streamlit as st
from yt_dlp import YoutubeDL

# ========== 💠 Theme Styling for JamalEditz ==========
st.set_page_config(page_title="YouTube Direct URL | JamalEditz", layout="centered")

st.markdown("""
    <style>
        body { background-color: white; }
        .title {
            color: #f04e23;
            font-size: 28px;
            font-weight: 700;
            text-align: center;
            margin-top: 20px;
        }
        .desc {
            text-align: center;
            font-size: 16px;
            margin-bottom: 30px;
            color: green;
        }
        .stButton > button {
            background-color: #2ecc71;
            color: white;
            font-weight: bold;
            border: none;
            padding: 0.6rem 1.5rem;
            border-radius: 8px;
            transition: 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #27ae60;
            color: white;
            transform: scale(1.03);
        }
        .result-box {
            border: 2px solid #2ecc71;
            border-radius: 10px;
            padding: 20px;
            background: #f0fff5;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# ========== 🚀 YouTube Direct Link Extractor Logic ==========
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
            thumbnail = info.get("thumbnail")
            return title, direct_url, thumbnail
    except Exception as e:
        return None, None, None

# ========== 🧠 Streamlit UI ==========
st.markdown('<div class="title">🎬 YouTube Video Downloader</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">Paste your YouTube URL and get the direct video stream link with thumbnail.</div>', unsafe_allow_html=True)

youtube_url = st.text_input("🔗 Enter YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")

if st.button("🎯 Get The Video"):
    if youtube_url:
        with st.spinner("🔍 Fetching video URL..."):
            title, video_url, thumbnail = fetch_direct_video_url(youtube_url)

        if video_url:
            st.markdown(f"""
                <div class='result-box'>
                    <img src='{thumbnail}' width='100%' style='border-radius: 8px; margin-bottom: 15px;'>
                    <h4>✅ Title: {title}</h4>
                    <a href='{video_url}' target='_blank'>
                        <button style='margin-top:10px; background-color: #2ecc71;'>⬇️ Download Video Now</button>
                    </a>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Could not extract video URL. Please check the link.")
    else:
        st.warning("Please paste a YouTube video URL to continue.")
