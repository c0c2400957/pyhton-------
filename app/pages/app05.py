import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# 1. タイトル（実習共通のスタイルを踏襲）
st.title("社会情報プロジェクト実習I")

# ヘッダーと紹介文
st.header("🐱 世界のオシャレな猫種カタログ")
st.write("独特の毛並みや美しいシルエットを持つ、魅力的な猫種をあつめました。")

st.markdown("---")

# 2. 画面設計（st.columns を使って左右に綺麗に配置）
st.subheader("✨ 注目の猫種紹介")

# --- 1種類目：ロシアンブルー ---
col1, col2 = st.columns([2, 1])  # 比率を 2:1 にして文章を広めに
with col1:
    st.markdown("### 💎 ロシアンブルー (Russian Blue)")
    st.write(
        "「冬の精霊」とも呼ばれる、美しい銀灰色の毛並み（ブルー）と、鮮やかなエメラルドグリーンの瞳が特徴です。 "
        "静かで賢く、飼い主に従順な「ボイスレスキャット（鳴き声の静かな猫）」としても知られています。"
    )
with col2:
    # 画像の読み込みと表示
    img1 = Image.open("app/data/russian_blue.jpg")
    st.image(img1, caption="気品漂うロシアンブルー", use_container_width=True)

st.markdown("---")

# --- 2種類目：アビシニアン ---
col3, col4 = st.columns([2, 1])
with col3:
    st.markdown("### ☀️ アビシニアン (Abyssinian)")
    st.write(
        "エジプトの壁画に描かれた猫に似ているとされる、高貴な歴史を持つ猫種です。 "
        "1本の毛に複数の色が混ざるグラデーション（ティング）が美しく、非常に活発で知的な性格をしています。"
    )
with col4:
    img2 = Image.open("app/data/abyssinian.jpg")
    st.image(img2, caption="スタイリッシュな立ち姿のアビシニアン", use_container_width=True)

st.markdown("---")

# --- 3種類目：ベンガル ---
col5, col6 = st.columns([2, 1])
with col5:
    st.markdown("### 🐆 ベンガル (Bengal)")
    st.write(
        "野生のヤマネコのようなワイルドでオシャレな豹柄（ロゼット）が特徴の猫種です。 "
        "見た目のたくましさに反して、とても人懐っこく、猫としては珍しく水遊びが好きな一面もあります。"
    )
with col6:
    img3 = Image.open("app/data/bengal.jpg")
    st.image(img3, caption="ワイルドな美しさを持つベンガル", use_container_width=True)

st.markdown("---")


# 3. データ分析要素の融合（app02, app04 の応用）
st.subheader("📊 猫種の特徴をデータで比較")

# 猫種データの作成（Pandas DataFrame）
data = {
    "猫種": ["ロシアンブルー", "アビシニアン", "ベンガル"],
    "平均体重 (kg)": [4.0, 3.5, 5.5],
    "活発さ (5段階)": [2, 5, 5],
    "甘えん坊度 (5段階)": [4, 4, 3]
}
df = pd.DataFrame(data)

# データフレームの表示
st.write("💡 各猫種のスペック一覧：")
st.dataframe(df, use_container_width=True)

# Plotlyによるオシャレなインタラクティブ散布図
fig = px.scatter(
    df,
    x="活発さ (5段階)",
    y="甘えん坊度 (5段階)",
    size="平均体重 (kg)",
    color="猫種",
    hover_data=["平均体重 (kg)"],
    title="猫種の性格・サイズ分布マップ",
    range_x=[0, 6],
    range_y=[0, 6]
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")


# 4. インタラクティブなアクション（app01 の応用）
st.subheader("💟 あなたの推し猫は？")
choice = st.radio("一番お気に入りの猫種を選んでください：", ("ロシアンブルー", "アビシニアン", "ベンガル"))
btn = st.button("投票する")

if btn:
    # 投票が押されたら、ちょっとオシャレな緑色のボックスでメッセージを表示
    st.success(f"「{choice}」への投票ありがとうございました！🐾")