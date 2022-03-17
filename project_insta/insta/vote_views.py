from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from .models import Photo


@login_required(login_url='common:login')
def vote_photo(request, question_id):
    """
    insta 사진추천등록
    """
    photo = get_object_or_404(Photo, pk=question_id)
    if request.user == photo.owner:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        photo.voter.add(request.user)
    return redirect('insta:detail', photo_id=photo.id)
















