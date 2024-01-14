from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Questionlist, Chathistory
from difflib import get_close_matches
from .serializers import chatmessage
from django.http import JsonResponse
# Create your views here.

def loadQuestionlist():
    qlist = Questionlist.objects.get(id=1)
    qlist = (qlist.question).split('|')
    for x in qlist:
        if x == '':
            qlist.remove(x)

    return qlist


def findIdofQuestion(Question):
    questionlist = loadQuestionlist()
    print("questionlist",questionlist)
    match = get_close_matches(Question, questionlist, n=1, cutoff=0.6)
    print("match",match)
    if match:
        return{'status':True, 'match':match[0]}
    
    else:
        return {'status':False,}


class bot(APIView):
    def get(self, request, Question, format=None):
        if Question is not None:
            result = findIdofQuestion(Question)
            print("result get", Question)
            print("result get", result)
            if result['status']:
                answer = Chathistory.objects.get(question=result['match']).answer
                return Response({'Question':Question, 'reply':answer}, status=status.HTTP_201_CREATED)
            if not result['status']:
                answer="sorry I don't have Solution for your Quetestion\n can you please teach me\n please find a link to teach me"
                link = f"192.168.1.5:8000/bot/{Question}"
                return Response({'Question':Question, 'reply':answer, 'link':link}, status=status.HTTP_201_CREATED)
            

    def post(self, request, Question, format=None):
        if Question is not None:
            result = findIdofQuestion(Question)
            print("result post", result)
            if not result['status']:
                qlist = Questionlist.objects.get(id=1)
                qlist.question=f"{qlist.question}|{Question.lower()}"
                qlist.save()
                answer=(request.data)['answer']
                Chathistory.objects.create(
                    question=Question.lower(),
                    answer=answer.lower()
                )
            return Response({'Question':Question, 'answer':answer, 'questionlist':questionlist}, status=status.HTTP_201_CREATED)

        

