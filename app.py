import streamlit as st

# Cấu hình giao diện trang web
st.set_page_config(page_title="That Khe AI Karaoke Shadowing", page_icon="🎤", layout="centered")

st.markdown("""
    <h2 style='text-align: center; color: #2e7d32;'>🎤 That Khe AI Karaoke Shadowing Coach</h2>
    <p style='text-align: center;'>Hệ thống luyện nhại giọng hiển thị chữ chạy & đồng bộ thời gian thực</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Dữ liệu kịch bản: Câu + Thời gian dừng nhại lại (giây)
script_data = [
    {"id": 1, "text": "Welcome to That Khe! My name is Cuong, and I live here.", "pause": 5},
    {"id": 2, "text": "Every morning, when the sun is still sleeping, Uncle Ba is already awake.", "pause": 6},
    {"id": 3, "text": "He drinks hot tea and eats a big bowl of pho for superpower.", "pause": 5},
    {"id": 4, "text": "He takes bags of star anise and bamboo shoots to the border gate.", "pause": 6},
    {"id": 5, "text": "Uncle Ba cannot speak Chinese, but he uses crazy body language to sell everything.", "pause": 7},
    {"id": 6, "text": "Sometimes the mountain roads are slippery, but he never gives up.", "pause": 6},
    {"id": 7, "text": "At 4:00 PM, he rides back home, tired but happy with his family.", "pause": 6}
]

import json
script_json = json.dumps(script_data)

# Giao diện điều khiển mượt mà bằng HTML/JS chống lỗi trình duyệt
karaoke_html = f"""
<div style="background-color: #1e1e1e; color: white; padding: 25px; border-radius: 12px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
    <div style="font-size: 14px; color: #00bcd4; margin-bottom: 10px; font-weight: bold;" id="step-indicator">Chọn câu bên dưới hoặc bấm Chạy toàn bài</div>
    
    <div style="height: 160px; display: flex; align-items: center; justify-content: center; padding: 15px; border: 2px solid #4CAF50; border-radius: 8px; margin-bottom: 20px; background-color: #2d2d2d;">
        <p id="karaoke-screen" style="font-size: 22px; font-weight: bold; margin: 0; color: #FFD700; line-height: 1.4;">Bấm nút "Nghe & Nhại giọng" ở từng câu bên dưới để bắt đầu luyện tập!</p>
    </div>
    
    <div id="countdown-display" style="font-size: 16px; color: #ff9800; font-weight: bold; min-height: 25px; margin-bottom: 15px;"></div>
    
    <button onclick="playFullSession()" style="background-color: #ff5722; color: white; padding: 12px 25px; border: none; border-radius: 6px; cursor: pointer; font-size: 16px; font-weight: bold;">▶️ Chạy Tự Động Toàn Bài</button>
    <button onclick="stopAll()" style="background-color: #f44336; color: white; padding: 12px 20px; border: none; border-radius: 6px; cursor: pointer; font-size: 16px; font-weight: bold; margin-left: 10px;">⏹️ Dừng lại</button>
</div>

<script>
const data = {script_json};
let globalTimer = null;

function speakSentence(index, callback) {{
    if (index >= data.length) {{
        document.getElementById("karaoke-screen").innerText = "🎉 Hoàn thành xuất sắc bài học!";
        document.getElementById("countdown-display").innerText = "";
        document.getElementById("step-indicator").innerText = "Đã kết thúc";
        return;
    }}

    const item = data[index];
    const screen = document.getElementById("karaoke-screen");
    const countdownEl = document.getElementById("countdown-display");
    const indicator = document.getElementById("step-indicator");

    screen.innerText = item.text;
    indicator.innerText = "Câu " + (index + 1) + " / " + data.length;
    countdownEl.innerText = "🔊 Đang đọc mẫu chuẩn...";

    const utterance = new SpeechSynthesisUtterance(item.text);
    utterance.lang = 'en-US';
    utterance.rate = 0.85; // Tốc độ chuẩn cho cấp độ A2

    utterance.onend = function() {{
        let timeLeft = item.pause;
        countdownEl.innerText = "⏳ Thời gian nhại lại (Shadowing): " + timeLeft + "s (Hãy đọc to)";

        globalTimer = setInterval(() => {{
            timeLeft--;
            if (timeLeft > 0) {{
                countdownEl.innerText = "⏳ Thời gian nhại lại (Shadowing): " + timeLeft + "s (Hãy đọc to)";
            }} else {{
                clearInterval(globalTimer);
                if (callback) callback();
            }}
        }}, 1000);
    }};

    window.speechSynthesis.speak(utterance);
}}

function playFullSession() {{
    window.speechSynthesis.cancel();
    if (globalTimer) clearInterval(globalTimer);
    
    let currentIndex = 0;
    function nextStep() {{
        speakSentence(currentIndex, function() {{
            currentIndex++;
            nextStep();
        }});
    }}
    nextStep();
}}

function stopAll() {{
    window.speechSynthesis.cancel();
    if (globalTimer) clearInterval(globalTimer);
    document.getElementById("karaoke-screen").innerText = "Đã dừng bài học.";
    document.getElementById("countdown-display").innerText = "";
    document.getElementById("step-indicator").innerText = "Tạm dừng";
}}

// Hàm hỗ trợ bấm nghe từng câu riêng lẻ từ bên ngoài
function playSpecific(text, pauseTime) {{
    window.speechSynthesis.cancel();
    if (globalTimer) clearInterval(globalTimer);
    
    const screen = document.getElementById("karaoke-screen");
    const countdownEl = document.getElementById("countdown-display");
    
    screen.innerText = text;
    countdownEl.innerText = "🔊 Đang đọc mẫu...";
    
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = 0.85;
    
    utterance.onend = function() {{
        let timeLeft = pauseTime;
        countdownEl.innerText = "⏳ Thời gian nhại lại: " + timeLeft + "s";
        globalTimer = setInterval(() => {{
            timeLeft--;
            if (timeLeft > 0) {{
                countdownEl.innerText = "⏳ Thời gian nhại lại: " + timeLeft + "s";
            }} else {{
                clearInterval(globalTimer);
                countdownEl.innerText = "✨ Hết giờ! Bạn đọc rất tốt.";
            }}
        }}, 1000);
    }};
    window.speechSynthesis.speak(utterance);
}}
</script>
"""

st.markdown(karaoke_html, unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 📜 Hoặc chọn luyện tập từng câu cụ thể:")

# Tạo danh sách các nút bấm chọn câu trực quan ngay trên Streamlit
for idx, item in enumerate(script_data):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write(f"**{idx+1}.** {item['text']}")
    with col2:
        # Nút gọi trực tiếp hàm JavaScript để đọc câu tương ứng
        button_html = f"""
        <button onclick="playSpecific('{item['text']}', {item['pause']})" style="background-color: #4CAF50; color: white; padding: 6px 12px; border: none; border-radius: 4px; cursor: pointer; font-size: 13px; font-weight: bold;">🔊 Nghe & Nhại</button>
        """
        st.markdown(button_html, unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 🎙️ Ghi âm giọng đọc của bạn để tự kiểm tra")
audio_value = st.audio_input("Bấm vào micro để ghi âm giọng của bạn:")
if audio_value is not None:
    st.success("✨ Đã ghi âm thành công!")
    st.audio(audio_value)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Hệ thống Luyện Ngữ Điệu AI thông minh | 100% Free Cloud</p>", unsafe_allow_html=True)