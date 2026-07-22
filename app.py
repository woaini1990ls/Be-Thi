import streamlit as st

# Cấu hình giao diện trang web
st.set_page_config(page_title="That Khe AI Shadowing & Video Coach", page_icon="🎬", layout="centered")

st.title("🎬 That Khe AI Shadowing & Video Coach")
st.subheader("Ngách địa phương: Luyện nhại giọng kèm Video bối cảnh AI")
st.markdown("---")

# Danh sách câu chuyện kèm theo mô tả cảnh quay (Visual Prompt) tương ứng cho AI Video
story_data = [
    {
        "sentence": "Welcome to That Khe! My name is Cuong, and I live here.",
        "prompt": "Cinematic wide shot of a peaceful mountain town in That Khe Lang Son, Vietnam, early morning mist, local boy smiling, vibrant colors, 4k"
    },
    {
        "sentence": "Every morning, when the sun is still sleeping, Uncle Ba is already awake.",
        "prompt": "A middle-aged Vietnamese man waking up early before sunrise in a rustic wooden house, holding a hot tea cup, cinematic lighting"
    },
    {
        "sentence": "He drinks hot tea and eats a big bowl of pho for superpower.",
        "prompt": "Close up of a steaming bowl of delicious traditional Vietnamese pho on a wooden table, morning light"
    },
    {
        "sentence": "He takes bags of star anise and bamboo shoots to the border gate.",
        "prompt": "A Vietnamese local merchant carrying bags of star anise spices and fresh bamboo shoots on a motorbike near a mountain border gate"
    },
    {
        "sentence": "Uncle Ba cannot speak Chinese, but he uses crazy body language to sell everything.",
        "prompt": "A friendly Asian trader talking with lively hand gestures and smiling broadly at a bustling outdoor market stall"
    },
    {
        "sentence": "Sometimes the mountain roads are slippery, but he never gives up.",
        "prompt": "A motorbike riding carefully on a wet, misty mountain pass road in Vietnam after rain, dramatic adventure mood"
    },
    {
        "sentence": "At 4:00 PM, he rides back home, tired but happy with his family.",
        "prompt": "A Vietnamese family sitting together around a warm dinner table sharing a cozy meal in the evening, heartwarming cinematic shot"
    }
]

# Giao diện chọn câu
sentence_list = [item["sentence"] for item in story_data]
selected_sentence = st.selectbox("📜 Chọn câu trong câu chuyện của Cường:", sentence_list)

# Tìm dữ liệu tương ứng với câu được chọn
current_item = next(item for item in story_data if item["sentence"] == selected_sentence)

st.info(f"**Câu hiện tại:** {selected_sentence}")

# Hiển thị bối cảnh Video AI tương ứng
st.markdown(f"**🎨 Bối cảnh Video minh họa (AI Prompt):** `{current_item['prompt']}`")

# Tích hợp công cụ sinh video từ hệ thống AI chuyên dụng
if st.button("🚀 Tạo Video minh họa bối cảnh câu này bằng AI"):
    with st.spinner("AI đang xử lý và tạo video phù hợp với bối cảnh Thất Khê... Vui lòng đợi trong giây lát!"):
        try:
            # Gọi công cụ tạo video từ hệ thống
            video_result = video_generation.generate_video_from_inputs(
                prompt=current_item['prompt'],
                image_references=None,
                audio_references=None,
                video_references=None
            )
            
            # Kiểm tra kết quả trả về từ API tạo video
            if video_result and hasattr(video_result, 'videos') and video_result.videos:
                st.success("Your video is ready!")
                # Hiển thị video trực tiếp trên giao diện web thông qua ID trả về
                # Lưu ý: Hệ thống tự động render video tại vị trí gọi ID chuẩn
                for v in video_result.videos:
                    if hasattr(v, 'video_id') and v.video_id:
                        st.markdown(f"Video ID: {v.video_id}")
            else:
                st.error("Can't generate your video. Try another prompt.")
        except Exception as e:
            st.error(f"Đã xảy ra lỗi kết nối hệ thống video: {e}")

st.markdown("---")

# Tích hợp Web Speech API (Text-to-Speech) để nghe câu mẫu
tts_html = f"""
<div style="margin: 20px 0;">
    <button onclick="speakText()" style="background-color: #2e7d32; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">🔊 Nghe câu mẫu (Listen)</button>
</div>

<script>
function speakText() {{
    const text = "{selected_sentence}";
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = 0.9;
    window.speechSynthesis.speak(utterance);
}}
</script>
"""
st.markdown(tts_html, unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 🎙️ Ghi âm giọng đọc của bạn để luyện Shadowing")
audio_value = st.audio_input("Bấm vào micro để ghi âm:")
if audio_value is not None:
    st.success("✨ Đã ghi âm thành công!")
    st.audio(audio_value)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Hệ thống Web Luyện Ngữ Điệu AI thông minh | 100% Free Cloud</p>", unsafe_allow_html=True)