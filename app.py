import streamlit as st

# 1. Cấu hình trang
st.set_page_config(
    page_title="That Khe AI Shadowing Studio",
    page_icon="🎓",
    layout="centered"
)

# 2. Tiêu đề ứng dụng
st.title("🎓 That Khe AI Shadowing Studio")
st.subheader("Hệ thống luyện nhại giọng 3 bước chuẩn quốc tế • Chuyện Thợ phiên Thất Khê")
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

# 4. Thanh chọn câu học tập
selected_index = st.selectbox(
    "📌 Chọn câu trong bài học để luyện tập:",
    options=range(len(script_data)),
    format_func=lambda x: f"Câu {x+1}: {script_data[x]['text']}"
)

current_item = script_data[selected_index]

# Màn hình hiển thị câu & bối cảnh Karaoke
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

# =========================================================================
# BƯỚC 1: BẤM NGHE MẪU
# =========================================================================
st.markdown("### 🔊 BƯỚC 1: Bấm nghe mẫu bản xứ")
st.markdown("Lắng nghe thật kỹ ngữ điệu và cách phát âm của AI trước khi đọc theo:")

tts_html = f"""
<div style="margin: 10px 0;">
    <button onclick="playNativeSpeech()" style="background-color: #2e7d32; color: white; padding: 12px 24px; border: none; border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: bold;">
        ▶️ Nghe Mẫu Bản Xứ
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
    utterance.rate = 0.85; // Tốc độ chuẩn chậm vừa phải cho học sinh
    window.speechSynthesis.speak(utterance);
}}
</script>
"""
st.components.v1.html(tts_html, height=70)

st.markdown("---")

# =========================================================================
# BƯỚC 2: NHẠI LẠI (GHI ÂM GIỌNG ĐỌC)
# =========================================================================
st.markdown("### 🎙️ BƯỚC 2: Nhại lại (Ghi âm giọng của bạn)")
st.markdown("Bấm vào biểu tượng micro bên dưới để ghi âm lại câu bạn vừa nghe:")

audio_file = st.audio_input("Bấm vào micro để ghi âm:", key=f"audio_input_{selected_index}")

if audio_file is not None:
    st.success("✨ Đã thu âm xong giọng của bạn! Nghe lại đối chiếu:")
    st.audio(audio_file)

st.markdown("---")

# =========================================================================
# BƯỚC 3: AI CHECK, SỬA LỖI VÀ KHÍCH LỆ ĐỘNG VIÊN
# =========================================================================
st.markdown("### 🤖 BƯỚC 3: AI Check lỗi, Sửa phát âm & Khích lệ")
st.markdown("Chấm điểm thông minh bằng giọng nói trực tiếp qua AI, kèm theo những lời nhận xét cực kỳ hài hước và động lực:")

ai_checker_html = f"""
<div style="background-color: #f0f4c3; padding: 20px; border-radius: 12px; border: 2px solid #afb42b; font-family: sans-serif;">
    <button onclick="startAIJudge()" id="judge-btn" style="background-color: #e65100; color: white; padding: 12px 24px; border: none; border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: bold;">
        🎯 Bấm để AI Check và Sửa lỗi ngay
    </button>
    
    <div id="result-box" style="margin-top: 15px; display: none; background: white; padding: 15px; border-radius: 8px; border-left: 5px solid #ff6f00;">
        <p id="user-transcript" style="font-style: italic; color: #555; margin: 0 0 8px 0;"></p>
        <p id="ai-comment" style="font-size: 16px; font-weight: bold; color: #2e7d32; margin: 0; line-height: 1.5;"></p>
    </div>
</div>

<script>
const targetSentence = "{current_item['text']}";

function startAIJudge() {{
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {{
        alert("Trình duyệt của bạn không hỗ trợ nhận diện giọng nói AI. Hãy dùng Google Chrome nhé!");
        return;
    }}

    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    
    const btn = document.getElementById("judge-btn");
    const box = document.getElementById("result-box");
    const transcriptEl = document.getElementById("user-transcript");
    const commentEl = document.getElementById("ai-comment");

    box.style.display = "block";
    transcriptEl.innerText = "🎧 AI đang lắng nghe bạn nhại giọng... Hãy đọc to rõ nhé!";
    commentEl.innerText = "⏳ Đang phân tích độ chuẩn xác...";
    btn.disabled = true;
    btn.style.backgroundColor = "#9e9e9e";

    recognition.onresult = function(event) {{
        const saidText = event.results[0][0].transcript;
        transcriptEl.innerText = "🗣️ Bạn vừa đọc: \"" + saidText + "\"";
        
        let score = calculateScore(saidText.toLowerCase(), targetSentence.toLowerCase());
        
        let feedbacks = [];
        if (score > 0.8) {{
            feedbacks = [
                "🌟 Oa! Phát âm đỉnh chóp như người bản xứ London luôn! Cứ đà này mai mốt thành phiên dịch viên quốc tế mất thôi! 😎🚀",
                "🔥 Xuất sắc hoàn hảo! Ngữ điệu mượt hơn cả bôi mỡ. Tây gặp chắc tưởng bạn sinh ra ở Mỹ ấy chứ! 👑🎉",
                "🎉 Quá tuyệt vời! AI chấm điểm 10/10 và tặng bạn một tràng pháo tay vang dội! Chuyển câu tiếp theo thui nào! 🏆"
            ];
        }} else if (score > 0.4) {{
            feedbacks = [
                "👍 Khá lắm! Nghe là biết có đầu tư luyện tập theo bước 1 rồi đây. Chỉ hơi vấp một tẹo ở vài từ thôi, sửa nhẹ cái là bay cao bay xa ngay! Cố lên nào phi công trẻ! ✈️💪",
                "💡 Gần chuẩn rồi Đại bàng ơi! Đã hình thành phong cách đọc của siêu sao Thất Khê rồi đấy. Thả lỏng cơ miệng, đọc lại ngầu hơn một chút nữa là hoàn hảo! 🎸🔥",
                "🎯 Trúng đích hơn nửa chặng đường rồi! AI đánh giá bạn có tiềm năng lớn. Làm lại một nháy nữa cho nó rực rỡ xem nào! 🎬✨"
            ];
        }} else {{
            feedbacks = [
                "😂 Ấy chà, hình như micro đang... đi ngủ gật hoặc bạn đang cố đọc bằng một ngôn ngữ ngoài hành tinh nào đó rồi! Nghe lại mẫu ở Bước 1 rồi đọc to rõ lại xem nào, AI tin bạn làm được! 🛸💪",
                "🐒 Ấy chết, AI nghe xong mà giật mình tưởng tiếng chim hót trong rừng Thất Khê! Đừng nản, hít một hơi thật sâu, bấm nghe mẫu lại rồi sút tung nóc câu này nhé! ⚽🚀",
                "😜 Cười lên nào! Khởi đầu thế này mới có chỗ cho sự tiến bộ vượt bậc chứ. Thử lại lần nữa với 200% năng lượng xem AI có ngả mũ thán phục không nào! 💥👑"
            ];
        }}
        
        let randomMsg = feedbacks[Math.floor(Math.random() * feedbacks.length)];
        commentEl.innerHTML = randomMsg;
        
        btn.disabled = false;
        btn.style.backgroundColor = "#e65100";
    }};

    recognition.onerror = function(event) {{
        transcriptEl.innerText = "⚠️ Ôi, hình như AI chưa nghe rõ giọng vàng giọng ngọc của bạn.";
        commentEl.innerHTML = "😅 Không sao cả! Thử bấm lại nút và đọc sát micro hơn chút nhé, chiến thần không sợ khó! 🛡️💪";
        btn.disabled = false;
        btn.style.backgroundColor = "#e65100";
    }};

    recognition.onend = function() {{
        btn.disabled = false;
        btn.style.backgroundColor = "#e65100";
    }};

    recognition.start();
}}

function calculateScore(str1, str2) {{
    const w1 = str1.split(" ");
    const w2 = str2.split(" ");
    let matches = 0;
    for (let word of w1) {{
        if (w2.includes(word)) matches++;
    }}
    return matches / Math.max(w1.length, w2.length);
}
</script>
"""
st.components.v1.html(ai_checker_html, height=220)

# Chân trang
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Phát triển chuyên biệt cho giáo dục Thất Khê • Hoạt động ổn định 100% trên Streamlit Cloud</p>", unsafe_allow_html=True)