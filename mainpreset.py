import youtube_dl
from enum import Enum


class YLFormat(Enum):
    m4a = '140'  # audio only
    mp4_144p = '160'
    mp4_240p = '133'
    mp4_360p = '134'
    mp4_480p = '135'
    mp4_720p = '136'
    mp4_1080p = '137'
    gp3_176_144 = '17'  # 3gp: 176*144
    gp3_320_240 = '36'
    flv = '5'
    webm = '43'
    mp4_640_360 = '18'  # 640 * 360
    mp4_1280_720 = '22'


def download(url: str, options: dict):
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])


download_list = [  # edit this
    ('https://www.youtube.com/watch?v=vbttZVTSJRU', YLFormat.mp4_640_360, YLFormat.mp4_1280_720, ...),
]

for cur_data in download_list:
    cur_url, tuple_format = cur_data[0], cur_data[1:]
    for format_info in tuple_format:
        if not isinstance(format_info, YLFormat):
            print(f'the format is not correct. format: {format_info}')
            continue
        fmt_name, fmt = format_info.name, format_info.value
        try:
            download(cur_url, dict(format=fmt,
                                   outtmpl=f'%(title)s-{fmt_name}.%(ext)s',
                                   # ignoreerrors=True,
                                   # quiet=True
                                   ))
        except youtube_dl.utils.DownloadError:
            print(f'download error: {cur_url} | {fmt_name}')