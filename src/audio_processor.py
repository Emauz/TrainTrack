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
    print("Started new session with path: {}\n".format(session))

    # query DialogFlow for intent
    response = dialogflow_client.detect_intent(session=session, query_input=query_input, input_audio=input_audio)
    return response

def debug_print(payload):
    print('=' * 20)
    print('Interpreted query: {}'.format(payload.query_result.query_text))
    print('Response text: {}'.format(payload.query_result.fulfillment_text))
    # print out all fields:
    for entry in payload.query_result.parameters.fields:
        if payload.query_result.parameters.fields.get(entry):
            print(entry + ": ", end="")
            print(payload.query_result.parameters.fields.get(entry), end='')
    print(payload)


if __name__ == "__main__":
    import sys
    import random
    if(len(sys.argv) == 1):
        print("Must provide a file to process")
    else:
        for p in sys.argv[1:]:
            debug_print(process_audio_file(random.randint(0, 1000), p))

