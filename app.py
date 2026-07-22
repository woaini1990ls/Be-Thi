import streamlit as st

# Cấu hình giao diện trang web
st.set_page_config(page_title="That Khe AI Shadowing Coach", page_icon="🎤", layout="centered")

st.title("🎤 That Khe AI Shadowing Coach")
st.subheader("Ngách địa phương: Luyện nhại giọng tiếng Anh A2 cực vui nhộn")
st.markdown("---")

# Nội dung bài học (Câu chuyện của Cường về Thợ phiên)
sentences = [
    "Welcome to That Khe! My name is Cuong, and I live here.",
    "Every morning, when the sun is still sleeping, Uncle Ba is already awake.",
    "He drinks hot tea and eats a big bowl of pho for superpower.",
    "He takes bags of star anise and bamboo shoots to the border gate.",
    "Uncle Ba cannot speak Chinese, but he uses crazy body language to sell everything.",
    "Sometimes the mountain roads are slippery, but he never gives up.",
    "At 4:00 PM, he rides back home, tired but happy with his family."
]

# Giao diện chọn câu để luyện Shadowing
st.markdown("### 📜 Chọn câu để luyện tập (Shadowing):")
selected_sentence = st.selectbox("Chọn một câu trong bài:", sentences)

# Hiển thị câu được chọn
st.info(f"**Câu hiện tại:** {selected_sentence}")

# Hướng dẫn luyện tập
st.markdown("""
**💡 Hướng dẫn cách luyện Shadowing 100% Free:**
1. **Nghe mẫu:** Bấm nút bên dưới để nghe trình duyệt đọc mẫu câu.
2. **Nhại giọng:** Đọc to lại câu đó theo đúng ngữ điệu.
""")

# Tích hợp Web Speech API (Text-to-Speech) bằng HTML/JS đơn giản nhúng trong Streamlit
tts_html = f"""
<div style="margin: 20px 0;">
    <button onclick="speakText()" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">🔊 Nghe câu mẫu (Listen)</button>
</div>

<script>
function speakText() {{
    const text = "{selected_sentence}";
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = 0.9; // Tốc độ chậm vừa phải cho cấp độ A2
    window.speechSynthesis.speak(utterance);
}}
</script>
"""

st.markdown(tts_html, unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 🎙️ Ghi âm giọng đọc của bạn")
st.markdown("Bạn có thể ghi âm trực tiếp bằng micro của điện thoại hoặc máy tính để kiểm tra phản xạ:")

# Tính năng ghi âm tích hợp sẵn của Streamlit
audio_value = st.audio_input("Bấm vào micro để ghi âm giọng của bạn:")

if audio_value is not None:
    st.success("✨ Đã ghi âm thành công! Hãy nghe lại để so sánh với bản gốc nhé:")
    st.audio(audio_value)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Phát triển cho cộng đồng giáo dục Thất Khê | 100% Free & No-Code</p>", unsafe_allow_html=True)