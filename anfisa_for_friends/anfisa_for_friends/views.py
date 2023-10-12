from django.shortcuts import render


def test_rendering(request):
    template = 'catalog/block_content_rendered.html'
    context = {
        'products': [
            'Iron carrot',
            'Giant mousetrap',
            'Dehydrated boulders',
            'Invisible paint',
        ]
    }
    return render(request, template, context)
