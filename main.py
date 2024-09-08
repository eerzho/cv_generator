from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
pdfmetrics.registerFont(TTFont('DejaVuSerif', os.path.join(base_dir, 'fonts/DejaVuSerif.ttf')))
pdfmetrics.registerFont(TTFont('DejaVuSerif-Bold', os.path.join(base_dir,'fonts/DejaVuSerif-Bold.ttf')))
pdfmetrics.registerFont(TTFont('DejaVuSerif-Italic', os.path.join(base_dir,'fonts/DejaVuSerif-Italic.ttf')))
pdfmetrics.registerFont(TTFont('DejaVuSerif-BoldItalic', os.path.join(base_dir,'fonts/DejaVuSerif-BoldItalic.ttf')))

pdfmetrics.registerFontFamily(
    'DejaVuSerif', 
    normal='DejaVuSerif', 
    bold='DejaVuSerif-Bold',
    italic='DejaVuSerif-Italic', 
    boldItalic='DejaVuSerif-BoldItalic'
)

pdf_output_path = "RU_CV_Zhanbolat_Yerkinbay.pdf"

doc = SimpleDocTemplate(pdf_output_path, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=35, bottomMargin=18)

styles = getSampleStyleSheet()
styles['Normal'].fontName = 'DejaVuSerif'

name_style = ParagraphStyle(
    'Name',
    parent=styles['Normal'],
    fontSize=16,  
    alignment=TA_CENTER
)

centered_style = ParagraphStyle(
    'Centered',
    parent=styles['Normal'],
    alignment=TA_CENTER
)

Story = []

header = Paragraph("<b>Жанболат Еркинбай</b>", name_style)
Story.append(header)
Story.append(Spacer(1, 7))

subheader = Paragraph("28.05.1999 | Прага, Чехия | eerzho@gmail.com", centered_style)
Story.append(subheader)
Story.append(Spacer(1, 7))

links = Paragraph("linkedin.com/in/eerzho | github.com/eerzho | leetcode.com/u/eerzho", centered_style)
Story.append(links)
Story.append(Spacer(1, 14))

style = styles['Normal']

work_header = Paragraph("<b>Опыт работы</b>", style)
Story.append(work_header)
Story.append(Spacer(1, 7))

experience_text = [
    ("<b>Go Developer</b>", "Май 2024 - настоящее время", "Freelance", 
     "- Для автоматизации взаимодействия с пользователями был создан бот Telegram с интегрированным OpenAI API. Бот повысил качество обслуживания, быстро реагируя на запросы и предоставляя необходимую информацию.",
     "- Разрабатываю собственный сервис аутентификации, обеспечивающий высокую степень защиты и контроля доступа к пользовательским данным."),

    ("<b>PHP Symfony Developer</b>", "Ноябрь 2022 - настоящее время", "Slotegrator, Прага, Чехия",
     "- Разрабатывал библиотеку для интеграции внутренних микросервисов, что значительно ускорило процесс интеграции.",
     "- Работал над SEO-сервисом, который позволяет администраторам самостоятельно управлять SEO-контентом. Это ускорило обновление сайта и повысило его рейтинг в поисковых системах.",
     "- Участвовал в разработке Content-сервиса, который позволяет администраторам самостоятельно управлять контентом сайта, сокращая количество запросов к разработчикам и упрощая процесс внесения изменений."),

    ("<b>PHP Developer</b>", "Декабрь 2021 - Ноябрь 2022", "Slotegrator, Чехия (удаленно)",
     "- Участвовал в разработке PHP-сайтов клиента, создавая новые функции.",
     "- Исправлял ошибки, следил за стабильностью работы сайтов, оперативно устранял ошибки и внедрял улучшения для повышения производительности и безопасности."),

    ("<b>PHP Laravel Developer</b>", "Январь 2021 - Ноябрь 2021", "PFDO, Россия (удаленно)",
     "- Разработал сервис для общения с клиентами и их поддержки через электронную почту вместо стандартного почтового клиента. Это позволило оптимизировать процесс общения с клиентами и было особенно эффективно в случаях длительных переписок и большого количества запросов."),

    ("<b>PHP Laravel Developer</b>", "Июль 2020 - Январь 2021", "Alasys, Алматы, Казахстан",
     "- Работал над платформой онлайн-обучения, улучшая интерфейс и добавляя новые функции для повышения удобства использования.",
     "- Была разработана система управления закупками, в которую были добавлены новые функции и оптимизированы процессы для более эффективного управления закупками.")
]

for job in experience_text:
    Story.append(Paragraph(job[0], style))
    Story.append(Paragraph(job[1], style))
    Story.append(Paragraph(job[2], style))
    for line in job[3:]:
        Story.append(Paragraph(line, style))
    Story.append(Spacer(1, 7))

education_header = Paragraph("<b>Образование</b>", style)
Story.append(education_header)
Story.append(Spacer(1, 7))

education_text = [
    "Международный университет информационных технологий",
    "Сентябрь 2017 - Июль 2021",
    "Алматы, Казахстан",
    "Бакалавр, Вычислительная техника и программное обеспечение"
]

for line in education_text:
    Story.append(Paragraph(line, style))
Story.append(Spacer(1, 7))

skills_header = Paragraph("<b>Технические навыки</b>", style)
Story.append(skills_header)
Story.append(Spacer(1, 7))

skills_text = [
    "Языки: Go, PHP, JavaScript, SQL",
    "Фреймворки: Gin, Chi, Symfony, Laravel",
    "Инструменты: PostgreSQL, MongoDB, MySQL, Rest API, Git, CI/CD, Docker, MinIO, Redis, Kafka, RabbitMQ, Jenkins, ELK, Jira, Confluence, Notion"
]

for line in skills_text:
    Story.append(Paragraph(line, style))

doc.build(Story)

pdf_output_path
