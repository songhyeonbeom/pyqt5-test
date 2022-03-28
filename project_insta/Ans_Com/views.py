from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from insta.models import Photo
from .models import Answer

from .forms import AnswerForm
from django.contrib.auth.decorators import login_required, resolve_url









@login_required(login_url='common:login')
def answer_create(request, photo_id):
    """
    insta photo 답변등록
    """
    photo = get_object_or_404(Photo, pk=photo_id)
    answer_list = None
    if request.method == "POST":

        form = AnswerForm(request.POST)
        if form.is_valid():


            answer = form.save(commit=False)
            answer.owner = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.photo = photo
            answer.save()

            return redirect('{}#answer_{}'.format(
                resolve_url('insta:photo_detail', pk=photo.id), answer.id))

    else:
        form = AnswerForm()

    context = {'photo': photo, 'form': form}
    return render(request, 'insta/photo_detail.html', context)
