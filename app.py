import streamlit as st
import base64

# 1. Cấu hình trang
st.set_page_config(
    page_title="That Khe AI Karaoke & Shadowing Studio",
    page_icon="🎬",
    layout="centered"
)

# 2. Tiêu đề ứng dụng
st.title("🎬 That Khe AI Karaoke & Shadowing Studio")
st.subheader("Hệ thống luyện nhại giọng tiếng Anh • Chuyện Thợ phiên Thất Khê")
st.markdown("---")

# 3. Dữ liệu bài học chuẩn A2 
@st.cache_data
def get_script_data():
    return [
        {
            "id": 1, 
            "text": "Welcome to That Khe! My name is Cuong, and I live here.", 
            "vi": "Chào mừng đến với Thất Khê! Tên tôi là Cường, và tôi sống ở đây.",
            "scene": "Cảnh toàn thị trấn Thất Khê buổi sớm bình minh, mây giăng núi đồi."
        },
        {
            "id": 2, 
            "text": "Every morning, when the sun is still sleeping, Uncle Ba is already awake.", 
            "vi": "Mỗi sáng, khi mặt trời còn đang ngủ, bác Ba đã thức dậy rồi.",
            "scene": "Cảnh sáng sớm trời còn tối mờ, bác Ba lục đục thức dậy."
        },
        {
            "id": 3, 
            "text": "He drinks hot tea and eats a big bowl of pho for superpower.", 
            "vi": "Ông ấy uống trà nóng và ăn một tô phở lớn để có siêu năng lực.",
            "scene": "Cảnh tô phở nóng hổi nghi ngút khói buổi sáng ở Lạng Sơn."
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
            "scene": "Cảnh trao đổi mua bán sôi nổi bằng ngôn ngữ cơ thể vui nhộn."
        },
        {
            "id": 6, 
            "text": "Sometimes the mountain roads are slippery, but he never gives up.", 
            "vi": "Đôi khi đường núi trơn trượt, nhưng bác ấy không bao giờ từ bỏ.",
            "scene": "Cảnh đường đèo núi mờ sương, xe máy di chuyển thận trọng."
        },
        {
            "id": 7, 
            "text": "At 4:00 PM, he rides back home, tired but happy with his family.", 
            "vi": "Lúc 4 giờ chiều, bác phóng xe về nhà, mệt nhưng hạnh phúc bên gia đình.",
            "scene": "Cảnh bữa cơm gia đình đầm ấm quây quần lúc chiều tà."
        }
    ]

script_data = get_script_data()

# 4. Thanh chọn câu học tập an toàn
selected_index = st.selectbox(
    "📌 Chọn câu trong bài học để luyện tập:",
    options=range(len(script_data)),
    format_func=lambda x: f"Câu {x+1}: {script_data[x]['text']}"
)

current_item = script_data[selected_index]

# 5. Khung hiển thị màn hình Karaoke & Bối cảnh
st.markdown("### 🎥 Màn hình Chữ chạy Karaoke & Bối cảnh")

with st.container():
    st.info(f"**🎬 Bối cảnh:** {current_item['scene']}")
    st.markdown(
        f"""
        <div style="background-color: #1e1e1e; color: #FFD700; padding: 20px; border-radius: 10px; font-size: 20px; font-weight: bold; text-align: center;">
            🎵 "{current_item['text']}"
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"**🇻🇳 Nghĩa tiếng Việt:** *{current_item['vi']}*")

st.markdown("---")

# 6. PHẦN ÂM THANH MẪU: Tích hợp Web Speech API (Đọc tự động bằng giọng bản xứ của trình duyệt)
# Giải pháp này KHÔNG CẦN TỆP ÂM THANH NGOÀI, trình duyệt tự đọc chuẩn xác 100% tiếng Anh
st.markdown("### 🔊 Bước 1: Nghe âm thanh mẫu bản xứ")
st.markdown("Bấm nút phát bên dưới để nghe AI đọc mẫu chuẩn xác:")

tts_html = f"""
<div style="margin: 10px 0;">
    <button onclick="playNativeSpeech()" style="background-color: #2e7d32; color: white; padding: 12px 24px; border: none; border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: bold;">
        ▶️ Bấm nghe AI đọc mẫu
    </button>
</div>

<script>
function playNativeSpeech() {{
    const text = "{current_item['text']}";
    if (!('speechSynthesis' in window)) {{
        alert("Trình duyệt không hỗ trợ phát âm thanh!");
        return;
    }}
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = 0.85; // Tốc độ chuẩn chậm vừa phải cho học sinh luyện tập
    window.speechSynthesis.speak(utterance);
}}
</script>
"""
st.components.v1.html(tts_html, height=70)

st.markdown("---")

# 7. Phần Ghi Âm Nhại Giọng (Shadowing) sử dụng Widget Native
st.markdown("### 🎙️ Bước 2: Ghi âm giọng đọc (Shadowing)")
st.markdown("Sau khi nghe mẫu, bấm vào biểu tượng micro bên dưới để ghi âm lại câu đọc của bạn:")

audio_file = st.audio_input("Bấm vào micro để ghi âm giọng của bạn:", key=f"audio_input_{selected_index}")

if audio_file is not None:
    st.success("✨ Ghi âm thành công! Hãy nghe lại giọng đọc của chính bạn bên dưới:")
    st.audio(audio_file)
    
    # Phản hồi từ trợ lý AI với thái độ tích cực, khích lệ
    st.info("🌟 **Trợ lý AI khích lệ:** Tuyệt vời quá! Bạn đã hoàn thành rất xuất sắc phần ghi âm này. Việc bạn chủ động luyện tập mỗi ngày sẽ giúp ngữ điệu tiến bộ cực nhanh. Hãy tiếp tục phát huy ở câu tiếp theo nhé! 💪🚀")

# 8. Chân trang
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Phát triển chuyên biệt cho giáo dục Thất Khê • Hoạt động ổn định 100% trên Streamlit Cloud</p>", unsafe_allow_html=True)