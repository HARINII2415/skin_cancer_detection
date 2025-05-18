<h1 align="center">🧠 Skin Disease AI Detector</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Built%20With-Streamlit-%23FF4B4B?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Powered%20By-Gemini%20AI-pink?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge" />
</p>

---

## 🌐 Live Demo

🔗 [**melanoma-lesion-dedector.onrender.com**](https://melanoma-lesion-dedector.onrender.com/)

---

## 💡 What It Does

- 📸 Upload or click a picture of your skin
- 🔍 Gemini AI detects **diseases or confirms healthy skin**
- 🤖 Chatbot asks **interactive questions** to verify the diagnosis
- 👩‍⚕️ Suggests doctor consultation if symptoms don’t match

---

## 🛠️ Tech Stack

| Technology | Role |
|------------|------|
| **Streamlit** | Web UI |
| **Gemini API** | Image & Chat Intelligence |
| **Python** | Main backend language |
| **Pillow (PIL)** | Image processing |
| **dotenv** | Manage secrets safely |

---

## 📁 Project Structure

├── main.py            # Streamlit App
├── chat.py            # Gemini chat logic
├── requirements.txt   # Dependencies
├── .env               # API key (keep secret!)
└── README.md          # You're here

🚀 Getting Started Locally
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/HARINII2415/skin-disease-ai.git
cd skin-disease-ai
2. Create and activate virtual environment (optional)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Create .env file
bash
Copy
Edit
echo "GEMINI_API_KEY=your_api_key_here" > .env
5. Run the app
bash
Copy
Edit
streamlit run main.py
🎯 Use Case
This tool is ideal for:

Early skin condition awareness

AI-assisted dermatology prototypes

HealthTech hackathons or student AI projects

🙋‍♀️ Developed by
Harini A 
🎓 3rd-year B.Tech IT Student
💻 Passionate about AI, Full Stack Development, and HealthTech

<p align="left"> <a href="https://www.linkedin.com/in/harini-a-9a014925a" target="_blank">🌐 LinkedIn</a> • <a href="https://harinii2415.github.io" target="_blank">💼 Portfolio</a> </p>
🛑 Disclaimer
⚠️ This is a demo tool and does not provide medical advice.
For accurate diagnosis and treatment, consult a medical professional.

⭐ Show Some Love
If this helped or inspired you:

⭐ Star this repo
🖊️ Fork & contribute
🔁 Share with friends

🔮 Upcoming Ideas
✅ Email report feature

✅ Multi-disease detection

🎨 Better UI using Tailwind / CSS

📊 Symptom analytics dashboard
