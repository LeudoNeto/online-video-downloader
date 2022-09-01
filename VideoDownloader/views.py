from django.shortcuts import render
from pytube import YouTube
from django.http import HttpResponse
from os import remove
from .twitter_download import getVideo, save_file

def index(request):
    if request.method == "POST":
        website = request.POST.get('website')
        url = request.POST.get('url')

        if website == 'yt':
            resolution = request.POST.get('video')
            quality = request.POST.get('audio')

            if resolution:
                video = YouTube(url).streams.filter(resolution=resolution, progressive=True)[0]
                filename = f'{video.title}.mp4'
                video.download(output_path='videos', filename=filename)

                with open (f'videos/{filename}', 'rb') as video:
                    response = HttpResponse(video, content_type='application/vnd.mp4')
                    response['Content-Disposition'] = 'attachment; filename=' + filename
                    remove(f'videos/{filename}')
                    return response
            

            audio = YouTube(url).streams.filter(abr=quality)[0]
            filename = f'{audio.title}.mp3'
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
        if website == 'yt':  
            try:
                video = YouTube(url)
            except:
                return render(request, 'index.html', {'yt_error' : True})
            print(video.streams)

            audios = video.streams.filter(type='audio')

            context = {
                'url' : url,
                'website' : website,
                'video' : video,
                'best_video' : video.streams.get_highest_resolution(),
                'videos' : video.streams.filter(progressive=True, type='video')[::-1],
                'audios' : audios[::-1],
                'best_audio' : audios[-1]
            }

            return render(request, 'index.html', context)
    
        if website == 'ig':
            pass

        if website == 'tw':

            video = getVideo(url)
            token = video.log['guest_token']

            save_file(video.url, token)
            filename = token + '.mp4'

            with open (f'videos/{filename}', 'rb') as video:
                response = HttpResponse(video, content_type='application/vnd.mp4')
                response['Content-Disposition'] = 'attachment; filename=' + filename
                remove(f'videos/{filename}')
                return response

        if website == 'pin':
            pass

        if website == 'rd':
            pass