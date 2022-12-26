import os
import azure.cognitiveservices.speech as speechsdk

async def tts(msg):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=str(os.getenv('SPEECH_KEY')), region="eastus")
    # speech_config = speechsdk.SpeechConfig(subscription="f373237de5d540efa08ac1ef02edeed2", region="eastus")
    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='zh-CN-shaanxi-XiaoniNeural'


    file_name = "/Users/taozhang/Desktop/My Porjects/MazeBot-for-Discord/voices/test.mp3"
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3)

    # file_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True, filename=file_name)

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)


    print(f'file_name: {msg}')
    # Get text from the console and synthesize to the default speaker.
    speech_synthesis_result = speech_synthesizer.speak_text_async(msg).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(msg))
        return True
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
        return False