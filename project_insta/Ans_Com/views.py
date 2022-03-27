from django.shortcuts import render, get_object_or_404, redirect

from insta.models import Photo
from django.utils import timezone




def answer_create(request, photo_id):
    """
    insta 답변등록
    """
    photo = get_object_or_404(Photo, pk=photo_id)
    photo.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('insta:photo_detail', photo_id=photo.id)














# @login_required(login_url='common:login')
# def answer_create(request, photo_id):
#     """
#     insta photo 답변등록
#     """
#     photo = get_object_or_404(Photo, pk=photo_id)
#     if request.method == "POST":
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.author = request.user  # author 속성에 로그인 계정 저장
#             answer.create_date = timezone.now()
#             answer.photo = photo
#             answer.save()
#             return redirect('{}#answer_{}'.format(
#                 resolve_url('insta:photo_detail', photo_id=photo.id), answer.id))
#
#     else:
#         form = AnswerForm()
#     context = {'photo': photo, 'form': form}
#     return render(request, 'insta/photo_detail.html', context)
#
