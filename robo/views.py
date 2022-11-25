from django.shortcuts import render, redirect
from django.http import HttpResponse

# from gmail import sendingMessage

# sendingMessage("nikhil24min@gmail.com","subject","message")
#this function will send sms to the given email id from your Gmail account.
import pyrebase
 
config={
    "apiKey": "AIzaSyAkE3sw-DiuhnRAVWaU4qvw95DEnxTKHiM",
    "authDomain": "mcarr-c57c1.firebaseapp.com",
    "databaseURL": "https://mcarr-c57c1-default-rtdb.firebaseio.com",
    "projectId": "mcarr-c57c1",
    "storageBucket": "mcarr-c57c1.appspot.com",
    "messagingSenderId": "976355410045",
    "appId": "1:976355410045:web:4e871f13b24d08e232b114",
    "measurementId": "G-RKWVWE53XC"
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

# View to render the index page before login
def index(request):

    # get status of the receptionist
    temp = database.child('RRstatus').get().val()
    tempstatus = dict(temp)
    print(tempstatus)
    context = {"tempstatus":tempstatus}
    return render(request,'index.html', context)


# ------------ list feedbacks view
def feedback_list_func(request):
    
    data = database.child('Feedbacks').shallow().get().val()
    print(data)

    feedlist = []
    for each in data:
        feedlist.append(each)

    feeds = []
    for each in feedlist:
        print("-----------")
        print(database.child('Feedbacks').child(each).get())
        print(database.child('Feedbacks').child(each).get().val())
        print(database.child('Feedbacks').child(each).child('datetime').get().val())

        temp = dict(database.child('Feedbacks').child(each).get().val())
        print(temp)

        temp["id"]=each
        # feeds[each]=temp
        feeds.append(temp)

    # feeds = data.child()

    print(feeds)

    context = {"feedlist":feedlist,"feeds":feeds}
    return render(request, 'feedbacks.html', context)


# ----------------- interactions list
def interactions_list_func(request):

    data = database.child('Interactions').shallow().get().val()
    templist = []
    inters = []

    for each in data:
        templist.append(each)

    for each in templist:
        temp = dict(database.child('Interactions').child(each).get().val())
        inters.append(temp)
        print(temp)

    context = {'inters':inters}
    return render(request, 'interactions.html', context)