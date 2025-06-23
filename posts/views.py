from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Post
from .validators import dates_validator, parse_date_safe

class PostListView(ListView):
    model = Post
    template_name = 'posts/feed.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        queryset = Post.objects.all()
        self.invalid_date_range = False

        sort_by = self.request.GET.get('sort', '-date_posted')
        allowed_fields = ['date_posted', '-date_posted', 'title', '-title', 'author']

        if sort_by not in allowed_fields:
            sort_by = '-date_posted'

        search_query = self.request.GET.get('q','')[:100]
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query) |
                Q(author__icontains=search_query)
            ).distinct()

        date_from_raw = self.request.GET.get('date_from')
        date_to_raw = self.request.GET.get('date_to')
        date_from = parse_date_safe(date_from_raw)
        date_to = parse_date_safe(date_to_raw)

        if (date_from_raw or date_to_raw) and dates_validator(date_from, date_to):
            print("detected invalid date")
            self.invalid_date_range = True
            return queryset.order_by(sort_by)

        if date_from:
            queryset = queryset.filter(date_posted__gte=date_from)
        if date_to:
            queryset = queryset.filter(date_posted__lte=date_to)


        return queryset.order_by(sort_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['current_sort'] = self.request.GET.get('sort', '-date_posted')
        context['search_query'] = self.request.GET.get('q', '')
        context['date_from'] = self.request.GET.get('date_from','')
        context['date_to'] = self.request.GET.get('date_to','')
        context['invalid_date_range'] = getattr(self, 'invalid_date_range', False)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/single_post.html'
    context_object_name = 'post'

