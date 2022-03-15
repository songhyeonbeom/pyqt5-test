from django.shortcuts import render

from django.views.generic import ListView, DetailView
from photo.models import Album, Photo
from django.views.generic import CreateView, UpdateView, DeleteView

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from photo.forms import PhotoInlineFormSet
from config.views import OwnerOnlyMixin


from django.shortcuts import render, get_object_or_404
from .models import Album, Photo
from django.core.paginator import Paginator, EmptyPage, InvalidPage














class AlbumLV(ListView):
    model = Album


class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo


class PhotoCV(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ('album', 'title', 'image', 'description')
    success_url = reverse_lazy('photo:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PhotoChangeLV(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photo/photo_change_list.html'
    #매니져가 지정이 안되면 object_list

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)


class PhotoUV(OwnerOnlyMixin, UpdateView):
    model = Photo
    fields = ('album', 'title', 'image', 'description')
    success_url = reverse_lazy('photo:index')


class PhotoDelV(OwnerOnlyMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:index')


class AlbumPhotoCV(LoginRequiredMixin, CreateView):
    model = Album
    fields = ('name', 'description')
    success_url = reverse_lazy('photo:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


#--- Change-list/Delete for Album
class AlbumChangeLV(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'photo/album_change_list.html'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)


class AlbumPhotoUV(OwnerOnlyMixin, UpdateView):
    model = Album
    fields = ('name', 'description')
    success_url = reverse_lazy('photo:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class AlbumDelV(OwnerOnlyMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('photo:index')










# Create your views here.
def allPhotoAB(request, c_slug=None):
    c_page = None;
    photos_list = None;
    if c_slug != None:
        c_page = get_object_or_404(Album, slug=c_slug)
        photos_list = Photo.objects.filter(Album=c_page)
    else:
        photos_list = Photo.objects.all()

    paginator = Paginator(photos_list, 6)
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1

    try:
        photos = paginator.page(page)
    except(EmptyPage, InvalidPage):
        photos = paginator.page(paginator.num_pages)

    return render(request, 'photo/album.html', {'album': c_page, 'photos': photos})


def PhotoABDetail(request, c_slug, photo_slug):
    try:
        photo = Photo.objects.get(Album__slug = c_slug, slug = photo_slug)
    except Exception as e :
        raise e

    return render(request, 'photo/photo.html', {'photo' : photo})