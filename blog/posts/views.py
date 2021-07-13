from django.http import JsonResponse, Http404
from django.shortcuts import render

from posts.assets import get_all_posts, get_template_directory


# Feel free to move this to a new file if you are carrying out the 'tags' calculation
# there
stopWords = [
    "#", "##", "a", "about", "above", "after", "again", "against", "all", "am",
    "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
    "before", "being", "below", "between", "both", "but", "by", "can't", "cannot",
    "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
    "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
    "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
    "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
    "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
    "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
    "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other",
    "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
    "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than",
    "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there",
    "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this",
    "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't",
    "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when",
    "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why",
    "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're",
    "you've", "your", "yours", "yourself", "yourselves"
]


def index(request):
    """ render the index html.

    Renders the react html, pulls js from the static directory.
    """
    return render(request, f'{get_template_directory()}/index.html')


def post(request, slug):
    """Returns the content of a post, or 404.

    If the requested slug does not exist, return 404.
    otherwise return a json object containing:
    - author
    - slug
    - title
    - content

    for the specified post. keys are lower case.
    """
    all_posts = get_all_posts()
    if slug not in all_posts.keys():
        # return 404
        raise Http404('post not found')
    return JsonResponse(all_posts[slug])


def posts(request):
    """ Returns a list of post objects, as described in `post()`.

    Scans the assets/posts/ directiory on every call and returns
    a list of post objects.
    """
    all_posts = get_all_posts()
    result_set = []
    for path, post in all_posts.items():
        del post['author']
        del post['content']
        result_set.append(post)
    return JsonResponse(result_set, safe=False)
