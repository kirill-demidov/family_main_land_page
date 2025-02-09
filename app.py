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
            text-align: center;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
        }
        .site-list {
            list-style: none;
            padding: 0;
        }
        .site-list li {
            margin: 15px 0;
            padding: 10px;
            background: #e0e0e0;
            border-radius: 5px;
        }
        .site-list a {
            text-decoration: none;
            font-size: 18px;
            color: #007BFF;
            display: block;
        }
        .site-list p {
            margin: 5px 0 0;
            font-size: 14px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Путеводитель по нашим WEB сайтам</h1>
        <ul class="site-list">
            {% for site in sites %}
            <li>
                <a href="{{ site['url'] }}" target="_blank">{{ site['name'] }}</a>
                <p>{{ site['description'] }}</p>
            </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    sites = [
        {"name": "Family Web", "url": "https://family-web-16542874441.europe-central2.run.app",
         "description": "Семейная информация"},
        {"name": "Gen Web", "url": "https://gen-web-16542874441.europe-central2.run.app",
         "description": "Бизнес по генеалогии Евгении"},
        {"name": "Geo Web", "url": "https://geo-web-16542874441.europe-central2.run.app",
         "description": "Заготовка сайта по геоэкономике для Данилина"},
        {"name": "LLM Web", "url": "https://llm-web-16542874441.europe-central2.run.app",
         "description": "Новости для НДИ"},
        {"name": "Modeler Web", "url": "https://modeler-web-16542874441.us-central1.run.app",
         "description": "Моделер (процессор данных)"},
        {"name": "Sozd Web", "url": "https://sozd-web-16542874441.europe-central2.run.app",
         "description": "Законопроекты ГД РФ"},
        {"name": "Traffic Lamas", "url": "https://traffic-lamas-16542874441.europe-central2.run.app",
         "description": "Расчет рисков при планировании поездок"},
    ]
    return render_template_string(HTML_TEMPLATE, sites=sites)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
