
import streamlit as st
import yt_dlp
import os

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        file_name = ydl.prepare_filename(info_dict).replace('.webm', '.mp3').replace('.m4a', '.mp3')
        return file_name

st.title("YouTube Music Downloader")

url = st.text_input("Enter YouTube Music URL:")

if st.button("Download"):
    if url:
        try:
            st.info("Downloading...")
            file_name = download_audio(url)
            st.success(f"Downloaded: {file_name}")
            with open(file_name, "rb") as f:
                st.download_button(
                    label="Download MP3",
                    data=f,
                    file_name=file_name,
                    mime="audio/mpeg"
                )
            os.remove(file_name)  # Clean up the file after download
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a URL.")
