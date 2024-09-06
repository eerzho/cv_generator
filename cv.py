from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet

# Регистрация всех стилей шрифта DejaVuSerif
pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSerif-Bold', 'DejaVuSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSerif-Italic', 'DejaVuSerif-Italic.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSerif-BoldItalic', 'DejaVuSerif-BoldItalic.ttf'))

# Создание FontFamily для связки стилей шрифта
pdfmetrics.registerFontFamily('DejaVuSerif', normal='DejaVuSerif', bold='DejaVuSerif-Bold',
                              italic='DejaVuSerif-Italic', boldItalic='DejaVuSerif-BoldItalic')

# File path
pdf_output_path = "RU_CV_Zhanbolat_Yerkinbay.pdf"

# Create a PDF document
doc = SimpleDocTemplate(pdf_output_path, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=35, bottomMargin=18)

# Использование зарегистрированного FontFamily
styles = getSampleStyleSheet()
styles['Normal'].fontName = 'DejaVuSerif'

Story = []

# Add content to PDF
style = styles['Normal']

header = Paragraph("<b>Жанболат Еркинбай</b><br/>28.05.1999<br/>Прага, Чехия<br/>"
                   "eerzho@gmail.com<br/>github.com/eerzho | linkedin.com/in/eerzho | leetcode.com/u/eerzho", style)
Story.append(header)
Story.append(Spacer(1, 7))

# Work Experience
work_header = Paragraph("<b>Опыт работы</b>", style)
Story.append(work_header)
Story.append(Spacer(1, 7))

experience_text = [
    ("<b>Go Developer</b>", "Май 2024 - настоящее время", "Freelance", 
     "- Создал Telegram-бота с использованием OpenAI API, что позволило разрабатывать интерактивные сценарии и автоматизировать взаимодействие с пользователями. Бот помог улучшить качество обслуживания, оперативно отвечая на запросы и предоставляя необходимую информацию."),

    ("<b>PHP Symfony Developer</b>", "Февраль 2023 - настоящее время", "Slotegrator, Прага, Чехия",
     "- Разрабатывал библиотеку для интеграции микросервисов — это сильно ускорило процесс их интеграции.",
     "- Работал над SEO-сервисом, который дал возможность администраторам самим управлять SEO-контентом. Теперь обновления на сайте происходят быстрее, а позиции в поиске улучшились.",
     "- Создавал Content-сервис, который позволил администраторам самостоятельно управлять контентом на сайте. Это уменьшило количество запросов к разработчикам и упростило процесс изменений."),

    ("<b>PHP Developer</b>", "Декабрь 2021 - Февраль 2023", "Slotegrator, Прага, Чехия",
     "- Участвовал в разработке различных клиентских проектов, создавал новые модули с полезной функциональностью.",
     "- Исправлял баги, следил за стабильностью работы приложений. Быстро устранял ошибки и внедрял улучшения для повышения производительности и безопасности."),

    ("<b>PHP Laravel Developer</b>", "Январь 2021 - Ноябрь 2021", "PFDO, Москва, Россия",
     "- Разработал сервис для коммуникации и поддержки клиентов через email, заменив стандартный email-клиент. Это позволило оптимизировать процесс общения с клиентами, особенно в случаях длительной переписки и большого объема запросов."),

    ("<b>PHP Laravel Developer</b>", "Июль 2020 - Январь 2021", "Alasys, Алматы, Казахстан",
     "- Работал над онлайн-платформой для обучения, улучшал интерфейс и добавлял новые функции, чтобы сделать использование более интуитивным.",
     "- Разработал систему контроля закупок, добавил новые функции и оптимизировал процессы, что помогло более эффективно управлять закупками.")
]

# Adding work experience
for job in experience_text:
    Story.append(Paragraph(job[0], style))
    Story.append(Paragraph(job[1], style))
    Story.append(Paragraph(job[2], style))
    for line in job[3:]:
        Story.append(Paragraph(line, style))
    Story.append(Spacer(1, 7))

# Education
education_header = Paragraph("<b>Образование</b>", style)
Story.append(education_header)
Story.append(Spacer(1, 7))

education_text = [
    "Международный университет информационных технологий",
    "Алматы, Казахстан",
    "Сентябрь 2017 - Июль 2021",
    "Бакалавр, Вычислительная техника и программное обеспечение"
]

for line in education_text:
    Story.append(Paragraph(line, style))
Story.append(Spacer(1, 7))

# Technical Skills
skills_header = Paragraph("<b>Технические навыки</b>", style)
Story.append(skills_header)
Story.append(Spacer(1, 7))

skills_text = [
    "Языки: Go, PHP, JavaScript, SQL",
    "Фреймворки: Gin, Chi, Symfony, Laravel",
    "Инструменты: Rest API, Git, CI/CD, Docker, AWS, Redis, Kafka, RabbitMQ, Jenkins, ELK, Jira, Confluence, Notion, MongoDB, PostgreSQL, MySQL"
]

for line in skills_text:
    Story.append(Paragraph(line, style))

# Build the PDF
doc.build(Story)

pdf_output_path
