from django.shortcuts import render

# Create your views here.
@csrf_exempt
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def userInfo(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        userName = post_data['username']
        first_name = post_data['first_name']
        last_name = post_data['last_name']
        user = User.objects.get(username=userName)
        profile = UserProfile.objects.create(user=user,first_name=first_name,last_name=last_name)
        profile.save()
        return JsonResponse({"success": True})
