from django.http import JsonResponse

def view_question(request, question_id):
    context = {}
    try:
        question = Question.objects.get(id=question_id)
        question.views += 1
        question.save()
        context['question_id'] = question.id
        context['title'] = question.title
        context['author'] = question.author
        context['module'] = question.module.title
        context['explanation'] = question.explanation
        context['tried_what'] = question.tried_what
        context['summary'] = question.summary
        context['pub_date'] = question.pub_date
        context['status'] = question.status
        context['tags'] = list(question.tags.all())
        context['score'] = question.score
        context['views'] = question.views
        context['upvote_or_downvote'] = check_upvote_or_downvote(question)

        answer_query_result = Answer.objects.filter(question=question)
        context['answer_list'] = []
        for answer in answer_query_result:
            answer_dict = {}
            answer_dict['author'] = answer.author
            answer_dict['content'] = answer.content
            answer_dict['pub_date'] = answer.pub_date
            answer_dict['score'] = answer.score
            answer_dict['is_solution'] = answer.is_solution
            context['answer_list'].append(answer_dict)
    except Question.DoesNotExist:
        context['question_id'] = context['title'] = context['author'] = context['module'] = context['explanation'] = context['tried_what'] = context['summary'] = context['pub_date'] = context['status'] = context['score'] = context['views'] = context['upvote_or_downvote'] = "Question does not exist"
    return return JsonResponse(context)