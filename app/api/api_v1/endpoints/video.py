import os

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import StreamingResponse


router = APIRouter()


def chunks_from_stream(source, chunk_size, start, size):
    bytes_read = 0
    with open(source, mode='rb') as stream:
        stream.seek(start)
        while bytes_read < size:
            bytes_to_read = min(chunk_size, size - bytes_read)
            yield stream.read(bytes_to_read)
            bytes_read = bytes_read + bytes_to_read


@router.get('/pexels')
def stream_video(request: Request):
    range = request.headers.get('Range')
    start, end = range.replace('bytes=', '').split('-')
    start = int(start)
    end = int(end) if end else start + 1024*1024
    source = '/home/tomi/git/testimonial/testimonial-api/pexels-solodsha-9008406.mp4'
    total_size = os.path.getsize(source)

    return StreamingResponse(
        chunks_from_stream(
            source,
            start=start,
            chunk_size=1024*1024,
            size=total_size),
        headers={
            'Accept-Ranges': 'bytes',
            'Content-Range': f'bytes {start}-{start + 1024*1024}/{total_size}',
            'Content-Type': 'video/mp4'
        },
        status_code=206)
