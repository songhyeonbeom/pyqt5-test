from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PhotoForm
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


@login_required(login_url='common:login')
def photo_modify(request, photo_id):
    """
    insta photo 수정
    """
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.user != photo.owner:
        messages.error(request, '수정권한이 없습니다')
        return redirect('insta:photo_detail', pk=photo.id)

    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.modify_date = timezone.now()  # 수정일시 저장
            photo.save()
            return redirect('insta:photo_detail', pk=photo.id)
    else:
        form = PhotoForm(instance=photo)
    context = {'form': form}
    return render(request, 'insta/photo_form.html', context)





@login_required(login_url='common:login')
def photo_delete(request, photo_id):
    """
    insta photo 댓글 삭제
    """
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.user != photo.owner:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('insta:photo_detail', pk=photo.id)
    photo.delete()
    return redirect('insta:allPhotoAB')