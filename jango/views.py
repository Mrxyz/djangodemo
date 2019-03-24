from django.shortcuts import render
from django.http import HttpResponse
import time
import face_api
from Video_Analysis_server.Face_Reco import recognition

def index(request):  # request参数包含用户请求的信息，不管是否使用，必须有
    method = request.method  # 判断请求方式 GET POST PUT
    if method == 'POST':  # 判断是否是POST请求
        if request.POST.get('path'):  # 判断该POST请求是否有path这个参数
            faceinfo = face_api.getFaceInfo('http://gb.cri.cn/mmsource/images/2005/07/20/el050720045.jpg')
            return HttpResponse(faceinfo)
             # return HttpResponse(u'请求的是url')
        else:
            img = request.FILES.get('file')  # 获取用户上传的文件
            if not img:
                return HttpResponse(u'上传失败')
            path = 'static/faceimg/%s.jpg' %time.time()
            with open('jango/' + path, 'wb') as fn:  # w=写字符串 wb=写文件
                fn.write(img.read())
            faceinfo = recognition.recognition(path)
            return HttpResponse(faceinfo)
            # return render(request, 'face.html', context={'imgurl': path}) #+ HttpResponse(faceinfo)
    else:
        return render(request, 'face.html', context={'imgurl': 'http://gb.cri.cn/mmsource/images/2005/07/20/el050720045.jpg'})