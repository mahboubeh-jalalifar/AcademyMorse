from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import pytz # type: ignore
def Iran_time(request):
    Iran_timezone= pytz.timezone("Asia/Tehran")
    now=datetime.now (Iran_timezone)
    current_time=now.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse (f"Today is: {current_time}")