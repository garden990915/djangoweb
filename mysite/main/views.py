from django.shortcuts import redirect, render
from .models import *


# Create your views here.
def index(request):
    # templates 폴더 안에 있는 폴더 및 html파일의 경로를 설정
    return render(request, 'main/index.html')


def notice_list(request):
    noticelist = Notice.objects.all()
    return render(request, 'main/notice_list.html', {'noticeList':noticelist})

def notice_view(request,pk):
    noticeview = Notice.objects.get(pk=pk)
    return render(request, 'main/notice_view.html', {'notice':noticeview})

def notice_add(request):
    if request.method == 'POST':
        new_notice = Notice.objects.create(
            title = request.POST['title'],
            contents = request.POST['contents'],
            views = 0
        )
        return redirect('/notice/')
    return render(request, 'main/notice_add.html')

def notice_remove(request, pk):
    # 데이터베이스에서 post에 저장된 행을 삭제
    if request.method == 'POST':
        notice = Notice.objects.get(pk=pk)
        notice.delete()
    # 목록 페이지 실행
    return redirect('/notice/')
    # get방식의 경우

def notice_program(request):
    programList = Program.objects.all()
    return render(request, 'main/program.html', {'programList':programList})