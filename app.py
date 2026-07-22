import streamlit as st

# Cấu hình giao diện trang web
st.set_page_config(page_title="That Khe AI Shadowing & Video Coach", page_icon="🎬", layout="centered")

st.title("🎬 That Khe AI Shadowing & Video Coach")
st.subheader("Ngách địa phương: Luyện nhại giọng kèm Video bối cảnh Thất Khê")
st.markdown("---")

# Danh sách câu chuyện kèm theo liên kết video minh họa trực quan (Sử dụng video mẫu chuẩn)
story_data = [
    {
        "sentence": "Welcome to That Khe! My name is Cuong, and I live here.",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4" # Thay link video thực tế của bạn vào đây
    },
    {
        "sentence": "Every morning, when the sun is still sleeping, Uncle Ba is already awake.",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4"
    },
    {
        "sentence": "He drinks hot tea and eats a big bowl of pho for superpower.",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4"
    },
    {
        "sentence": "He takes bags of star anise and bamboo shoots to the border gate.",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4"
    },
    {
        "sentence": "Uncle Ba cannot speak Chinese, but he uses crazy body language to sell everything.",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4"
    },
    {
        "sentence": "Sometimes the mountain roads are slippery, but he never gives up.",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4"
    },
    {
        "sentence": "At 4:00 PM, he rides back home, tired but happy with his family.",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4"
    }
]

# Giao diện chọn câu
sentence_list = [item["sentence"] for item in story_data]
selected_sentence = st.selectbox("📜 Chọn câu trong câu chuyện của Cường:", sentence_list)

# Tìm dữ liệu tương ứng với câu được chọn
current_item = next(item for item in story_data if item["sentence"] == selected_sentence)

st.info(f"**Câu hiện tại:** {selected_sentence}")

# Hiển thị Video minh họa bối cảnh ngay lập tức không cần chờ đợi
st.markdown("### 🎥 Video bối cảnh minh họa:")
st.video(current_item["video_url"])

st.markdown("---")

# Tích hợp Web Speech API (Text-to-Speech) để nghe câu mẫu
tts_html = f"""
<div style="margin: 20px 0;">
    <button onclick="speakText()" style="background-color: #2e7d32; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">🔊 Nghe câu mẫu (Listen)</button>
</div>

<script>
function speakText() {{
    const text = "{selected_sentence}";
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = 0.9;
    window.speechSynthesis.speak(utterance);
}}
</script>
"""
st.markdown(tts_html, unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 🎙️ Ghi âm giọng đọc của bạn để luyện Shadowing")
audio_value = st.audio_input("Bấm vào micro để ghi âm:")
if audio_value is not None:
    st.success("✨ Đã ghi âm thành công!")
    st.audio(audio_value)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Hệ thống Web Luyện Ngữ Điệu AI thông minh | 100% Free Cloud</p>", unsafe_allow_html=True)