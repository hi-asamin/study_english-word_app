from django_filters import FilterSet, filters
from .models import word

class OriginalOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s (降順)'

class WordFilter(FilterSet):
    word = filters.CharFilter(label='英単語', lookup_expr='contains')
    part_of_speech = ChoiceFilter(choices=PART_OF_SPEECH_CHOICES)

    order_by = OriginalOrderingFilter(
        fields=(
            ('word', 'word'),
            ('part_of_speech', 'part_of_speech'),
        ),
        field_labels={
            'word': '英単語',
            'speech': '品詞',
        },
        label='並び順'
    )

    class Meta:
        model = Word
        fields = ('word', 'part_of_speech')

PART_OF_SPEECH_CHOICES = (
    (0, '名詞'),
    (1, '代名詞'),
    (2, '動詞'),
    (3, '形容詞'),
    (4, '副詞'),
    (5, '前置詞'),
    (6, '接続詞'),
    (7, '間投詞')
)
