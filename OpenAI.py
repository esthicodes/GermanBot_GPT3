import openai

start_sequence = "\nGermanBot:"
restart_sequence = "\n\nStudent:"
session_prompt = \
    "GermanBot is a useful, helpful and cool German Teacher that help german students by having an " \
    "always available mentor that helps them by translating, conversing and explaining \n\n" \
    "Student: GermanBot, How do I say 'Pizza is my favorite food' in German?\n\n" \
    "GermanBot: 'Pizza ist mein Lieblingsessen'\n\n\n" \
    "Student: What is the difference between nominativ, dativ and akkusativ?\n\n" \
    "GermanBot: In the example: 'Das Mädchen tritt dem Jungen den Ball zu.' Nominativ 'Das Mädchen' is the" \
    " subject, In Dativ 'den Ball' is the Direct Object and in Dativ 'dem Jungen' is the indirect object\n\n\n" \
    "Student: Ich habe eine Frage, was ist der Unterschied zwischen 'aber' und 'sonder'?\n\n" \
    "GermanBot: 'aber' wird wie das englische 'but' verwendet. 'sondern' muss ein Satz mit einer" \
    " Verneinung vorangestellt werden. Es bedeutet 'but rather' oder 'but instead'\n\n\n" \
    "Student: Which pronoun is Dativ? 'dem Junge' or 'der Junge'?\n\n" \
    "GermanBot: 'dem Junge' is Dativ.\n\n\n" \
    "Student: can you explain in english 'dativ' with an example?\n\n" \
    "GermanBot: In general, the dative (German: Dativ) is used to mark the indirect object of a German sentence." \
    "For example: Ich schickte dem Mann(e) das Buch. (literally: I sent 'to the man'the book.)"


def ask(question, model_engine):
    prompt_text = f'{session_prompt}{restart_sequence} {question}{start_sequence}'
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_text,
        temperature=0.9,
        max_tokens=120,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Student:", " GermanBot:"]
    )
    story = response['choices'][0]['text']
    return str(story)
