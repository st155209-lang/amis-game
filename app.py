"""彼界之靈｜星辰守護之戰 — Streamlit 外殼

把同資料夾的 index.html（單檔遊戲）嵌進 Streamlit 頁面。
遊戲本身是純前端，不需要後端；這個檔案只是讓它能部署在 streamlit.io。
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="彼界之靈｜星辰守護之戰",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 隱藏 Streamlit 預設頁首/頁尾並去掉邊距，讓遊戲盡量佔滿畫面
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

GAME_FILE = Path(__file__).with_name("index.html")


@st.cache_resource(show_spinner="載入遊戲中…")
def load_game() -> str:
    return GAME_FILE.read_text(encoding="utf-8")


# 遊戲高度（像素）。可用網址參數調整，例如 ?h=700
try:
    height = int(st.query_params.get("h", 900))
except (TypeError, ValueError):
    height = 900

components.html(load_game(), height=height, scrolling=False)

# 若已經把遊戲放上 GitHub Pages，也可改用下面這行（頁面較輕量），並刪掉上一行：
# components.iframe("https://<你的帳號>.github.io/<你的repo名稱>/", height=height, scrolling=False)
