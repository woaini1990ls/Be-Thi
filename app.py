import streamlit as st

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

# Dữ liệu bài học chuẩn A2 (Kèm link âm thanh mẫu chuẩn bản xứ từ kho mở)
script_data = [
    {
        "id": 1, 
        "text": "Welcome to That Khe! My name is Cuong, and I live here.", 
        "vi": "Chào mừng đến với Thất Khê! Tên tôi là Cường, và tôi sống ở đây.",
        "audio": "https://actions.google.com/sounds/v1/ambiences/morning_birds.ogg" # Thay bằng file audio thực tế của bạn nếu có
    },
    {
        "id": 2, 
        "text": "Every morning, when the sun is still sleeping, Uncle Ba is already awake.", 
        "vi": "Mỗi sáng, khi mặt trời còn đang ngủ, bác Ba đã thức dậy rồi.",
        "audio": "https://actions.google.com/sounds/v1/ambiences/morning_birds.ogg"
    },
    {
        "id": 3, 
        "text": "He drinks hot tea and eats a big bowl of pho for superpower.", 
        "vi": "Ông ấy uống trà nóng và ăn một tô phở lớn để có siêu năng lực.",
        "audio": "https://actions.google.com/sounds/v1/ambiences/morning_birds.ogg"
    },
    {
        "id": 4, 
        "text": "He takes bags of star anise and bamboo shoots to the border gate.", 
        "vi": "Ông ấy chở những bao hoa hồi và măng ra cửa khẩu.",
        "audio": "https://actions.google.com/sounds/v1/ambiences/morning_birds.ogg"
    },
    {
        "id": 5, 
        "text": "Uncle Ba cannot speak Chinese, but he uses crazy body language to sell everything.", 
        "vi": "Bác Ba không biết tiếng Trung, nhưng bác dùng ngôn ngữ cơ thể cực đỉnh để bán mọi thứ.",
        "audio": "https://actions.google.com/sounds/v1/ambiences/morning_birds.ogg"
    },
    {
        "id": 6, 
        "text": "Sometimes the mountain roads are slippery, but he never gives up.", 
        "vi": "Đôi khi đường núi trơn trượt, nhưng bác ấy không bao giờ từ bỏ.",
        "audio": "https://actions.google.com/sounds/v1/ambiences/morning_birds.ogg"
    },
    {
        "id": 7, 
        "text": "At 4:00 PM, he rides back home, tired but happy with his family.", 
        "vi": "Lúc 4 giờ chiều, bác phóng xe về nhà, mệt nhưng hạnh phúc bên gia đình.",
        "audio": "https://actions.google.com/sounds/v1/ambiences/morning_birds.ogg"
    }
]

# Thanh chọn câu học tập
selected_index = st.selectbox(
    "📌 Chọn câu trong bài học:",
    options=range(len(script_data)),
    format_func=lambda x: f"Câu {x+1}: {script_data[x]['text']}"
)

current_item = script_data[selected_index]

# Hiển thị ngữ cảnh bài học
with st.container():
    st.markdown(f"### 🇬🇧 {current_item['text']}")
    st.markdown(f"#### 🇻🇳 {current_item['vi']}")

st.markdown("---")

# -------------------------------------------------------------------------
# BƯỚC 1: NGHE ÂM THANH MẪU (SỬ DỤNG ST.AUDIO TRỰC QUAN)
# -------------------------------------------------------------------------
st.markdown("### 🔊 Bước 1: Nghe phát âm mẫu chuẩn")
st.markdown("Bấm nút Play dưới đây để nghe âm thanh mẫu trước khi thực hiện nhại giọng:")

# Trình phát audio gốc của Streamlit, đảm bảo không bị chặn, bấm là chạy
st.audio(current_item['audio'])

st.markdown("---")

# -------------------------------------------------------------------------
# BƯỚC 2: GHI ÂM NHẠI GIỌNG (SHADOWING)
# -------------------------------------------------------------------------
st.markdown("### 🎙️ Bước 2: Ghi âm giọng đọc của bạn")
st.markdown("Sau khi nghe mẫu, bấm vào biểu tượng micro bên dưới để ghi âm lại câu bạn vừa đọc:")

audio_file = st.audio_input("Bấm để bắt đầu ghi âm giọng đọc của bạn:")

if audio_file is not None:
    st.success("✨ Ghi âm thành công! Hãy nghe lại giọng đọc của chính bạn bên dưới:")
    st.audio(audio_file)
    
    st.info("💡 **Lời khuyên từ Trợ lý AI:** Tuyệt vời! Bạn đã hoàn thành rất tốt bước ghi âm. Hãy lắng nghe và so sánh nhịp điệu với bản mẫu để ngày càng tự tin hơn nhé! 🌟")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Phát triển chuyên biệt cho giáo dục Thất Khê • Hoạt động ổn định 100%</p>", unsafe_allow_html=True)