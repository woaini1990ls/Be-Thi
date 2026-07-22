import streamlit as st

# Cấu hình giao diện trang web
st.set_page_config(page_title="That Khe AI Karaoke Shadowing", page_icon="🎤", layout="centered")

st.markdown("""
    <h2 style='text-align: center; color: #2e7d32;'>🎤 That Khe AI Karaoke Shadowing Coach</h2>
    <p style='text-align: center;'>Hệ thống luyện nhại giọng hiển thị chữ chạy & tự động dừng theo nhịp điệu bản xứ</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Dữ liệu kịch bản: Câu + Thời gian dừng sau câu đó (tính bằng giây để học sinh nhại lại)
script_data = [
    {"text": "Welcome to That Khe! My name is Cuong, and I live here.", "pause": 5},
    {"text": "Every morning, when the sun is still sleeping, Uncle Ba is already awake.", "pause": 6},
    {"text": "He drinks hot tea and eats a big bowl of pho for superpower.", "pause": 5},
    {"text": "He takes bags of star anise and bamboo shoots to the border gate.", "pause": 6},
    {"text": "Uncle Ba cannot speak Chinese, but he uses crazy body language to sell everything.", "pause": 7},
    {"text": "Sometimes the mountain roads are slippery, but he never gives up.", "pause": 6},
    {"text": "At 4:00 PM, he rides back home, tired but happy with his family.", "pause": 6}
]

# Chuyển dữ liệu sang định dạng JSON để truyền sang JavaScript an toàn
import json
script_json = json.dumps(script_data)

# Khởi tạo giao diện Video/Karaoke giả lập thông minh bằng HTML5 + Canvas + Web Speech API
karaoke_html = f"""
<div style="background-color: #1e1e1e; color: white; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
    <div id="video-screen" style="height: 180px; display: flex; align-items: center; justify-content: center; padding: 15px; border: 2px dashed #4CAF50; border-radius: 8px; margin-bottom: 15px; background-color: #2d2d2d;">
        <p id="karaoke-text" style="font-size: 22px; font-weight: bold; margin: 0; color: #FFD700; text-align: center;">Bấm "Bắt đầu bài học" để chạy video tự động...</p>
    </div>
    
    <div id="status-timer" style="font-size: 14px; color: #00bcd4; margin-bottom: 10px; font-weight: bold;">Trạng thái: Sẵn sàng</div>
    
    <button onclick="startKaraokeSession()" style="background-color: #4CAF50; color: white; padding: 12px 25px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; font-weight: bold;">▶️ Bắt đầu Chạy Video & Dừng Nhại Giọng</button>
    <button onclick="stopSession()" style="background-color: #f44336; color: white; padding: 12px 25px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; font-weight: bold; margin-left: 10px;">⏹️ Dừng lại</button>
</div>

<script>
const scriptData = {script_json};
let currentIdx = 0;
let isRunning = false;
let timeoutId = null;

function speakAndPause(index) {{
    if (!isRunning || index >= scriptData.length) {{
        document.getElementById("karaoke-text").innerText = "🎉 Hoàn thành bài học! Tuyệt vời!";
        document.getElementById("status-timer").innerText = "Trạng thái: Đã xong";
        isRunning = false;
        return;
    }}

    const item = scriptData[index];
    const screen = document.getElementById("karaoke-text");
    const timerStatus = document.getElementById("status-timer");

    // Hiển thị câu hiện tại lên màn hình video giả lập
    screen.innerText = item.text;
    timerStatus.innerText = "🔊 Đang đọc mẫu...";

    // Sử dụng tính năng phát âm thanh tích hợp sẵn của trình duyệt (Text-to-Speech)
    const utterance = new SpeechSynthesisUtterance(item.text);
    utterance.lang = 'en-US';
    utterance.rate = 0.85; // Tốc độ chuẩn chậm vừa phải cho học sinh A2

    utterance.onend = function() {{
        if (!isRunning) return;
        
        // Bắt đầu đếm ngược thời gian dừng để học sinh nhại lại (Shadowing)
        let timeLeft = item.pause;
        timerStatus.innerText = "⏳ Thời gian nhại lại (Shadowing): " + timeLeft + "s ... (Hãy đọc to)";

        const countdown = setInterval(() => {{
            timeLeft--;
            if (timeLeft > 0) {{
                timerStatus.innerText = "⏳ Thời gian nhại lại (Shadowing): " + timeLeft + "s ... (Hãy đọc to)";
            }} else {{
                clearInterval(countdown);
                if (isRunning) {{
                    currentIdx++;
                    speakAndPause(currentIdx); // Chuyển sang câu tiếp theo
                }}
            }}
        }}, 1000);
        
        timeoutId = countdown;
    }};

    window.speechSynthesis.speak(utterance);
}}

function startKaraokeSession() {{
    if (isRunning) return;
    window.speechSynthesis.cancel(); // Xóa các hàng đợi cũ nếu có
    isRunning = true;
    currentIdx = 0;
    speakAndPause(currentIdx);
}}

function stopSession() {{
    isRunning = false;
    window.speechSynthesis.cancel();
    if (timeoutId) clearInterval(timeoutId);
    document.getElementById("karaoke-text").innerText = "Đã dừng bài học.";
    document.getElementById("status-timer").innerText = "Trạng thái: Tạm dừng";
}}
</script>
"""

st.markdown(karaoke_html, unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 🎙️ Ghi âm cá nhân để kiểm tra phát âm thực tế")
st.markdown("Bạn có thể ghi âm trực tiếp giọng đọc của mình sau khi nghe xong từng câu:")

audio_value = st.audio_input("Bấm vào micro để ghi âm:")
if audio_value is not None:
    st.success("✨ Đã ghi âm thành công! Bạn có thể phát lại để kiểm tra:")
    st.audio(audio_value)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Hệ thống Luyện Giọng Khung Hình Thông Minh | 100% Free Cloud</p>", unsafe_allow_html=True)