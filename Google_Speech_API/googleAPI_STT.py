# Youlim & Hyunji Code
# 환경 설정 참고 블로그 https://ninano1109.tistory.com/41

def transcribe_gcs_with_word_time_offsets(speech_file):

    """Transcribe the given audio file asynchronously and output the word time
    offsets."""

    from google.cloud import speech
    import io

    # Instantiates a client
    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ko-KR",
        enable_word_time_offsets=True,
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    result = operation.result(timeout=90)

    for result in result.results:
        alternative = result.alternatives[0]
        print("Transcript: {}".format(alternative.transcript))
        print("Confidence: {}".format(alternative.confidence))

        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time

            print(
                f"Word: {word}, start_time: {start_time.total_seconds()}, end_time: {end_time.total_seconds()}"
            )

transcribe_gcs_with_word_time_offsets('../audio&data/sample2.wav')

# 결과를 json 파일로 저장하도록 추출 진행 필요