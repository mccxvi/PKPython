# PKPython
Python app that shows connection, price, changes etc. for a given route from PKP Bilkom website in a Terminal.

![Demo](demo.gif)

## Python Setup

Clone repo and create virtual environment
```
git clone https://github.com/mccxvi/PKPython.git
python3 -m venv PKPython
cd PKPython
```

Activate the virtual environment for this project

Windows /
```
Scripts\activate.bat
```

Linux & MacOS /

```
source bin/activate
```

Install required packages with pip

```
pip install -r requirements.txt
```

## Selenium Web Driver

Download appropriate version of [ChromeDriver](https://chromedriver.chromium.org/downloads) for your OS and specify the executable path in:

```
WebDriverPath = ""
```

## TODO List

- — English Localization
- — User specified time of the connection
- — Preview of a complete route with their time of departure/arrival and track numbers
