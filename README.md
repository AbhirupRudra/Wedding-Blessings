# 💍 Digital Wedding Video Guestbook (Offline/Local)

A private, locally hosted web application that allows wedding guests to record video messages using their own smartphones. The videos are streamed over a local Wi-Fi network and saved directly to the host laptop.

## ✨ Features

* **Offline First:** No internet required. Works entirely over a local Wi-Fi network (or Hotspot).
* **Zero Install for Guests:** Guests scan a QR code or type a URL; no app download needed.
* **Personalized Experience:** Guests enter their name before recording, and the interface greets them personally.
* **Automated Organization:** Video files are automatically renamed with the guest's name and a timestamp (e.g., `Aunt_Joy_20251210_143001.webm`).
* **Cross-Platform:** Works on iOS (Safari) and Android (Chrome) using a self-signed SSL certificate.

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML5, CSS3, JavaScript (MediaRecorder API)
* **Security:** `pyopenssl` (for ad-hoc SSL/HTTPS)

## 📂 Project Structure

```text
WeddingGuestbook/
│
├── app.py                 # Main Flask server application
├── wedding_videos/        # (Auto-generated) Folder where guest videos are saved
└── templates/
    ├── index.html         # Landing page (Name entry)
    └── record.html        # Recording interface
 
