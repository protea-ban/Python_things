from docx import Document
from docx.shared import RGBColor

boldText = []
redText = []
doc = Document("test.docx")

for p in doc.paragraphs:
    for r in p.runs:
        if r.bold:
            boldText.append(r.text)
        if r.font.color.rgb == RGBColor(255,0,0):
            redText.append(r.text)

result = {
    'bold text':boldText,
    'red text':redText,
    'both':set(boldText) & set(redText)
}

# 输出结果
for title in result.keys():
    print(title.center(30,'='))
    for text in result[title]:
        print(text)