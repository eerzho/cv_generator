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

pdf_output_path = "EN_CV_Zhanbolat_Yerkinbay.pdf"

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

header = Paragraph("<b>Zhanbolat Yerkinbay</b>", name_style)
Story.append(header)
Story.append(Spacer(1, 7))

subheader = Paragraph("28.05.1999 | Prague, Czech Republic | eerzho@gmail.com", centered_style)
Story.append(subheader)
Story.append(Spacer(1, 7))

links = Paragraph("linkedin.com/in/eerzho | github.com/eerzho | leetcode.com/u/eerzho", centered_style)
Story.append(links)
Story.append(Spacer(1, 14))

style = styles['Normal']

work_header = Paragraph("<b>Work Experience</b>", style)
Story.append(work_header)
Story.append(Spacer(1, 7))

experience_text = [
    ("<b>Go Developer</b>", "May 2024 - Present", "Freelance", 
     "- Created a Telegram bot with integrated OpenAI API for automating interactions with users. The bot improved service quality by quickly responding to inquiries and providing necessary information.",
     "- Developing a custom authentication service that ensures high security and access control to user data."),

    ("<b>PHP Symfony Developer</b>", "November 2022 - Present", "Slotegrator, Prague, Czech Republic",
     "- Developed a library for integrating internal microservices, significantly speeding up the integration process.",
     "- Worked on an SEO service that allows admins to manage SEO content independently. This sped up website updates and improved its ranking in search engines.",
     "- Contributed to the development of a Content service, enabling admins to manage website content independently, reducing the need for developer involvement and streamlining the process."),

    ("<b>PHP Developer</b>", "December 2021 - November 2022", "Slotegrator, Czech Republic (Remote)",
     "- Contributed to the development of client PHP websites, adding new features.",
     "- Fixed bugs, ensured site stability, quickly addressed issues, and implemented improvements to enhance performance and security."),

    ("<b>PHP Laravel Developer</b>", "January 2021 - November 2021", "PFDO, Russia (Remote)",
     "- Developed a service for client communication and support via email, replacing the standard email client. This optimized the communication process and was especially effective for long conversations and high volumes of requests."),

    ("<b>PHP Laravel Developer</b>", "July 2020 - January 2021", "Alasys, Almaty, Kazakhstan",
     "- Worked on an online learning platform, improving the interface and adding new features to enhance usability.",
     "- Developed a procurement management system with new features and optimized processes for more efficient procurement management.")
]

for job in experience_text:
    Story.append(Paragraph(job[0], style))
    Story.append(Paragraph(job[1], style))
    Story.append(Paragraph(job[2], style))
    for line in job[3:]:
        Story.append(Paragraph(line, style))
    Story.append(Spacer(1, 7))

education_header = Paragraph("<b>Education</b>", style)
Story.append(education_header)
Story.append(Spacer(1, 7))

education_text = [
    "International University of Information Technology",
    "September 2017 - July 2021",
    "Almaty, Kazakhstan",
    "Bachelor's, Computer Engineering and Software"
]

for line in education_text:
    Story.append(Paragraph(line, style))
Story.append(Spacer(1, 7))

skills_header = Paragraph("<b>Technical Skills</b>", style)
Story.append(skills_header)
Story.append(Spacer(1, 7))

skills_text = [
    "Languages: Go, PHP, JavaScript, SQL",
    "Frameworks: Gin, Chi, Symfony, Laravel",
    "Tools: PostgreSQL, MongoDB, MySQL, Rest API, Git, CI/CD, Docker, MinIO, Redis, Kafka, RabbitMQ, Jenkins, ELK, Jira, Confluence, Notion"
]

for line in skills_text:
    Story.append(Paragraph(line, style))

doc.build(Story)

pdf_output_path
