from deep_translator import GoogleTranslator
import deep_translator

def translate_text(input_text, target_language='hi'):
    print(deep_translator.__version__)

    def translate_chunk(chunk):
        """Wrapper for Google Translate with character limit workaround."""
        translate = GoogleTranslator(source='auto', target=target_language).translate
        translated_text = ''
        source_text_chunk = ''

        for sentence in chunk.split('. '):
            sentence = sentence.strip()  # Remove leading/trailing whitespaces
            if len(sentence.encode('utf-8')) + len(source_text_chunk.encode('utf-8')) < 5000:
                source_text_chunk += '. ' + sentence if source_text_chunk else sentence
            else:
                translated_chunk = translate(source_text_chunk)
                translated_text += ' ' + translated_chunk if translated_chunk else ''
                
                if len(sentence.encode('utf-8')) < 5000:
                    source_text_chunk = sentence
                else:
                    message = '<<Omitted Word longer than 5000 bytes>>'
                    translated_text += ' ' + translate(message)
                    source_text_chunk = ''

        if source_text_chunk:
            translated_chunk = translate(source_text_chunk)
            translated_text += ' ' + translated_chunk if translated_chunk else ''

        return translated_text.strip()  # Remove leading/trailing whitespaces

    try:
        # Translate the input text
        translated_text = translate_chunk(input_text)

        # Return the translated text
        return translated_text
    except Exception as e:
        return str(e)
