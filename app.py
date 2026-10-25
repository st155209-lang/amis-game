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
# 同時加入開發者標語的浮動樣式（可自由選擇開啟）
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      
      /* 如果你想讓標語精緻地固定在網頁右下角，可以使用下方的 CSS 樣式 */
      .developer-badge {
          position: fixed;
          bottom: 10px;
          right: 15px;
          background-color: rgba(0, 0, 0, 0.6);
          color: #ffffff;
          padding: 5px 12px;
          border-radius: 20px;
          font-size: 13px;
          font-family: sans-serif;
          z-index: 9999;
          pointer-events: none;
          letter-spacing: 1px;
      }
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

# 1. 載入並渲染 HTML 遊戲
components.html(load_game(), height=height, scrolling=False)

# 2. 新增開發者標語
# 做法 A：直接顯示在遊戲下方（乾淨、直覺）
st.markdown(
    "<p style='text-align: center; color: #888888; font-size: 14px; margin-top: 10px;'>🛠️ 開發者：信諺 Hanata</p>", 
    unsafe_allow_html=True
)

# 做法 B：如果你想讓標語「浮動固定在畫面右下角」（像專業遊戲的浮水印），請把下面這行的 # 註解拿掉：
# st.markdown('<div class="developer-badge">🛠️ 開發者：＊＊＊</div>', unsafe_allow_html=True)

# 若已經把遊戲放上 GitHub Pages，也可改用下面這行（頁面較輕量），並刪掉第 47 行的 components.html：
# components.iframe("https://<你的帳號>.github.io/<你的repo名稱>/", height=height, scrolling=False)
