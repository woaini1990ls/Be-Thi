import streamlit as st
import json

# Cấu hình giao diện
st.set_page_config(
    page_title="That Khe AI Shadowing Studio",
    page_icon="🎬",
    layout="centered"
)

# Giao diện Tiêu đề phong cách EdTech hiện đại
st.markdown("""
    <div style='text-align: center; padding: 15px;'>
        <h1 style='color: #1b5e20; margin-bottom: 5px;'>🎬 That Khe AI Shadowing & Video Studio</h1>
        <p style='color: #555; font-size: 16px;'>Luyện nhại giọng thông minh • Bối cảnh sinh động • Chữ chạy Karaoke trực quan</p>
    </div>
    <hr style='border: 1px solid #c8e6c9;'>
""", unsafe_allow_html=True)

# Dữ liệu bài học chuẩn A2 (Câu chuyện Thợ phiên Thất Khê) kèm theo hình ảnh/video bối cảnh minh họa trực quan
script_data = [
    {
        "id": 1, 
        "text": "Welcome to That Khe! My name is Cuong, and I live here.", 
        "vi": "Chào mừng đến với Thất Khê! Tên tôi là Cường, và tôi sống ở đây.",
        "bg_image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
        "scene": "Cảnh toàn thị trấn Thất Khê buổi sớm bình minh, mây giăng núi đồi."
    },
    {
        "id": 2, 
        "text": "Every morning, when the sun is still sleeping, Uncle Ba is already awake.", 
        "vi": "Mỗi sáng, khi mặt trời còn đang ngủ, bác Ba đã thức dậy rồi.",
        "bg_image": "https://images.unsplash.com/photo-1470240731273-7821a6eeb6bd?auto=format&fit=crop&w=800&q=80",
        "scene": "Cảnh sáng sớm trời còn tối mờ, bác Ba lục đục thức dậy."
    },
    {
        "id": 3, 
        "text": "He drinks hot tea and eats a big bowl of pho for superpower.", 
        "vi": "Ông ấy uống trà nóng và ăn một tô phở lớn để có siêu năng lực.",
        "bg_image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=80",
        "scene": "Cảnh tô phở nóng hổi nghi ngút khói buổi sáng ở Lạng Sơn."
    },
    {
        "id": 4, 
        "text": "He takes bags of star anise and bamboo shoots to the border gate.", 
        "vi": "Ông ấy chở những bao hoa hồi và măng ra cửa khẩu.",
        "bg_image": "https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=800&q=80",
        "scene": "Cảnh chở hàng hóa đặc sản hoa hồi, măng tre ra khu vực cửa khẩu."
    },
    {
        "id": 5, 
        "text": "Uncle Ba cannot speak Chinese, but he uses crazy body language to sell everything.", 
        "vi": "Bác Ba không biết tiếng Trung, nhưng bác dùng ngôn ngữ cơ thể cực đỉnh để bán mọi thứ.",
        "bg_image": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=800&q=80",
        "scene": "Cảnh trao đổi mua bán sôi nổi bằng ngôn ngữ cơ thể vui nhộn."
    },
    {
        "id": 6, 
        "text": "Sometimes the mountain roads are slippery, but he never gives up.", 
        "vi": "Đôi khi đường núi trơn trượt, nhưng bác ấy không bao giờ từ bỏ.",
        "bg_image": "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=800&q=80",
        "scene": "Cảnh đường đèo núi mờ sương, xe máy di chuyển thận trọng."
    },
    {
        "id": 7, 
        "text": "At 4:00 PM, he rides back home, tired but happy with his family.", 
        "vi": "Lúc 4 giờ chiều, bác phóng xe về nhà, mệt nhưng hạnh phúc bên gia đình.",
        "bg_image": "https://images.unsplash.com/photo-1511895426328-dc8714191300?auto=format&fit=crop&w=800&q=80",
        "scene": "Cảnh bữa cơm gia đình đầm ấm quây quần lúc chiều tà."
    }
]

script_json = json.dumps(script_data)

# Giao diện Player Karaoke trực quan kết hợp Hình ảnh bối cảnh và Chữ chạy động
player_html = f"""
<div style="background-color: #121212; color: white; padding: 20px; border-radius: 15px; box-shadow: 0 6px 15px rgba(0,0,0,0.4); text-align: center; font-family: sans-serif;">
    
    <!-- Màn hình hiển thị bối cảnh trực quan -->
    <div id="scene-container" style="position: relative; height: 240px; border-radius: 10px; overflow: hidden; border: 2px solid #4CAF50; background-image: url('{script_data[0]['bg_image']}'); background-size: cover; background-position: center; display: flex; flex-direction: column; justify-content: flex-end; padding: 15px;">
        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0, 0, 0, 0.5);"></div>
        
        <div style="position: relative; z-index: 2;">
            <p id="scene-desc" style="font-size: 13px; color: #a5d6a7; margin: 0 0 5px 0; font-style: italic;">🎬 Bối cảnh: {script_data[0]['scene']}</p>
            <!-- Khung chữ chạy Karaoke -->
            <p id="karaoke-text" style="font-size: 20px; font-weight: bold; color: #FFD700; margin: 0 0 10px 0; line-height: 1.4;">{script_data[0]['text']}</p>
            <p id="vietnamese-text" style="font-size: 14px; color: #fff; margin: 0;">🇻🇳 {script_data[0]['vi']}</p>
        </div>
    </div>

    <!-- Thanh trạng thái và bộ đếm thời gian Shadowing -->
    <div id="status-bar" style="margin: 15px 0; font-size: 15px; font-weight: bold; color: #00bcd4; min-height: 24px;">
        Trạng thái: Sẵn sàng luyện tập
    </div>

    <!-- Bảng điều khiển nút bấm -->
    <div style="display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
        <button onclick="playCurrentSentence()" style="background-color: #2e7d32; color: white; padding: 10px 20px; border: none; border-radius: 6px; cursor: pointer; font-size: 15px; font-weight: bold;">🔊 Nghe Mẫu Phát Âm</button>
        <button onclick="playFullLesson()" style="background-color: #ff5722; color: white; padding: 10px 20px; border: none; border-radius: 6px; cursor: pointer; font-size: 15px; font-weight: bold;">▶️ Chạy Tự Động Toàn Bài</button>
        <button onclick="stopSession()" style="background-color: #d32f2f; color: white; padding: 10px 15px; border: none; border-radius: 6px; cursor: pointer; font-size: 15px; font-weight: bold;">⏹️ Dừng</button>
    </div>

    <!-- Thanh chuyển đổi câu thủ công -->
    <div style="margin-top: 15px; display: flex; justify-content: space-between; align-items: center; background: #1e1e1e; padding: 10px; border-radius: 8px;">
        <button onclick="prevSentence()" style="background: #333; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer;">◀ Câu trước</button>
        <span id="page-indicator" style="font-size: 14px; font-weight: bold;">Câu 1 / {len(script_data)}</span>
        <button onclick="nextSentence()" style="background: #333; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer;">Câu sau ▶</button>
    </div>
</div>

<script>
const data = {script_json};
let currentIndex = 0;
let isRunning = false;
let globalTimer = null;

function updateView(index) {{
    const item = data[index];
    document.getElementById("karaoke-text").innerText = item.text;
    document.getElementById("vietnamese-text").innerText = "🇻🇳 " + item.vi;
    document.getElementById("scene-desc").innerText = "🎬 Bối cảnh: " + item.scene;
    document.getElementById("scene-container").style.backgroundImage = "url('" + item.bg_image + "')";
    document.getElementById("page-indicator").innerText = "Câu " + (index + 1) + " / " + data.length;
}}

function playCurrentSentence(onEndCallback) {{
    window.speechSynthesis.cancel();
    if (globalTimer) clearInterval(globalTimer);
    
    const item = data[currentIndex];
    updateView(currentIndex);
    
    const statusBar = document.getElementById("status-bar");
    statusBar.style.color = "#FFD700";
    statusBar.innerText = "🔊 Đang đọc mẫu chuẩn bản xứ...";

    const utterance = new SpeechSynthesisUtterance(item.text);
    utterance.lang = 'en-US';
    utterance.rate = 0.85; // Tốc độ chuẩn chậm cho cấp độ A2

    utterance.onend = function() {{
        let timeLeft = 6; // Thời gian dừng để học sinh nhại lại
        statusBar.style.color = "#00bcd4";
        
        globalTimer = setInterval(() => {{
            if (timeLeft > 0) {{
                statusBar.innerText = "⏳ Thời gian nhại lại (Shadowing): " + timeLeft + "s (Hãy đọc to)";
                timeLeft--;
            }} else {{
                clearInterval(globalTimer);
                if (onEndCallback) onEndCallback();
            }}
        }}, 1000);
    }};

    window.speechSynthesis.speak(utterance);
}}

function playFullLesson() {{
    window.speechSynthesis.cancel();
    if (globalTimer) clearInterval(globalTimer);
    isRunning = true;
    currentIndex = 0;

    function step() {{
        if (!isRunning) return;
        playCurrentSentence(function() {{
            currentIndex++;
            if (currentIndex < data.length) {{
                step();
            }} else {{
                document.getElementById("status-bar.innerText") = "🎉 Hoàn thành toàn bộ bài học!";
                isRunning = false;
            }}
        }});
    }}
    step();
}}

function stopSession() {{
    isRunning = false;
    window.speechSynthesis.cancel();
    if (globalTimer) clearInterval(globalTimer);
    document.getElementById("status-bar").innerText = "Trạng thái: Đã dừng lại";
}}

function nextSentence() {{
    window.speechSynthesis.cancel();
    if (globalTimer) clearInterval(globalTimer);
    if (currentIndex < data.length - 1) {{
        currentIndex++;
        updateView(currentIndex);
    }}
}}

function prevSentence() {{
    window.speechSynthesis.cancel();
    if (globalTimer) clearInterval(globalTimer);
    if (currentIndex > 0) {{
        currentIndex--;
        updateView(currentIndex);
    }}
}}
</script>
"""

st.markdown(player_html, unsafe_allow_html=True)

st.markdown("---")

# -------------------------------------------------------------------------
# BỘ GHI ÂM NHẠI GIỌNG (SHADOWING RECORDING)
# -------------------------------------------------------------------------
st.markdown("### 🎙️ Ghi âm giọng đọc của bạn")
st.markdown("<p style='font-size: 14px; color: #555;'>Sau khi nghe mẫu và luyện nhại, hãy bấm vào micro bên dưới để ghi âm lại giọng đọc thực tế của bạn:</p>", unsafe_allow_html=True)

audio_value = st.audio_input("Bấm vào biểu tượng micro để ghi âm:")

if audio_value is not None:
    st.success("✨ Ghi âm thành công! Phát lại để kiểm tra:")
    st.audio(audio_value)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #888; font-size: 13px;'>Hệ thống Luyện Ngữ Điệu Khung Hình Động • Chạy trực tiếp 100% Free</p>", unsafe_allow_html=True)