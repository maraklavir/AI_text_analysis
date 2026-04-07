import re
from collections import Counter
from openai import OpenAI

import os
MOJ_KLJUC = os.getenv("OPENAI_API_KEY")

print("--- START ANALIZE ---")

text = """
What Is a Woman? is a 2022 American documentary 
film about gender and transgender issues, directed 
by Justin Folk and presented by conservative political 
commentator Matt Walsh. It was released by conservative website The 
Daily Wire. In it, Walsh asks various people "What is a woman?" with the goal of 
showing them that their definition of womanhood is 
circular.[1] Walsh said he made it in opposition to gender ideology.[2][1]
It is described in many sources as anti-trans[3] or transphobic.[4][5][6] 
It was released to subscribers of The Daily Wire on June 1, 2022, coinciding 
with the start of Pride Month.[7]
What Is a Woman? received mixed reviews. Walsh's approach garnered praise 
from conservative commentators, while drawing criticism from other sources, 
including advocates of transgender healthcare.[1][5] According to transgender 
activists and others who appeared in it, Walsh had invited individuals to participate
under false pretenses.[8][9][10] Walsh's tour to showcase What Is a Woman? at college
campuses sparked protests.[11][12] In June 2023, during the subsequent Pride Month, it
gained further attention when Elon Musk promoted it on Twitter.[13] The title, "What is 
a woman?", has become a widespread rhetorical question in anti-trans discourse.[14]
"""

# Obrada teksta za brojanje riječi
text_clean = text.lower()
text_clean = re.sub(r'[^\w\s]', '', text_clean)
words = text_clean.split()
word_counts = Counter(words)

print("\nNajčešćih 5 riječi:")
for word, count in word_counts.most_common(5):
    print(f"{word}: {count}")

# Poziv AI-u
client = OpenAI(api_key=MOJ_KLJUC)

print("\nŠaljem upit AI-u... molim sačekaj.")

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Summarize this text in 2 sentences:\n{text}"}
        ]
    )
    print("\nAI summary:")
    print(response.choices[0].message.content)

except Exception as e:
    print("\nDOŠLO JE DO GREŠKE:")
    print(e)
    