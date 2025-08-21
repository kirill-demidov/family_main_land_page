from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Список WEB</title>
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f4f4f4;
        text-align: left;
    }
    .container {
        max-width: 800px;
        _margin: 50px auto;
        margin-top: 50px;
        margin-left: 50px;
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #333;
    }
    .site-list-wrapper {
        display: flex;
        /* justify-content: center;  Удалить или закомментировать */
    }
    .site-list {
        display: flex;
        flex-wrap: wrap;
        width: 100%;
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .site-list li {
        flex: 0 0 50%;
        box-sizing: border-box;
        margin: 0;
        padding: 10px;
        background: #e0e0e0;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .site-list a {
        text-decoration: none;
        font-size: 18px;
        color: #007BFF;
        display: block;
    }
    .site-list p {
        margin: 5px 0 0;
        font-size: 16px;
        color: #666;
    }
</style>
</head>
<body>
    <div class="container">
        <h1>Путеводитель по нашим WEB сайтам</h1>
        <div class="site-list-wrapper">
            <ul class="site-list">
                {% for site in sites %}
                <li>
                    <a href="{{ site['url'] }}" target="_blank"
                            title="Переход на сайт {{site['url']}}">
                            <img src="/static/{{site['icon']}}" width="18" height="18">
                            <u>{{ site['name'] }}</u></a>
                    <p>{{ site['description'] }}</p>
                </li>
                {% endfor %}
            </ul>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    sites = [
        {"name": "Family Web", "url": "https://family-web-16542874441.europe-central2.run.app",
         "description": "Семейная информация", "icon": "dollar.png"},

        {"name": "Gen Web", "url": "https://gen-web-16542874441.europe-central2.run.app",
         "description": "Бизнес по генеалогии Евгении", "icon": "lupa.png"},

        {"name": "Geo Web", "url": "https://geo-web-16542874441.europe-central2.run.app",
         "description": "Заготовка сайта по гео-экономике для Данилина", "icon": "word.png"},

        {"name": "LLM Web", "url": "https://llm-web-16542874441.europe-central2.run.app",
         "description": "Новости для НДИ", "icon": "star_david.png"},

        {"name": "Modeler Web", "url": "https://modeler-web-16542874441.us-central1.run.app",
         "description": "Моделер (процессор данных)", "icon": "write_db.png"},

        {"name": "Sozd Web", "url": "https://sozd-web-16542874441.europe-central2.run.app",
         "description": "Законопроекты ГД РФ", "icon": "mobile_icon.png"},

        {"name": "URBAN Web", "url": "https://urban-web-16542874441.europe-central2.run.app",
         "description": "Видео из Youtube по URBAN и конкурентам", "icon": "youtube.png"},

        {"name": "Archive_index Web", "url": "https://archive-web-16542874441.europe-central2.run.app",
         "description": "Архивные документы", "icon": "archive_index.png"},

        {"name": "LIB Web", "url": "https://lib-web-16542874441.europe-central2.run.app",
         "description": "Библиотека публикаций", "icon": "library.png"},

        {"name": "Traffic Lamas", "url": "https://traffic-lamas-16542874441.europe-central2.run.app",
         "description": "Расчет рисков при планировании поездок", "icon": "motorway.png"},

        {"name": "Video Youtube", "url": "https://shu-web-16542874441.europe-central2.run.app",
         "description": "Видео и комментарии из Youtube", "icon": "multi_greater.png"},
    ]
    return render_template_string(HTML_TEMPLATE, sites=sites)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
