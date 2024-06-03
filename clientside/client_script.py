import asyncio
import sounddevice
import numpy as np
import pyvirtualcam
import cv2 
import multiprocessing
import requests, uuid
import os
import sys
from PIL import ImageFont, ImageDraw, Image
from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent, TranscriptResultStream
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
TRANSLATE_KEY = os.getenv("TRANSLATE_KEY")

try:
    file_path = os.getcwd() + r"\clientside\client_captions.txt"
    os.chmod(file_path, 0o644)
    file_path = os.getcwd() + r"\clientside\client_script_file.txt"
    os.chmod(file_path, 0o644)
except:
    pass

file_in = open(os.getcwd() + r"\clientside\client_captions.txt", "w")
file_in.close()
script_file = open(os.getcwd() + r"\clientside\client_script_file.txt", "w")
script_file.close()

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

class MyEventHandler(TranscriptResultStreamHandler):
    async def handle_transcript_event(self, transcript_event: TranscriptEvent):
        results = transcript_event.transcript.results
        if results and not results[0].is_partial:
            # This is the final result
            for result in results:
                for alt in result.alternatives:
                    text = alt.transcript
                    text = translate(text, fr = 'zh-CN', to = "en-US")
                    try:
                        file_in = open(os.getcwd() + r"\clientside\client_captions.txt", "a", encoding='utf-8-sig')
                        file_in.write(text + "\n")
                        file_in.close()
                        script_file = open(os.getcwd() + r"\clientside\client_script_file.txt", "a")
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        script_file.write(f"{timestamp} Client: {text}\n")
                        script_file.close()
                    except:
                        pass
                    print(alt.transcript)
                    print(text)

async def mic_stream():
    loop = asyncio.get_event_loop()
    input_queue = asyncio.Queue()

    def callback(indata, frame_count, time_info, status):
        loop.call_soon_threadsafe(input_queue.put_nowait, (bytes(indata), status))

    stream = sounddevice.RawInputStream(
        channels=1,
        samplerate=16000,
        callback=callback,
        blocksize=1024 * 2,
        dtype="int16",
    )

    with stream:
        while True:
            indata, status = await input_queue.get()
            yield indata, status


async def write_chunks(stream):
    async for chunk, status in mic_stream():
        await stream.input_stream.send_audio_event(audio_chunk=chunk)
    await stream.input_stream.end_stream()


async def basic_transcribe():
    client = TranscribeStreamingClient(region="us-east-1")
    language_codes = ["zh-CN", "en-AU", "en-GB", "en-US", "fr-FR", "fr-CA", "de-DE", 
                    "hi-IN", "ja-JP", "ko-KR", "pt-BR", "es-US", "th-TH"]

    stream = await client.start_stream_transcription(
        language_code="zh-CN",
        media_sample_rate_hz=16000,
        media_encoding="pcm",
    )

    handler = MyEventHandler(stream.output_stream)
    await asyncio.gather(write_chunks(stream), handler.handle_events())


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(basic_transcribe())
    loop.close()

def cam():

    def draw_caption(text, x1, y1, x2, y2, x_text, y_text):
        img_pil = Image.fromarray(frame)
        draw = ImageDraw.Draw(img_pil, "RGBA")

        draw.rectangle([x1, y1, x2, y2], fill=(0, 0, 0, 127))
        draw.text((x_text, y_text),  text, font = font, fill = (255, 50, 50))

        return img_pil

    vid = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)

    fontpath = "./simsun.ttc"
    font = ImageFont.truetype(fontpath, 32)

    with pyvirtualcam.Camera(height=720, width=1280, fps=30) as cam:
        print(f'Using virtual camera: {cam.device}')
        while True:
            ret, frame = vid.read() 
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            try:
                file_out = open(os.getcwd() + r"\clientside\client_captions.txt", "r", encoding='utf-8-sig')
                text = file_out.readlines()[-1].rstrip()
                file_out.close()
                def get_x(length_text):
                    x = int(max(32, (frame.shape[1] / 2) - 8 * length_text))
                    return x
                
                y = int(frame.shape[0] * 0.82)

                if len(text) <= 76:
                    x = get_x(len(text))
                    
                    frame = np.array(draw_caption(text, x-5, y-5, x + font.getbbox(text)[2], y+40, x, y))

                else:
                    t = text.split()

                    t1 = " ".join(t[:(len(t) // 2)])
                    t2 = " ".join(t[len(t)//2:])

                    x1 = get_x(len(t1))
                    x2 = get_x(len(t2))

                    frame = np.array(draw_caption(t1, x1-5, y-5, x1 + font.getbbox(t1)[2], y+40, x1, y))
                    frame = np.array(draw_caption(t2, x2-5, y+40, x2 + font.getbbox(t2)[2], y+80, x2, y+40))
            except:
                pass


            frame = cv2.flip(frame, 1)
            cam.send(frame)
            cam.sleep_until_next_frame()


def translate(text, fr, to):
    key = TRANSLATE_KEY
    endpoint = "https://api.cognitive.microsofttranslator.com"
    location = "eastus"
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': fr,
        'to': to
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return(response[0]['translations'][0]['text'])

def run():
    t1 = multiprocessing.Process(target=cam)
    t2 = multiprocessing.Process(target=main)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

def stop():
    sys.exit()