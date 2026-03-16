# 🌐 Language Translator

A web-based language translation tool that enables users to translate text between **English**, **Tamil**,  **Malayalam**, **Telugu**, **Kannada** and **Hindi** using a simple and intuitive user interface. This project leverages a **Python Flask** backend with the **Google Translate API** to provide translations. 🌍✨

## Features 🔑

- **Multi-language Translation**: Translate text between English, Tamil, Malayalam, Telugu, Kannada and Hindi. 🌐
- **User-Friendly Interface**: Built with HTML, CSS, and JavaScript to create a seamless experience. 💻
- **Real-Time Translation**: Automatic language detection and dynamic translation. ⚡
- **Responsive Design**: Works well on both desktop and mobile devices. 📱

## Technologies Used ⚙️

### Frontend:
- **HTML5**: Structure of the page. 📑
- **CSS3**: Styling with responsive design for different screen sizes. 🎨
- **JavaScript**: For handling user interactions and API calls to the backend. 📡

### Backend:
- **Python 3.12.9**: Backend language. 🐍
- **Flask**: Lightweight web framework for the backend. 🔥
- **Deep Translator**: A Python library that provides access to multiple translation services such as Google Translate. 🌐
- **Flask-CORS**: For handling Cross-Origin Resource Sharing (CORS) issues in API requests. 🔄

## Installation 💾

### Prerequisites
Make sure you have **Python 3.12.9** or similar versions. You also need `git` to clone the repository. 🖥️

Clone the repository:
```
git clone https://github.com/Shrivishal007/Language-Translator.git
cd Language-Translator
```

Install the required dependencies:
```
pip install -r requirements.txt
```

## Running the Backend 🚀

Start the Flask server:
```
python translate.py
```

The backend server will be running at:
```
http://127.0.0.1:5000
```

## Running the Frontend 🌍

Simply open the `index.html` file in your web browser. The user interface will be displayed, where you can:
- Select the source language (English, Tamil, Malayalam, Telugu, Kannada or Hindi). 🔄
- Enter the text to be translated. ✍️
- Select the target language for translation. 🔄
- Press "Translate" to view the output. 🚀

## How to Use 📖

1. Select the source language (English, Tamil, Malayalam, Telugu, Kannada or Hindi) from the "Select the Input Language" dropdown. 🗣️
2. Enter the text you want to translate in the input text area. 📝
3. Select the target language (English, Tamil, Malayalam, Telugu, Kannada or Hindi) from the "Select the Target Language" dropdown. 🗣️
4. Press the "Translate" button to see the translated text in the output area. 🔄

## Contribution 🤝

This project was developed by Shrivishal, with backend contributions by [Yuvaraj B](https://github.com/yuvii-b). 🙌
If you would like to contribute:
1. Fork the repository. 🍴
2. Create a new branch (git checkout -b feature-name). 🌱
3. Commit your changes (git commit -am 'Add new feature'). 📦
4. Push to the branch (git push origin feature-name). 🚀
5. Create a new Pull Request. 🔄

## License 📜

This project is licensed under the MIT License 📜
[MIT License](LICENSE)

## Acknowledgements 🙏

- Deep Translator: Python library used for translation services 🌐
- Flask: A lightweight web framework for Python. Flask Documentation 🔥
- Font Awesome: For the icons used in the UI. Font Awesome 🎨
- Google Fonts: For the fonts used in the design. Google Fonts ✨

## Troubleshooting 🛠️

- Backend not starting: Ensure all dependencies are installed. Run pip install -r requirements.txt to install missing libraries. ⚠️
- CORS Issues: If you encounter issues related to cross-origin requests, ensure the Flask-CORS package is correctly installed. 🔄
