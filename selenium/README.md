# 🕸️ Selenium Web Scraper

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Headless Chrome](https://img.shields.io/badge/Chrome-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)

</div>

## 📝 Table of Contents
- [English](#english)
  - [Description](#description)
  - [Features](#features)
  - [Technologies](#technologies)
  - [Installation](#installation)
- [العربية](#العربية)
  - [الوصف](#الوصف)
  - [المميزات](#المميزات)
  - [التقنيات](#التقنيات)
  - [التثبيت](#التثبيت)

## English

### Description
A powerful and flexible web scraping tool built with Python and Selenium. This project allows you to extract structured data and HTML content from any website, with advanced features like dynamic scrolling, metadata extraction, and user-agent randomization.

### Features
✨ **Core Features**
- Extracts page content and structured data (titles, links, images, articles, metadata)
- Supports dynamic scrolling for infinite-scroll pages
- Saves scraped HTML and data as JSON in `scraped_data/`
- Handles timeouts and errors gracefully
- Custom user-agent for each session

🚀 **Technical Features**
- Headless Chrome browser for fast, background scraping
- Modular, object-oriented code
- Easy to extend for new selectors or data types

### Technologies
- **Core**: Python, Selenium
- **Browser**: Headless Chrome
- **User-Agent**: fake-useragent
- **Data Storage**: JSON, HTML

### Installation
1. **Clone the repository**
```bash
git clone <your-repo-url>
cd selenium
```
2. **Install dependencies**
```bash
pip install -r requirements.txt
```
3. **Download ChromeDriver**
- Download the correct version of ChromeDriver for your Chrome browser from [here](https://chromedriver.chromium.org/downloads)
- Update the `DRIVER_PATH` in `selenium1.py` to the location of your `chromedriver.exe`

4. **Run the scraper**
```bash
python selenium1.py
```
5. **Follow the prompt**
- Enter the website URL when prompted.
- Scraped data will be saved in the `scraped_data/` folder.

---

## العربية

### الوصف

أداة قوية ومرنة لاستخلاص البيانات من الويب باستخدام بايثون وسيلينيوم. يتيح لك هذا المشروع استخراج البيانات المنظمة ومحتوى HTML من أي موقع، مع ميزات متقدمة مثل التمرير الديناميكي واستخراج بيانات الميتا وتغيير وكيل المستخدم تلقائيًا.

### المميزات
✨ **الميزات الأساسية**
- استخراج محتوى الصفحة والبيانات المنظمة (العناوين، الروابط، الصور، المقالات، بيانات الميتا)
- يدعم التمرير التلقائي للصفحات ذات التمرير اللانهائي
- حفظ البيانات المستخرجة كملفات HTML وJSON في مجلد `scraped_data/`
- معالجة الأخطاء وانتهاء المهلة بشكل ذكي
- وكيل مستخدم عشوائي لكل جلسة

🚀 **الميزات التقنية**
- متصفح كروم بدون واجهة (Headless) لسرعة الاستخلاص
- كود منظم وقابل للتطوير
- سهل التوسعة لإضافة محددات أو أنواع بيانات جديدة

### التقنيات
- **الأساس**: بايثون، سيلينيوم
- **المتصفح**: كروم بدون واجهة
- **وكيل المستخدم**: fake-useragent
- **تخزين البيانات**: JSON، HTML

### التثبيت
1. **استنساخ المستودع**
```bash
git clone <your-repo-url>
cd selenium
```
2. **تثبيت المتطلبات**
```bash
pip install -r requirements.txt
```
3. **تحميل ChromeDriver**
- قم بتحميل النسخة المناسبة من ChromeDriver حسب إصدار متصفحك من [هنا](https://chromedriver.chromium.org/downloads)
- حدث مسار `DRIVER_PATH` في ملف `selenium1.py` حسب مكان chromedriver.exe

4. **تشغيل الأداة**
```bash
python selenium1.py
```
5. **اتبع التعليمات**
- أدخل رابط الموقع عند الطلب.
- سيتم حفظ البيانات المستخرجة في مجلد `scraped_data/`.

---

## 👨‍💻 Developer
- **Name**: م محمد علي حزام
- **GitHub**: [H7ugf](https://github.com/H7ugf/projects_py.git)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 