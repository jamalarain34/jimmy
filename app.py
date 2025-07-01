import streamlit as st
from PIL import Image, UnidentifiedImageError
import io




# Page config
st.set_page_config(page_title="Image Converter | JamalEditz", layout="centered")

# ====== 🔲 Custom Styling ======
st.markdown("""
    <style>
        .main-box {
            border: 0px solid #f04e23;
            border-radius: 16px;
            padding: 5px 5px;
            background-color: #ffffff;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.08);
        }
        .stButton > button {
            background-color: #f04e23;
            color: white;
            font-weight: bold;
            border: none;
            padding: 0.5rem 1.5rem;
            border-radius: 8px;
            transition: 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #e5390d;
            transform: scale(1.03);
        }
        .stDownloadButton > button {
            background-color: #ff9800;
            color: white;
            font-weight: bold;
            border: none;
            padding: 0.4rem 1.2rem;
            border-radius: 8px;
            margin-bottom: 10px;
            transition: 0.3s ease;
        }
        .stDownloadButton > button:hover {
            background-color: #fb8c00;
            transform: scale(1.02);
        }
        .stSelectbox, .stFileUploader {
            margin-top: 15px;
        }
        .title {
            color: #111111;
            font-size: 30px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 10px;
        }
        .desc {
            text-align: center;
            color: #444;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ====== 💠 Main Content ======
st.markdown('<div class="main-box">', unsafe_allow_html=True)

st.markdown('<div class="title"></div>', unsafe_allow_html=True)
st.markdown('<div class="desc">Convert images into popular formats like PNG, JPEG, WebP and more. Built for creators by <strong>JamalEditz</strong>.</div>', unsafe_allow_html=True)

uploaded_files = st.file_uploader("📁 Upload your images", type=["jpg", "jpeg", "png", "webp", "bmp", "tiff"], accept_multiple_files=True)

formats = ["JPEG", "PNG", "WEBP", "BMP", "TIFF"]
output_format = st.selectbox("🎯 Choose Output Format", formats)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully.")
    if st.button("🔄 Convert Images Now"):
        st.info("Converting... Please wait ⏳")

        for idx, uploaded_file in enumerate(uploaded_files):
            try:
                image = Image.open(uploaded_file).convert("RGB")

                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format=output_format)
                img_byte_arr.seek(0)

                base_name = uploaded_file.name.rsplit('.', 1)[0]
                converted_name = f"{base_name}_converted.{output_format.lower()}"

                st.download_button(
                    label=f"⬇️ Download: {converted_name}",
                    data=img_byte_arr,
                    file_name=converted_name,
                    mime=f"image/{output_format.lower()}",
                    key=f"download_button_{idx}"
                )

            except UnidentifiedImageError:
                st.error(f"❌ Error: '{uploaded_file.name}' is not a valid image or is corrupted.")
            except Exception as e:
                st.error(f"⚠️ Unexpected error with file '{uploaded_file.name}': {str(e)}")
else:
    st.warning("Upload at least one image to begin.")

st.markdown('</div>', unsafe_allow_html=True)
