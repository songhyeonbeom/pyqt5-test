from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Photo


@login_required(login_url='common:login')
def vote_photo(request, photo_id):
    """
    insta 사진추천등록
    """
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.user == photo.owner:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        photo.voter.add(request.user)
    return redirect('insta:photo_detail', pk=photo.id)



def detail(request, photo_id):
    """
    insta 내용 출력
    """
    photo = get_object_or_404(Photo, pk=photo_id)
    context = {'photo': photo}
    return render(request, 'insta/photo_detail.html', context)















