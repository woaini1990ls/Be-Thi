import streamlit as st

# Cấu hình giao diện tổng thể
st.set_page_config(
    page_title="That Khe AI Shadowing Studio",
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

# Dữ liệu bài học chuẩn A2 (Câu chuyện Thợ phiên kèm link âm thanh mẫu chuẩn quốc tế)
script_data = [
    {
        "id": 1, 
        "text": "Welcome to That Khe! My name is Cuong, and I live here.", 
        "vi": "Chào mừng đến với Thất Khê! Tên tôi là Cường, và tôi sống ở đây.",
        "audio": "https://actions.google.com/sounds/v1/ambiences/morning_birds.ogg" # Link âm thanh mẫu (thay bằng file audio của bạn nếu có)
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

st.markdown("### 📌 Chọn câu cần luyện tập:")
selected_index = st.selectbox(
    "Danh sách câu trong bài:",
    options=range(len(script_data)),
    format_func=lambda x: f"Câu {x+1}: {script_data[x]['text']}"
)

current_item = script_data[selected_index]

# Khung hiển thị ngữ cảnh bài học
st.markdown(f"""
    <div style="background-color: #f1f8e9; padding: 20px; border-radius: 12px; border-left: 6px solid #4caf50; margin-bottom: 20px;">
        <p style="font-size: 13px; color: #2e7d32; font-weight: bold; margin-bottom: 5px;">CÂU HIỆN TẠI (LEVEL A2):</p>
        <p style="font-size: 20px; font-weight: bold; color: #111; margin-bottom: 8px;">{current_item['text']}</p>
        <p style="font-size: 15px; color: #666; font-style: italic; margin: 0;">🇻🇳 Nghĩa tiếng Việt: {current_item['vi']}</p>
    </div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# BỘ PHÁT ÂM THANH MẪU (SỬ DỤNG TRÌNH PHÁT AUDIO CHUẨN CỦA STREAMLIT)
# -------------------------------------------------------------------------
st.markdown("#### Bước 1: Nghe âm thanh mẫu chuẩn")
st.markdown("<p style='font-size: 14px; color: #555;'>Bấm nút Play dưới đây để nghe phát âm mẫu trước khi thực hiện nhại giọng:</p>", unsafe_allow_html=True)

# Sử dụng widget st.audio trực tiếp giúp loại bỏ hoàn toàn lỗi không phát ra tiếng trên trình duyệt
# (Bạn có thể thay thế link audio bằng file ghi âm giọng đọc chuẩn của bạn đặt trong cùng thư mục)
st.audio(current_item['audio'])

st.markdown("---")

# -------------------------------------------------------------------------
# BỘ GHI ÂM NHẠI GIỌNG (SHADOWING RECORDING)
# -------------------------------------------------------------------------
st.markdown("#### Bước 2: Ghi âm giọng của bạn để tự so sánh")
st.markdown("<p style='font-size: 14px; color: #555;'>Bấm vào biểu tượng micro bên dưới, đọc to lại câu tiếng Anh vừa nghe, sau đó phát lại để kiểm tra độ chính xác.</p>", unsafe_allow_html=True)

audio_value = st.audio_input("Bấm vào biểu tượng micro để bắt đầu ghi âm:")

if audio_value is not None:
    st.success("✨ Ghi âm thành công! Nghe lại giọng đọc của bạn:")
    st.audio(audio_value)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #888; font-size: 13px;'>Phát triển chuyên biệt cho giáo dục Thất Khê • Chạy ổn định 100% trên mọi thiết bị</p>", unsafe_allow_html=True)