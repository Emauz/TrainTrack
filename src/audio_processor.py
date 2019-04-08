""" Takes audio and sends it to DialogFlow """

import dialogflow_v2 as df


def process_audio_file(session_id, file_name):
    dialogflow_client = df.SessionsClient()

    with open(file_name, 'rb') as audio_file:
        input_audio = audio_file.read()

    # setup audio configurations

    # TERMPORARILY HARDCODED
    encoding = df.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
    sample_rate = 16000
    language_code = "en-US"
    project_id = "traintrack-236905"

    # read input file as variable
    audio_config = df.types.InputAudioConfig(
        audio_encoding=encoding, language_code=language_code, sample_rate_hertz=sample_rate)
    query_input = df.types.QueryInput(audio_config=audio_config)

    # set up session tokens and what not
    session = dialogflow_client.session_path(project_id, session_id)

    # query DialogFlow for intent
    response = dialogflow_client.detect_intent(session=session, query_input=query_input, input_audio=input_audio)
    return response


process_audio_file("0", "/home/eric/Audio/mozilla_commonvoice/test_audio.mp3")
