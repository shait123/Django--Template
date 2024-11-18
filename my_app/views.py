from django.shortcuts import render

def example_view(request):
    return render(request,'my_app/example.html')

def variable_view(request):
    my_var= {
        'first_name':'Shaitan','last_name':'Singh',
        'some_list':[1,2,3],'some_dic':{'some_key':'some_value'}
    }
    return render(request,'my_app/variable.html',context=my_var)