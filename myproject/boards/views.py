# from django.http import HttpResponse
from .models import Board, Post
from .forms import NewTopicForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
# import ipdb
# Create your views here.


def home(request):
    boards = Board.objects.all()
    # boards_names = list()

    # for board in boards:
    #     boards_names.append(board.name)

    # response_html = '<br>'.join(boards_names)

    # return HttpResponse(response_html)
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    # ipdb.set_trace()
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})


def about(request):
    # do something...
    return render(request, 'about.html')


def about_company(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            post.save()
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})
