import os
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from picture.models import Picture
from django.http import FileResponse, Http404
from urllib.parse import quote  # 파일 이름을 URL 인코딩하기 위해
from urllib.parse import urlparse, parse_qs


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-is_pinned', '-pk')[:10]
    pictures = Picture.objects.all().order_by('-created_at', '-pk')

    videos = read_youtube_links()  # 여러 영상 링크 읽기
    form_link = read_form_link()

    return render(
        request,
        'post/index.html',
        {
            'posts': posts,
            'picture': pictures,
            'videos': videos,  # 템플릿에서는 videos 변수로 반복 처리
            'form_link': form_link
        },
    )



def posts(request):
    # 전체 게시글 목록에서도 고정글을 우선 보여주고, 그 다음 최신글 순으로 정렬
    post_list = Post.objects.all().order_by('-is_pinned', '-pk')
    paginator = Paginator(post_list, 20)  # 20 posts per page

    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
    }

    form_link = read_form_link()

    return render(
        request,
        'post/posts.html',
        {
            'posts': page_obj,
            'form_link': form_link
        }
    )


def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    form_link = read_form_link()

    return render(
        request,
        'post/postDetail.html',
        {
            'post': post,
            'form_link': form_link
        }
    )


def download_post_file(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Http404("Post does not exist")

    # 파일 경로 생성
    file_path = post.file.path
    print(file_path)

    # 파일이 존재하는지 확인
    if os.path.exists(file_path):
        # FileResponse를 사용하여 응답을 파일 다운로드로 설정
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)

        # 파일 이름 인코딩
        filename = os.path.basename(file_path)
        filename_encoded = quote(filename)  # URL 인코딩

        # 올바른 Content-Disposition 설정
        response[
            'Content-Disposition'] = f'attachment; filename="{filename_encoded}"; filename*=UTF-8\'\'{filename_encoded}'
        response['Content-Type'] = 'application/octet-stream'
        return response
    else:
        return Http404("File does not exist")


def read_youtube_links():
    video_ids = []
    with open('linkSetting/youtube.txt', 'r', encoding="utf-8") as file:
        lines = file.readlines()  # 모든 줄을 읽음
    for line in reversed(lines):  # 역순으로 순회: 최신 링크가 먼저 처리됨
        url = line.strip()
        if url:  # 빈 줄은 무시
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            video_id = query_params.get('v', [None])[0]
            if video_id:
                video_ids.append(video_id)
    return video_ids


def read_form_link():
    with open('linkSetting/form.txt', 'r', encoding="utf-8") as file:
        url = file.read().split('\n')[-1].strip()

    return url
