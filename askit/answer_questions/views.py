import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from home_page.models import Question, Answer, Tag, Module, Comment, Notification, Activity
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


def check_upvote_or_downvote_question(question, user):
    print(question.upvotes.filter(id=user.id))
    if question.upvotes.filter(id=user.id).exists():
        return "upvote"
    elif question.downvotes.filter(id=user.id).exists():
        return "downvote"
    else:
        return "none"


def check_upvote_or_downvote_answer(answer, user):
    if answer.upvotes.filter(id=user.id).exists():
        return "upvote"
    elif answer.downvotes.filter(id=user.id).exists():
        return "downvote"
    else:
        return "none"


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_question(request, question_id):
    context = {}
    try:
        question = Question.objects.get(id=question_id)
        question.views += 1
        question.save()
        context['question_id'] = question.id
        context['title'] = question.title
        context['author'] = getattr(question.author, 'username', 'Anonymous')
        context['module'] = question.module.title
        context['explanation'] = question.explanation
        context['tried_what'] = question.tried_what
        context['summary'] = question.summary
        context['pub_date'] = question.pub_date
        context['status'] = question.status
        context['tags'] = []
        for x in question.tags.all():
            context['tags'].append(str(x))
        context['score'] = question.score
        context['views'] = question.views
        context['upvote_or_downvote'] = check_upvote_or_downvote_question(question, request.user)

        Comment_query_result = Comment.objects.filter(question=question)
        context['comment_list'] = []
        for comment in Comment_query_result:
            comment_dict = {}
            comment_dict['id'] = comment.id
            comment_dict['author'] = getattr(comment.author, 'username', 'Anonymous')
            comment_dict['content'] = comment.content
            comment_dict['pub_date'] = comment.pub_date
            context['comment_list'].append(comment_dict)

        answer_query_result = Answer.objects.filter(question=question)
        context['answer_list'] = []
        for answer in answer_query_result:
            answer_dict = {}
            answer_dict['id'] = answer.id
            answer_dict['author'] = getattr(answer.author, 'username', 'Anonymous')
            answer_dict['content'] = answer.content
            answer_dict['pub_date'] = answer.pub_date
            answer_dict['score'] = answer.score
            answer_dict['is_solution'] = answer.is_solution
            answer_dict['from_admin'] = answer.from_admin
            answer_dict['upvote_or_downvote'] = check_upvote_or_downvote_answer(answer, request.user)
            context['answer_list'].append(answer_dict)
    except Question.DoesNotExist:
        context['question_id'] = context['title'] = context['author'] = context['module'] = context['explanation'] = \
            context['tried_what'] = context['summary'] = context['pub_date'] = context['status'] = context['score'] = \
            context['views'] = context['upvote_or_downvote'] = "Question does not exist"
    return JsonResponse(context)


def set_up_test_database(request):
    return HttpResponse("Databae reset is no longer supported.")

    # Module.objects.all().delete()
    # Question.objects.all().delete()
    # Tag.objects.all().delete()
    # Answer.objects.all().delete()
    # Comment.objects.all().delete()
    # Notification.objects.all().delete()
    # Activity.objects.all().delete()
    #
    # sn = Module(title="SN", description="Security and Networking")
    # sn.save()
    # ai2 = Module(title="AI2", description="Artificial Intelligence 2")
    # ai2.save()
    # tp = Module(title="TP", description="Team Project")
    # tp.save()
    # misc = Module(title="Misc", description="Miscellaneous")
    # misc.save()
    #
    # sn_q1 = Question(title="What are the best practices for securing a wireless network in a university environment?",
    #                  module=sn,
    #                  explanation="As universities rely heavily on wireless networks to support their academic and administrative activities, ensuring the security of these networks is crucial. With the rise of cyber threats such as hacking, phishing, and malware attacks, it is important to understand the best practices for securing a wireless network in a university environment. This question seeks to explore the different strategies and tools that can be used to enhance the security of wireless networks, as well as the challenges that may arise in implementing these measures.",
    #                  tried_what="I already conducted some research on the topic and has looked into various resources such as online forums, white papers, and academic articles. I also spoken to some IT professionals at their university but is still seeking a broader perspective on the issue.",
    #                  summary="This question asks about the best practices for securing a wireless network in a university environment. The author has conducted some research on the topic but is seeking a broader perspective on the issue. The question seeks to explore the different strategies and tools that can be used to enhance the security of wireless networks, as well as the challenges that may arise in implementing these measures.",
    #                  score=13)
    # sn_q1.save()
    # sn_q1.tags.add(Tag.objects.get_or_create(tag_name="Security")[0])
    # sn_q1.tags.add(Tag.objects.get_or_create(tag_name="Wireless")[0])
    # sn_q1.tags.add(Tag.objects.get_or_create(tag_name="Network")[0])
    # sn_q1.tags.add(Tag.objects.get_or_create(tag_name="University")[0])
    #
    # sn_q1_a1 = Answer(question=sn_q1,
    #                   content="Securing a wireless network in a university environment is a complex task that requires a comprehensive approach. There are various strategies and tools that can be used to enhance the security of wireless networks, but implementing them can be challenging due to factors such as the size and complexity of the network, the diversity of devices and users, and the need to balance security with usability and accessibility.\nOne of the best practices for securing a wireless network is to use strong encryption and authentication protocols, such as WPA2-Enterprise or 802.1X, which can protect against unauthorized access and eavesdropping. It is also important to use strong and unique passwords for network devices and accounts, and to regularly update them to prevent brute-force attacks and password cracking.\nAnother best practice is to segment the network into different zones or subnets, with different access policies and security controls based on the sensitivity and criticality of the data and services. For example, a university may have separate subnets for student dormitories, academic departments, administrative offices, and research labs, each with its own access control lists, firewalls, and intrusion detection systems.\nIn addition, it is important to monitor the network for suspicious activity and to have incident response plans in place to quickly detect, isolate, and mitigate security breaches. This can involve using network monitoring tools, security information and event management (SIEM) systems, and security analytics to detect anomalies and potential threats in real-time.\nFinally, educating users about good security practices and raising awareness of the risks and consequences of security breaches can also be effective in enhancing the overall security posture of the wireless network. This can involve providing training and awareness campaigns on topics such as password hygiene, social engineering, phishing, and malware prevention.\nOverall, securing a wireless network in a university environment requires a multi-layered approach that combines technical controls, network segmentation, monitoring and incident response, and user education and awareness. By following best practices and staying vigilant, universities can reduce the risk of security breaches and protect their critical data and services from cyber threats.")
    # sn_q1_a1.save()
    #
    # sn_q2 = Question(title="What are the key differences between public and private IP addresses?",
    #                  module=sn,
    #                  explanation="IP addresses are unique numerical identifiers that are used to identify devices on a network. In general, IP addresses can be classified as either public or private, depending on their scope and accessibility. This question seeks to explore the key differences between public and private IP addresses, as well as the advantages and disadvantages of each type.",
    #                  tried_what="The author has done some basic research on the topic, but is looking for a more comprehensive explanation of the differences between public and private IP addresses.",
    #                  summary="This question asks about the key differences between public and private IP addresses, and their respective advantages and disadvantages. The author has done some preliminary research on the topic but is seeking a more comprehensive explanation.")
    # sn_q2.save()
    # sn_q2.tags.add(Tag.objects.get_or_create(tag_name="IP")[0])
    # sn_q2.tags.add(Tag.objects.get_or_create(tag_name="Address")[0])
    # sn_q2.tags.add(Tag.objects.get_or_create(tag_name="Public")[0])
    # sn_q2.tags.add(Tag.objects.get_or_create(tag_name="Private")[0])
    #
    # sn_q2_a1 = Answer(question=sn_q2,
    #                   content="Public IP addresses are globally unique and accessible from the Internet, while private IP addresses are only accessible within a private network and are not globally unique. Public IP addresses are typically used for servers and devices that need to be accessible from the Internet, while private IP addresses are used for internal devices such as computers, printers, and routers. Public IP addresses are assigned by the Internet Assigned Numbers Authority (IANA) or Internet Service Providers (ISPs), while private IP addresses are assigned by the network administrator according to the standards defined by the Internet Engineering Task Force (IETF).")
    # sn_q2_a1.save()
    #
    # ai2_q1 = Question(title="What is the difference between supervised and unsupervised learning in deep learning?",
    #                   module=ai2,
    #                   explanation="Deep learning is a subfield of machine learning that is inspired by the structure and function of the human brain. In deep learning, neural networks are used to learn from large amounts of data and make predictions or decisions based on that learning. Supervised and unsupervised learning are two of the most common types of learning in deep learning. This question seeks to explore the key differences between supervised and unsupervised learning in deep learning, as well as the advantages and disadvantages of each approach.",
    #                   tried_what="The author has done some preliminary research on the topic, but is looking for a more in-depth explanation of the differences between supervised and unsupervised learning in deep learning.",
    #                   summary="This question asks about the key differences between supervised and unsupervised learning in deep learning, and their respective advantages and disadvantages. The author has done some preliminary research on the topic but is seeking a more comprehensive explanation.")
    # ai2_q1.save()
    # ai2_q1.tags.add(Tag.objects.get_or_create(tag_name="Deep Learning")[0])
    # ai2_q1.tags.add(Tag.objects.get_or_create(tag_name="Supervised Learning")[0])
    # ai2_q1.tags.add(Tag.objects.get_or_create(tag_name="Unsupervised Learning")[0])
    #
    # ai2_q1_a1 = Answer(question=ai2_q1,
    #                    content="Supervised learning is a type of learning where the input data is labeled with corresponding output values, and the neural network learns to map inputs to outputs by minimizing the difference between predicted and actual outputs. In contrast, unsupervised learning is a type of learning where the input data is not labeled, and the neural network learns to identify patterns and structures in the data by clustering or dimensionality reduction. Supervised learning is often used for tasks such as classification, regression, and object detection, while unsupervised learning is often used for tasks such as clustering, anomaly detection, and feature extraction.")
    # ai2_q1_a1.save()
    #
    # prob_q1 = Question(title="What is the difference between probability and statistics?",
    #                    module=ai2,
    #                    explanation="Probability and statistics are two closely related fields of mathematics that deal with analyzing and understanding random events. While there is some overlap between the two fields, they have different goals and methods. This question seeks to explore the key differences between probability and statistics, as well as their relationship and applications.",
    #                    tried_what="The author has a basic understanding of both probability and statistics, but is looking for a more in-depth explanation of their differences.",
    #                    summary="This question asks about the differences between probability and statistics, and their relationship and applications.")
    # prob_q1.save()
    # prob_q1.tags.add(Tag.objects.get_or_create(tag_name="Probability")[0])
    # prob_q1.tags.add(Tag.objects.get_or_create(tag_name="Statistics")[0])
    #
    # prob_q1_a1 = Answer(question=prob_q1,
    #                     content="Probability is concerned with measuring the likelihood of an event occurring, based on some underlying model or assumptions. Statistics, on the other hand, is concerned with analyzing and interpreting data that has been generated by random processes, in order to draw conclusions or make predictions about the underlying system. In other words, probability deals with predicting the likelihood of future events, while statistics deals with analyzing past events and drawing conclusions about the underlying process. While the two fields are closely related, probability is more theoretical and concerned with the underlying mathematical models, while statistics is more applied and concerned with real-world data analysis and interpretation.")
    # prob_q1_a1.save()
    #
    # return HttpResponse("The database has been reset, visit https://askit.bham.team to go back to the home page")


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def submit_answer(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(id=question_id)
        post_data = json.loads(request.body)
        content = post_data['content']
        author = request.user
        answer = Answer(question=question, content=content, author=author,
                        from_admin=(request.user.is_superuser or request.user in question.module.admins.all()))
        answer.save()
        notification = Notification(receiver=question.author,
                                    detail=f"{author.username} has answered your question '{question.title}'"[:500],
                                    link="/question/" + str(question.id))
        notification.save()
        activity = Activity(author=author, action=f"answered question '{question.title}'"[0:200],
                            link="/question/" + str(question.id))
        activity.save()
        answer_dict = {'id': answer.id,
                       'author': getattr(answer.author, 'username', 'Anonymous'),
                       'content': answer.content,
                       'pub_date': answer.pub_date,
                       'score': answer.score,
                       'is_solution': answer.is_solution}
        return JsonResponse(answer_dict)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def submit_comment(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(id=question_id)
        post_data = json.loads(request.body)
        content = post_data['content']
        author = request.user
        comment = Comment(question=question, content=content, author=author)
        comment.save()
        notification = Notification(receiver=question.author,
                                    detail=f"{author.username} has commented on your question '{question.title}'"[:500],
                                    link="/question/" + str(question.id))
        notification.save()
        activity = Activity(author=author, action=f"commented on question '{question.title}'"[0:200],
                            link="/question/" + str(question.id))
        activity.save()
        comment_dict = {'id': comment.id,
                        'author': getattr(comment.author, 'username', 'Anonymous'),
                        'content': comment.content,
                        'pub_date': comment.pub_date}
        return JsonResponse(comment_dict)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def delete_comment(request, question_id, com_id):
    if request.method == 'DELETE':
        # post_data = json.loads(request.body)
        # comment_id = post_data['comment_id']
        comment = Comment.objects.get(id=com_id)
        if request.user == comment.author:
            comment.delete()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": "You are not the author of this comment"})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def upvote_question(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(id=question_id)
        # check if user has already upvoted or downvoted
        if question.upvotes.filter(id=request.user.id).exists():
            return JsonResponse(
                {"success": False, "score": question.score, "error": "You have already upvoted this question"})
        if question.downvotes.filter(id=request.user.id).exists():
            # remove from downvotes and increase score
            question.downvotes.remove(request.user)
            question.score += 1
        # add to upvotes and increase score
        question.upvotes.add(request.user)
        question.score += 1
        question.save()
        return JsonResponse({"success": True, "score": question.score})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def downvote_question(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(id=question_id)
        # check if user has already upvoted or downvoted
        if question.downvotes.filter(id=request.user.id).exists():
            return JsonResponse(
                {"success": False, "score": question.score, "error": "You have already downvoted this question"})
        if question.upvotes.filter(id=request.user.id).exists():
            # remove from upvotes and decrease score
            question.upvotes.remove(request.user)
            question.score -= 1
        # add to downvotes and decrease score
        question.downvotes.add(request.user)
        question.score -= 1
        question.save()
        return JsonResponse({"success": True, "score": question.score})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def upvote_answer(request, question_id, answer_id):
    if request.method == 'POST':
        answer = Answer.objects.get(id=answer_id)
        # check if user has already upvoted or downvoted
        if answer.upvotes.filter(id=request.user.id).exists():
            return JsonResponse(
                {"success": False, "score": answer.score, "error": "You have already upvoted this answer"})
        if answer.downvotes.filter(id=request.user.id).exists():
            # remove from downvotes and increase score
            answer.downvotes.remove(request.user)
            answer.score += 1
        # add to upvotes and increase score
        answer.upvotes.add(request.user)
        answer.score += 1
        answer.save()
        return JsonResponse({"success": True, "score": answer.score})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def downvote_answer(request, question_id, answer_id):
    if request.method == 'POST':
        answer = Answer.objects.get(id=answer_id)
        # check if user has already upvoted or downvoted
        if answer.downvotes.filter(id=request.user.id).exists():
            return JsonResponse(
                {"success": False, "score": answer.score, "error": "You have already downvoted this answer"})
        if answer.upvotes.filter(id=request.user.id).exists():
            # remove from upvotes and decrease score
            answer.upvotes.remove(request.user)
            answer.score -= 1
        # add to downvotes and decrease score
        answer.downvotes.add(request.user)
        answer.score -= 1
        answer.save()
        return JsonResponse({"success": True, "score": answer.score})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def accept_answer(request, question_id, answer_id):
    if request.method == 'POST':
        answer = Answer.objects.get(id=answer_id)
        question = answer.question
        if request.user == question.author:
            answer.is_solution = True
            answer.save()
            return JsonResponse({"success": True, "accepted_answer": answer.id})
        else:
            return JsonResponse({"success": False, "error": "You are not the author of this question"})


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def delete_question(request, question_id):
    if request.method == 'DELETE':
        question = Question.objects.get(id=question_id)
        module_title = question.module.title
        if request.user == question.author:
            question.delete()
            return JsonResponse({"success": True, 'module': module_title})
        else:
            return JsonResponse({"success": False, "error": "You are not the author of this question"})


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def delete_answer(request, question_id, answer_id):
    if request.method == 'DELETE':
        answer = Answer.objects.get(id=answer_id)
        if request.user == answer.author:
            answer.delete()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": "You are not the author of this answer"})
