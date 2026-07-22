import streamlit as st
import time

# Cấu hình giao diện trang web
st.set_page_config(
    page_title="That Khe AI Shadowing Studio",
    page_icon="🎓",
    layout="centered"
)

# Tiêu đề ứng dụng
st.title("🎓 That Khe AI Shadowing Studio")
st.subheader("Nền tảng luyện phát âm tiếng Anh A2 • Chuyện Thợ phiên Thất Khê")
st.markdown("---")

# Dữ liệu bài học chuẩn A2 (Câu chuyện Thợ phiên)
script_data = [
    {
        "id": 1, 
        "text": "Welcome to That Khe! My name is Cuong, and I live here.", 
        "vi": "Chào mừng đến với Thất Khê! Tên tôi là Cường, và tôi sống ở đây.",
        "scene": "Cảnh toàn thị trấn Thất Khê buổi sớm bình minh."
    },
    {
        "id": 2, 
        "text": "Every morning, when the sun is still sleeping, Uncle Ba is already awake.", 
        "vi": "Mỗi sáng, khi mặt trời còn đang ngủ, bác Ba đã thức dậy rồi.",
        "scene": "Cảnh sáng sớm trời chưa sáng, bác Ba lục đục thức dậy."
    },
    {
        "id": 3, 
        "text": "He drinks hot tea and eats a big bowl of pho for superpower.", 
        "vi": "Ông ấy uống trà nóng và ăn một tô phở lớn để có siêu năng lực.",
        "scene": "Cảnh tô phở nóng hổi nghi ngút khói buổi sáng."
    },
    {
        "id": 4, 
        "text": "He takes bags of star anise and bamboo shoots to the border gate.", 
        "vi": "Ông ấy chở những bao hoa hồi và măng ra cửa khẩu.",
        "scene": "Cảnh chở hàng hóa đặc sản hoa hồi và măng tre ra cửa khẩu."
    },
    {
        "id": 5, 
        "text": "Uncle Ba cannot speak Chinese, but he uses crazy body language to sell everything.", 
        "vi": "Bác Ba không biết tiếng Trung, nhưng bác dùng ngôn ngữ cơ thể cực đỉnh để bán mọi thứ.",
        "scene": "Cảnh trao đổi mua bán sôi nổi bằng ngôn ngữ cơ thể."
    },
    {
        "id": 6, 
        "text": "Sometimes the mountain roads are slippery, but he never gives up.", 
        "vi": "Đôi khi đường núi trơn trượt, nhưng bác ấy không bao giờ từ bỏ.",
        "scene": "Cảnh đường đèo núi mờ sương, di chuyển thận trọng."
    },
    {
        "id": 7, 
        "text": "At 4:00 PM, he rides back home, tired but happy with his family.", 
        "vi": "Lúc 4 giờ chiều, bác phóng xe về nhà, mệt nhưng hạnh phúc bên gia đình.",
        "scene": "Cảnh bữa cơm gia đình đầm ấm quây quần lúc chiều tà."
    }
]

# Thanh chọn câu học tập
selected_index = st.selectbox(
    "📌 Chọn câu trong bài học:",
    options=range(len(script_data)),
    format_func=lambda x: f"Câu {x+1}: {script_data[x]['text']}"
)

current_item = script_data[selected_index]

# Hiển thị khung nội dung chính bằng Native Container của Streamlit
with st.container():
    st.info(f"**🎬 Bối cảnh:** {current_item['scene']}")
    st.markdown(f"### 🇬🇧 {current_item['text']}")
    st.markdown(f"#### 🇻🇳 {current_item['vi']}")

st.markdown("---")

# -------------------------------------------------------------------------
# BỘ PHÁT ÂM THANH MẪU TRỰC QUAN (SỬ DỤNG WEB SPEECH API CHUẨN)
# -------------------------------------------------------------------------
st.markdown("### 🔊 Bước 1: Nghe phát âm mẫu")
st.markdown("Bấm nút bên dưới để trình duyệt đọc mẫu câu chuẩn A2:")

# Tích hợp JavaScript thông qua thành phần thành phần độc lập, an toàn tuyệt đối
tts_code = f"""
<div style="margin: 10px 0;">
    <button onclick="playAudio()" style="background-color: #2e7d32; color: white; padding: 12px 24px; border: none; border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: bold;">
        ▶️ Nghe Mẫu Phát Âm
    </button>
</div>

<script>
function playAudio() {{
    const text = "{current_item['text']}";
    if (!('speechSynthesis' in window)) {{
        alert("Trình duyệt không hỗ trợ phát âm!");
        return;
    }}
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = 0.85; // Tốc độ chuẩn chậm vừa phải
    window.speechSynthesis.speak(utterance);
}}
</script>
"""
st.components.v1.html(tts_code, height=70)

st.markdown("---")

# -------------------------------------------------------------------------
# BỘ GHI ÂM NHẠI GIỌNG (SHADOWING RECORDING)
# -------------------------------------------------------------------------
st.markdown("### 🎙️ Bước 2: Ghi âm nhại giọng (Shadowing)")
st.markdown("Sau khi nghe mẫu, bấm vào biểu tượng micro bên dưới để ghi âm lại giọng đọc của bạn và kiểm tra trực tiếp:")

audio_value = st.audio_input("Ghi âm giọng của bạn:")

if audio_value is not None:
    st.success("✨ Đã ghi âm thành công! Phát lại để kiểm tra đối chiếu:")
    st.audio(audio_value)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Hệ thống Luyện Giọng Tối Ưu • Chạy ổn định 100% trên Streamlit Cloud</p>", unsafe_allow_html=True)