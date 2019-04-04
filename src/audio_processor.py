""" Takes audio and sends it to DialogFlow """

import dialogflow_v2 as df


def process_audio_file(file_name, language_code):
    # read input file as variable
    with open(file_name, 'rb') as audio_file:
        input_file = audio_file.read()

    # setup audio configurations

    # TERMPORARILY HARDCODED
    encoding = df.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
    sample_rate = 16000

    audio_config = df.types.InputAudioConfig(encoding, language_code, sample_rate)
    query_input = df.types.QueryInput(audio_config)

    # query DialogFlow for intent
    dialogflow_client = df.SessionsClient()
    response = dialogflow_client.detect_intent()
    return response

