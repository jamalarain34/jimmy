# youtube_direct_url_streamlit.py
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
            color: #444;
        }
        .stButton > button {
            background-color: #f04e23;
            color: white;
            font-weight: bold;
            border: none;
            padding: 0.6rem 1.5rem;
            border-radius: 8px;
            transition: 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #e5390d;
            transform: scale(1.03);
        }
        .result-box {
            border: 2px solid #f04e23;
            border-radius: 10px;
            padding: 20px;
            background: #fff9f4;
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
            return title, direct_url
    except Exception as e:
        return None, None

# ========== 🧠 Streamlit UI ==========
st.markdown('<div class="title">🎬 YouTube Video Direct Link Tool</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">Paste your YouTube URL and get the direct video stream link.</div>', unsafe_allow_html=True)

youtube_url = st.text_input("🔗 Enter YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")

if st.button("🎯 Get Direct Link"):
    if youtube_url:
        with st.spinner("🔍 Fetching video URL..."):
            title, video_url = fetch_direct_video_url(youtube_url)

        if video_url:
            st.markdown(f"""
                <div class='result-box'>
                    <h4>✅ Title: {title}</h4>
                    <a href='{video_url}' target='_blank'>
                        <button style='margin-top:10px;'>⬇️ Open Direct Video Link</button>
                    </a>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Could not extract video URL. Please check the link.")
    else:
        st.warning("Please paste a YouTube video URL to continue.")
