from . import models


def get_overall_result():
    data = []
    subcategory = models.Subcategory.objects.all()
    for item in subcategory:
        scores = 0
        query = get_result_by_subcategory(item.id).all().values('scores')
        for value in query:
            scores += value['scores']
        data.append({
            'name': item.subcategory_name,
            'value': scores * 10  # percents
        })
    return data


def get_result_by_subcategory(subcategory_id, vote=1):
    choice = models.Choice.objects.filter(vote=vote) \
             & models.Choice.objects.filter(question_id__subcategory=subcategory_id)
    return choice


def reset():
    all_choice = models.Choice.objects.all()
    for choice in all_choice:
        choice.vote = False
        choice.save()
