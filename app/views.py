# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from models import Competition, Club, Major, OurStory

# Create your views here.

def testingClub(request):
    clubs = Club.objects.all()
    length = len(clubs)
    type = clubs[0].get_type
    if (length == 1):
        final = 'app/1.html'
    elif (length == 2):
        final = 'app/2.html'
    elif (length == 3):
        final = 'app/3.html'
    elif (length == 4):
        final = 'app/4.html'
    elif (length == 5):
        final = 'app/5.html'
    elif (length == 8):
        final = 'app/8.html'
    
    return render(request, final, {'units':clubs, 'type':type})

def testingCompetition(request):
    competitions = Competition.objects.all()
    length = len(competitions)
    type = competitions[0].get_type
    if (length == 1):
        final = 'app/1.html'
    elif (length == 2):
        final = 'app/2.html'
    elif (length == 3):
        final = 'app/3.html'
    elif (length == 4):
        final = 'app/4.html'
    elif (length == 5):
        final = 'app/5.html'
    elif (length == 8):
        final = 'app/8.html'
  
    return render(request, final, {'units':competitions, 'type':type})

def testingMajor(request):
    majors = Major.objects.all()
    length = len(majors)
    type = majors[0].get_type
    if (length == 1):
        final = 'app/1.html'
    elif (length == 2):
        final = 'app/2.html'
    elif (length == 3):
        final = 'app/3.html'
    elif (length == 4):
        final = 'app/4.html'
    elif (length == 5):
        final = 'app/5.html'
    elif (length == 8):
        final = 'app/8.html'
   
    return render(request, final, {'units':majors, 'type':type})

def index(request):
    return render(request, 'app/index.html', {})

def home(request):
    all = OurStory.objects.all()
    our_story = all[0]
    return render(request, 'app/home.html', {'our_story':our_story})

def competition_individual(request,pk):
    competition = get_object_or_404(Competition, pk=pk)
    tempURL = competition.url
    test = list(tempURL)
    check = 0
    index = 0
    embed = ['e','m','b','e','d', '/']
    for a in test:
        if a == "/" and check == 2:
            for e in embed:
                test.insert((index + 1), e)
                index += 1
            newCheck=0
            for rem in range(0,8):
                newCheck = index+1
                del test[newCheck]
                newCheck += 1
            break;
        elif a == "/":
            check += 1
            index += 1
        else:
            index += 1

    competition.url = "".join(test)
    return render(request, 'app/competition_individual.html', {'competition':competition})

def club_individual(request,pk):
    club = get_object_or_404(Club, pk=pk)
    tempURL = club.url
    test = list(tempURL)
    check = 0
    index = 0
    embed = ['e','m','b','e','d', '/']
    for a in test:
        if a == "/" and check == 2:
            for e in embed:
                test.insert((index + 1), e)
                index += 1
            newCheck=0
            for rem in range(0,8):
                newCheck = index+1
                del test[newCheck]
                newCheck += 1
            break;
        elif a == "/":
            check += 1
            index += 1
        else:
            index += 1

    club.url = "".join(test)
    return render(request, 'app/club_individual.html', {'club':club})

def major_individual(request,pk):
    major = get_object_or_404(Major, pk=pk)
    tempURL = major.url
    test = list(tempURL)
    check = 0
    index = 0
    embed = ['e','m','b','e','d', '/']
    for a in test:
        if a == "/" and check == 2:
            for e in embed:
                test.insert((index + 1), e)
                index += 1
            newCheck=0
            for rem in range(0,8):
                newCheck = index+1
                del test[newCheck]
                newCheck += 1
            break;
        elif a == "/":
            check += 1
            index += 1
        else:
            index += 1

    major.url = "".join(test)
    return render(request, 'app/major_individual.html', {'major':major})

def our_story(request):
    our_story = OurStory.objects.get(pk=1)
    tempURL = our_story.url
    
    test = list(tempURL)
   
    check = 0
    index = 0
    embed = ['e','m','b','e','d', '/']
    for a in test:
        if a == "/" and check == 2:
            for e in embed:
                test.insert((index + 1), e)
                index += 1
            newCheck=0
            for rem in range(0,8):
                newCheck = index+1
                del test[newCheck]
                newCheck += 1
            break;
        elif a == "/":
            check += 1
            index += 1
        else:
            index += 1
    final = "".join(test)
    our_story.url = final
    
    
    return render(request, 'app/our_story.html', {'our_story':our_story})
