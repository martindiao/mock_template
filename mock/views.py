from django.shortcuts import render
"""
All the pages' url are registered in the /mock/url.py 
"""


def test(request):
    """
    url: http://127.0.0.1:8000/test
    template for frontend develop
    mock the data for page and assign it to the required template
    """
    template = 'test.html'
    data = {
        'test_data': 23333,
        'test_data2': 23123123,
        'test_array': [1, 2, 3, 4]

    }
    return render(request, template, {'data': {
        'test_data': 23333,
        'test_data2': 23123123,
        'test_array': [1, 2, 3, 4]

    }})


def index(request):
    """
    url: http://127.0.0.1:8000/
    """
    return latest_reviews(request)


def latest_reviews(request):
    """

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    reviews_paged = Review.query.order_by(Review.id.desc()).paginate(page=page, per_page=per_page)
    return render_template('latest-reviews.html', reviews=reviews_paged, title='全站最新点评', this_module='home.latest_reviews')
    tips: this.module 是标记当前模版名称的, flask相关用法
    """
    reviews_paged = {
        'total': 234,
        'page': 233333,
        'items': [{
            'author': {'avatar': '我也不知道这个是什么', 'username': 'test_username', 'id': 23333333},
            'course': {'id': 23333, 'name': 'test_name', 'teacher_names_display': 'HammerWang', 'teachers': True},
            'publish_time': 20181012,
            'content': 'test_content',
            'id': 23333
        }],
        'has_prev': True,
        'is_hidden': False,
        'prev_num': 23123,
        'has_next': True
    }
    template = 'ustc_templates/latest-reviews.html'
    data = {
        'reviews': reviews_paged,
        'title': '全站最新点评',
        'this_module': 'home.latest_reviews'

    }
    return render(request, template, data)
