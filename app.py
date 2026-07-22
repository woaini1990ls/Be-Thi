import streamlit as st

# Cấu hình giao diện trang web
st.set_page_config(
    page_title="That Khe AI Shadowing Studio",
    page_icon="🎓",
    layout="centered"
)

# Tiêu đề ứng dụng
st.title("🎓 That Khe AI Shadowing Studio")
st.subheader("Luyện phát âm tiếng Anh A2 • Chuyện Thợ phiên Thất Khê cùng AI Khích lệ")
st.markdown("---")

# Dữ liệu bài học chuẩn A2 (Câu chuyện Thợ phiên)
script_data = [
    {
        "id": 1, 
        "text": "Welcome to That Khe! My name is Cuong, and I live here.", 
        "vi": "Chào mừng đến với Thất Khê! Tên tôi là Cường, và tôi sống ở đây."
    },
    {
        "id": 2, 
        "text": "Every morning, when the sun is still sleeping, Uncle Ba is already awake.", 
        "vi": "Mỗi sáng, khi mặt trời còn đang ngủ, bác Ba đã thức dậy rồi."
    },
    {
        "id": 3, 
        "text": "He drinks hot tea and eats a big bowl of pho for superpower.", 
        "vi": "Ông ấy uống trà nóng và ăn một tô phở lớn để có siêu năng lực."
    },
    {
        "id": 4, 
        "text": "He takes bags of star anise and bamboo shoots to the border gate.", 
        "vi": "Ông ấy chở những bao hoa hồi và măng ra cửa khẩu."
    },
    {
        "id": 5, 
        "text": "Uncle Ba cannot speak Chinese, but he uses crazy body language to sell everything.", 
        "vi": "Bác Ba không biết tiếng Trung, nhưng bác dùng ngôn ngữ cơ thể cực đỉnh để bán mọi thứ."
    },
    {
        "id": 6, 
        "text": "Sometimes the mountain roads are slippery, but he never gives up.", 
        "vi": "Đôi khi đường núi trơn trượt, nhưng bác ấy không bao giờ từ bỏ."
    },
    {
        "id": 7, 
        "text": "At 4:00 PM, he rides back home, tired but happy with his family.", 
        "vi": "Lúc 4 giờ chiều, bác phóng xe về nhà, mệt nhưng hạnh phúc bên gia đình."
    }
]

# Thanh chọn câu học tập
selected_index = st.selectbox(
    "📌 Chọn câu trong bài học:",
    options=range(len(script_data)),
    format_func=lambda x: f"Câu {x+1}: {script_data[x]['text']}"
)

current_item = script_data[selected_index]

# Hiển thị khung nội dung chính
with st.container():
    st.markdown(f"### 🇬🇧 {current_item['text']}")
    st.markdown(f"#### 🇻🇳 {current_item['vi']}")

st.markdown("---")

# -------------------------------------------------------------------------
# BỘ CÔNG CỤ AI: NGHE MẪU & LẮNG NGHE - ĐÁNH GIÁ TÍCH CỰC
# -------------------------------------------------------------------------
ai_evaluator_code = f"""
<div style="background-color: #f9fbe7; padding: 20px; border-radius: 12px; border: 2px solid #8bc34a; font-family: sans-serif;">
    <h3 style="color: #33691e; margin-top: 0;">🤖 Trợ lý AI Khích lệ phát âm</h3>
    <p style="color: #555; font-size: 14px;">Bấm nút nghe mẫu để chuẩn bị tinh thần, sau đó bấm <b>"🎤 Đọc và Nhờ AI Chấm Điểm"</b> để nói vào micro.</p>
    
    <div style="margin: 15px 0; display: flex; gap: 10px; flex-wrap: wrap;">
        <button onclick="playAudio()" style="background-color: #2e7d32; color: white; padding: 10px 18px; border: none; border-radius: 6px; cursor: pointer; font-size: 15px; font-weight: bold;">
            🔊 Nghe Mẫu
        </button>
        <button onclick="startAIEvaluation()" style="background-color: #ff6f00; color: white; padding: 10px 18px; border: none; border-radius: 6px; cursor: pointer; font-size: 15px; font-weight: bold;" id="record-btn">
            🎤 Đọc và Nhờ AI Chấm Điểm
        </button>
    </div>

    <div id="ai-feedback-box" style="margin-top: 15px; padding: 15px; background: white; border-radius: 8px; border-left: 5px solid #ffb300; display: none;">
        <p id="ai-status" style="font-weight: bold; color: #e65100; margin: 0 0 5px 0;">Đang lắng nghe bạn nói...</p>
        <p id="ai-user-said" style="font-style: italic; color: #555; margin: 0 0 8px 0;"></p>
        <p id="ai-encouragement" style="font-size: 16px; font-weight: bold; color: #2e7d32; margin: 0;"></p>
    </div>
</div>

<script>
const targetText = "{current_item['text']}";

function playAudio() {{
    if (!('speechSynthesis' in window)) {{
        alert("Trình duyệt không hỗ trợ phát âm!");
        return;
    }}
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(targetText);
    utterance.lang = 'en-US';
    utterance.rate = 0.85;
    window.speechSynthesis.speak(utterance);
}}

function startAIEvaluation() {{
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {{
        alert("Trình duyệt của bạn không hỗ trợ tính năng nhận diện giọng nói AI. Hãy sử dụng trình duyệt Google Chrome nhé!");
        return;
    }}

    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    const box = document.getElementById("ai-feedback-box");
    const statusEl = document.getElementById("ai-status");
    const saidEl = document.getElementById("ai-user-said");
    const encourageEl = document.getElementById("ai-encouragement");
    const btn = document.getElementById("record-btn");

    box.style.display = "block";
    statusEl.innerText = "🎙️ AI đang lắng nghe... Hãy đọc to rõ câu văn!";
    saidEl.innerText = "";
    encourageEl.innerText = "";
    btn.disabled = true;
    btn.style.backgroundColor = "#9e9e9e";

    recognition.onresult = function(event) {{
        const userSpeech = event.results[0][0].transcript;
        saidEl.innerText = "🗣️ Bạn vừa đọc: \"" + userSpeech + "\"";
        
        // Thuật toán đánh giá thông minh kết hợp thái độ cực kỳ tích cực, khích lệ
        let score = calculateSimilarity(userSpeech.toLowerCase(), targetText.toLowerCase());
        
        if (score > 0.75) {{
            encourageEl.innerHTML = "🌟 Tuyệt vời quá! Phát âm của bạn rất chuẩn xác và tự nhiên. Hãy giữ vững phong độ này nhé! 🎉";
            box.style.borderLeftColor = "#4caf50";
        }} else if (score > 0.4) {{
            encourageEl.innerHTML = "👍 Cố gắng lắm! Bạn đã đọc đúng phần lớn cấu trúc câu rồi. Chỉ cần chú ý luyện lại ngữ điệu cho mượt mà hơn chút nữa là hoàn hảo! 💪";
            box.style.borderLeftColor = "#ff9800";
        }} else {{
            encourageEl.innerHTML = "💡 Đừng nản lòng nhé! Việc luyện tập cần sự kiên trì. Hãy bấm 'Nghe Mẫu' lại một lượt rồi thử đọc to rõ hơn, AI tin bạn sẽ làm được! 🚀";
            box.style.borderLeftColor = "#f44336";
        }}
        
        statusEl.innerText = "✨ AI đã phân tích xong!";
        btn.disabled = false;
        btn.style.backgroundColor = "#ff6f00";
    }};

    recognition.onerror = function(event) {{
        statusEl.innerText = "⚠️ Ôi, AI chưa nghe rõ bạn đọc. Hãy thử bấm nút và đọc lại gần micro hơn nhé!";
        saidEl.innerText = "";
        encourageEl.innerHTML = "😊 Không sao cả, khởi đầu luôn có chút thử thách. Cố lên nào!";
        btn.disabled = false;
        btn.style.backgroundColor = "#ff6f00";
    }};

    recognition.onend = function() {{
        btn.disabled = false;
        btn.style.backgroundColor = "#ff6f00";
    }};

    recognition.start();
}}

// Hàm phụ trợ so khớp từ vựng đơn giản để đánh giá độ chính xác
function calculateSimilarity(str1, str2) {{
    const words1 = str1.split(" ");
    const words2 = str2.split(" ");
    let matchCount = 0;
    for (let w of words1) {{
        if (words2.includes(w)) matchCount++;
    }}
    return matchCount / Math.max(words1.length, words2.length);
}}
</script>
"""

st.components.v1.html(ai_evaluator_code, height=320)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Hệ thống Luyện Giọng AI Tích Hợp Khích Lệ • Chạy ổn định 100% trên Streamlit Cloud</p>", unsafe_allow_html=True)