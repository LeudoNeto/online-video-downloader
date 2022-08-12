from django.shortcuts import render
from pytube import YouTube
from django.http import HttpResponse
from os import remove

def index(request):
    if request.method == "POST":
        website = request.POST.get('website')
        url = request.POST.get('url')
        resolution = request.POST.get('video')
        quality = request.POST.get('audio')

        if resolution:
            video = YouTube(url).streams.filter(resolution=resolution, progressive=True)[0]
            filename = f'{video.title}.{video.subtype}'
            video.download(output_path='videos', filename=filename)

            with open (f'videos/{filename}', 'rb') as video:
                response = HttpResponse(video, content_type='application/vnd.mp4')
                response['Content-Disposition'] = 'attachment; filename=' + filename
                remove(f'videos/{filename}')
                return response
        

        audio = YouTube(url).streams.filter(abr=quality)[0]
        filename = f'{audio.title}.{audio.mime_type[audio.mime_type.index("/")+1:]}'
        audio.download(output_path='audios', filename=filename)

        with open (f'audios/{filename}', 'rb') as audio:
            response = HttpResponse(audio, content_type='application/vnd.mp3')
            response['Content-Disposition'] = 'attachment; filename=' + filename
            remove(f'audios/{filename}')
            return response


    website = request.GET.get('website')
    url = request.GET.get('url')

    if not url:
        return render(request, 'index.html')
    
    else:
        video = YouTube(url)

        audios = video.streams.filter(type='audio')

        context = {
            'url' : url,
            'website' : website,
            'video' : video,
            'best_video' : video.streams.get_highest_resolution(),
            'videos' : video.streams.filter(progressive=True, type='video'),
            'audios' : audios,
            'best_audio' : audios[-1]
        }

        return render(request, 'index.html', context)

def videodownload(request):
    video.streams.get_lowest_resolution().download(output_path='videos', filename='teste.mp4')

    with open ('videos/teste.mp4', 'rb') as video:
        response = HttpResponse(video, content_type='application/vnd.png')
        response['Content-Disposition'] = 'attachment; filename=' + 'teste.mp4'
        return response