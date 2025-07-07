def count_words(text):
    words = text.split()  # Splits on any whitespace
    return len(words)

input_text = 'Liebe Julia, herzlichen Glückwunsch zu deiner neuen Wohnung! Ich freue mich total für dich. Ein Umzug ist nie einfach, aber es ist toll, wenn man danach ein schönes Zuhause hat. Wie ist deine neue Wohnung? Ist sie größer oder kleiner als deine alte? Hast du einen Balkon oder vielleicht sogar einen Garten? Und wie gefällt dir die neue Umgebung – sind die Nachbarn nett? Ich würde deine Wohnung sehr gern mal sehen. Hättest du am nächsten Samstag oder Sonntag Zeit? Ich könnte Kuchen mitbringen und dir beim Auspacken helfen, wenn noch etwas zu tun ist. Ich bin gespannt auf deine Antwort. Viel Erfolg beim Einrichten und liebe Grüße! Dein Vignesh'
word_count = count_words(input_text)
print(f"Total words: {word_count}")