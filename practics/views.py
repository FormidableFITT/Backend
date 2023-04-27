from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import CommentForm
from .models import Comments

class CommentView(FormView):
    template_name = 'index.html'
    form_class = CommentForm
    success_url = reverse_lazy('comment')

    def form_valid(self, form):
        comment = Comments.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            text=form.cleaned_data['text']
        )
        comment.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comments.objects.all().order_by('-id')
        context['comments'] = comments
        return context



def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment')
    else:
        form = CommentForm()

    comments = Comments.objects.all().order_by('-id')[:10]

    context = {
        'form': form,
        'comments': comments
    }
    return render(request, 'index.html', context)
