import streamlit as st
import json

# Cấu hình giao diện tổng thể
st.set_page_config(
    page_title="That Khe AI Shadowing Coach",
    page_icon="🎓",
    layout="centered"
)

# Giao diện Tiêu đề trang trọng, sinh động
st.markdown("""
    <div style='text-align: center; padding: 10px;'>
        <h1 style='color: #1b5e20; margin-bottom: 5px;'>🎓 That Khe AI Shadowing Studio</h1>
        <p style='color: #555; font-size: 16px;'>Nền tảng luyện phát âm tương tác thông minh • Câu chuyện Thợ phiên Thất Khê</p>
    </div>
    <hr style='border: 1px solid #c8e6c9;'>
""", unsafe_allow_html=True)

# Dữ liệu bài học chuẩn A2 (Câu chuyện Thợ phiên)
script_data = [
    {"id": 1, "text": "Welcome to That Khe! My name is Cuong, and I live here.", "vi": "Chào mừng đến với Thất Khê! Tên tôi là Cường, và tôi sống ở đây."},
    {"id": 2, "text": "Every morning, when the sun is still sleeping, Uncle Ba is already awake.", "vi": "Mỗi sáng, khi mặt trời còn đang ngủ, bác Ba đã thức dậy rồi."},
    {"id": 3, "text": "He drinks hot tea and eats a big bowl of pho for superpower.", "vi": "Ông ấy uống trà nóng và ăn một tô phở lớn để có siêu năng lực."},
    {"id": 4, "text": "He takes bags of star anise and bamboo shoots to the border gate.", "vi": "Ông ấy chở những bao hoa hồi và măng ra cửa khẩu."},
    {"id": 5, "text": "Uncle Ba cannot speak Chinese, but he uses crazy body language to sell everything.", "vi": "Bác Ba không biết tiếng Trung, nhưng bác dùng ngôn ngữ cơ thể cực đỉnh để bán mọi thứ."},
    {"id": 6, "text": "Sometimes the mountain roads are slippery, but he never gives up.", "vi": "Đôi khi đường núi trơn trượt, nhưng bác ấy không bao giờ từ bỏ."},
    {"id": 7, "text": "At 4:00 PM, he rides back home, tired but happy with his family.", "vi": "Lúc 4 giờ chiều, bác phóng xe về nhà, mệt nhưng hạnh phúc bên gia đình."}
]

# Sidebar hoặc bộ chọn câu tập trung
st.markdown("### 📌 Chọn câu cần luyện tập:")
selected_index = st.selectbox(
    "Danh sách câu trong bài:",
    options=range(len(script_data)),
    format_func=lambda x: f"Câu {x+1}: {script_data[x]['text']}"
)

current_item = script_data[selected_index]

# Khung hiển thị ngữ cảnh bài học hiện đại
st.markdown(f"""
    <div style="background-color: #f1f8e9; padding: 20px; border-radius: 12px; border-left: 6px solid #4caf50; margin-bottom: 20px;">
        <p style="font-size: 13px; color: #2e7d32; font-weight: bold; margin-bottom: 5px;">CÂU HIỆN TẠI (LEVEL A2):</p>
        <p style="font-size: 20px; font-weight: bold; color: #111; margin-bottom: 8px;">{current_item['text']}</p>
        <p style="font-size: 15px; color: #666; font-style: italic; margin: 0;">🇻🇳 Nghĩa tiếng Việt: {current_item['vi']}</p>
    </div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# BỘ ĐIỀU KHIỂN ÂM THANH MẪU (TEXT-TO-SPEECH CHUẨN XÁC)
# -------------------------------------------------------------------------
st.markdown("#### Bước 1: Nghe âm thanh mẫu chuẩn từ AI")

tts_code = f"""
<div style="margin-bottom: 20px;">
    <button onclick="playAudioSample()" style="background-color: #2e7d32; color: white; padding: 12px 24px; border: none; border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: bold; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">
        🔊 Nghe mẫu phát âm
    </button>
    <span id="audio-status" style="margin-left: 15px; font-weight: bold; color: #d32f2f;"></span>
</div>

<script>
function playAudioSample() {{
    const text = "{current_item['text']}";
    const statusEl = document.getElementById("audio-status");
    
    if (!('speechSynthesis' in window)) {{
        alert("Trình duyệt của bạn không hỗ trợ phát âm thanh trực tiếp!");
        return;
    }}
    
    window.speechSynthesis.cancel(); // Dừng các luồng cũ
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = 0.85; // Tốc độ chuẩn chậm cho người học A2
    
    utterance.onstart = function() {{
        statusEl.style.color = "#2e7d32";
        statusEl.innerText = " đang phát âm mẫu...";
    }};
    
    utterance.onend = function() {{
        statusEl.style.color = "#1976d2";
        statusEl.innerText = " Hoàn tất! Hãy chuyển xuống dưới để ghi âm nhại giọng.";
    }};
    
    window.speechSynthesis.speak(utterance);
}}
</script>
"""

st.markdown(tts_code, unsafe_allow_html=True)

st.markdown("---")

# -------------------------------------------------------------------------
# BỘ GHI ÂM NHẠI GIỌNG (SHADOWING RECORDING)
# -------------------------------------------------------------------------
st.markdown("#### Bước 2: Ghi âm giọng của bạn để tự so sánh")
st.markdown("<p style='font-size: 14px; color: #555;'>Hãy bấm vào nút micro bên dưới, đọc to lại câu tiếng Anh vừa nghe, sau đó phát lại để kiểm tra độ chính xác.</p>", unsafe_allow_html=True)

audio_value = st.audio_input("Bấm vào biểu tượng micro để bắt đầu ghi âm:")

if audio_value is not None:
    st.success("✨ Ghi âm thành công! Nghe lại giọng đọc của bạn:")
    st.audio(audio_value)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #888; font-size: 13px;'>Phát triển chuyên biệt cho giáo dục Thất Khê • Chạy ổn định 100% trên mọi thiết bị</p>", unsafe_allow_html=True)