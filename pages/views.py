# pages/views.py
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
import pickle
import pandas as pd


def homePost(request):
    # Use request object to extract choice.

    age = -999
    weight = -999
    height = -999
    ap_hi = -999
    ap_lo = -999
    smoke = -999
    active = -999

    try:
        # Extract value from request object by control name.
        selected_age = request.POST['age']
        selected_height = request.POST['height']
        selected_weight = request.POST['weight']
        selected_ap_hi = request.POST['systolic']
        selected_ap_lo = request.POST['diastolic']
        selected_smoke = request.POST['smoker']
        selected_active = request.POST['active']

        # Crude debugging effort.
        print("Posted age: " + selected_age)
        print("Posted height: " + selected_height)
        print("Posted weight: " + selected_weight)
        print("Posted ap_hi: " + selected_ap_hi)
        print("Posted ap_lo: " + selected_ap_lo)
        print("Posted smoke: " + selected_smoke)
        print("Posted active: " + selected_active)

        # Convert string to integer.
        age = int(selected_age)
        height = int(selected_height)
        weight = int(selected_weight)
        ap_hi = int(selected_ap_hi)
        ap_lo = int(selected_ap_lo)
        smoke = int(selected_smoke)
        active = int(selected_active)


    # Enters 'except' block if integer cannot be created.
    except:
        return render(request, 'home.html', {
            'errorMessage': '*** The data submitted is invalid. Please try again.'
            # 'mynumbers': [1, 2, 3, 4, 5, 6, ]
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', kwargs={'age': age, 'height': height, 'weight': weight,
                                                                'ap_hi': ap_hi, 'ap_lo': ap_lo, 'smoke': smoke, 'active': active}))


def results(request, age, height, weight, ap_hi, ap_lo, smoke, active):
    print("*** Inside results()")
    # load saved model
    model = pickle.load(open('/Users/jlee/Documents/BCIT/CST/Term-4U/Comp4949 - Big Data Analytics Methods/4949Projects/cardio-app/best_model.pkl', 'rb'))
    scaler = pickle.load(open('/Users/jlee/Documents/BCIT/CST/Term-4U/Comp4949 - Big Data Analytics Methods/4949Projects/cardio-app/best_scaler.pkl', 'rb'))

    # Create a single prediction.
    test_df = pd.DataFrame(columns=['age', 'height', 'weight', 'ap_hi', 'ap_lo', 'smoke', 'active'])
    test_df = test_df._append({'age': age, 'height': height, 'weight': weight, 'ap_hi': ap_hi, 'ap_lo': ap_lo, 'smoke': smoke, 'active': active}, ignore_index=True)
    # singleSampleDf = singleSampleDf._append({'gmat': gmat,
    #                                          'work_experience': workExperience},
    #                                         ignore_index=True)

    # Scale the data
    scaled_df = scaler.transform(test_df)

    prediction = model.predict(scaled_df)

    print("Single prediction: " + str(prediction))

    return render(request, 'results.html', {'age': age, 'height': height, 'weight': weight,
                                            'ap_hi': ap_hi, 'ap_lo': ap_lo, 'smoke': smoke, 'active': active,
                                            'prediction': prediction})


def homePageView(request):
    # return request object and specify page.
    return render(request, 'home.html', {
        'mynumbers':[1,2,3,4,5,6,],
        'firstName': 'Jason',
        'lastName': 'Lee',})


def aboutPageView(request):
    # return request object and specify page.
    return render(request, 'about.html')

