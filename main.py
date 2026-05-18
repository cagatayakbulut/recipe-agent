import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

prompt = """
Sen bir Instagram yemek içerik üreticisisin.

Bugün için 1 yemek postu hazırla.

Şunları üret:
1. Türkçe tarif adı
2. English recipe title
3. Malzemeler Türkçe
4. Ingredients English
5. Yapılış Türkçe
6. Steps English
7. Türkçe Instagram caption
8. English Instagram caption
9. Hashtagler
10. AI görsel üretmek için İngilizce image prompt

Kurallar:
- Evde yapılabilir yemek olsun.
- Çok karmaşık olmasın.
- Aile dostu olsun.
- Instagram için sıcak ve iştah açıcı yaz.
- Görsel prompt İngilizce olsun.
- Çıktıyı düzenli başlıklarla ver.
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print("✅ AI Recipe Agent çalıştı")
print("-------------------------")
print(response.output_text)
