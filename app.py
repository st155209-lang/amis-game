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

# 隱藏 Streamlit 預設頁首/頁尾並去掉邊距
# 同時加入兩側懸浮標語的專屬樣式
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      
      /* 通用側邊標語樣式 */
      .side-badge {
          position: fixed;
          top: 50%;               /* 置於畫面垂直中間 */
          transform: translateY(-50%); /* 精準垂直居中 */
          background-color: rgba(0, 0, 0, 0.6); /* 半透明黑色背景 */
          color: #ffffff;         /* 白色文字 */
          padding: 12px 6px;      /* 內邊距 */
          font-size: 13px;
          font-family: sans-serif;
          z-index: 9999;          /* 確保顯示在最上層 */
          pointer-events: none;   /* 滑鼠滑過時穿透，不干擾點擊 */
          writing-mode: vertical-rl; /* 讓文字由上至下垂直排列 */
          letter-spacing: 2px;    /* 字距直排較美觀 */
          border-radius: 4px;     /* 稍微圓角 */
      }
      
      /* 左側標語定位與左邊圓角 */
      .badge-left {
          left: 0;
          border-radius: 0 4px 4px 0;
      }
      
      /* 右側標語定位與右邊圓角 */
      .badge-right {
          right: 0;
          border-radius: 4px 0 0 4px;
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

# 2. 渲染兩側的懸浮標語
# 左側標語：顯示開發者名稱
st.markdown('<div class="side-badge badge-left">❤️❤️❤️ 開發者：Hanata 信諺</div>', unsafe_allow_html=True)

# 右側標語：可以寫遊戲名稱、版本號或警語（文字可自由修改）
st.markdown('<div class="side-badge badge-right">🎮 彼界之靈｜星辰守護之戰</div>', unsafe_allow_html=True)

# 若已經把遊戲放上 GitHub Pages，也可改用下面這行（頁面較輕量），並刪掉第 67 行的 components.html：
# components.iframe("https://<你的帳號>.github.io/<你的repo名稱>/", height=height, scrolling=False)
