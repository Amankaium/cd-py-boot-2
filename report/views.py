from django.shortcuts import render, HttpResponse
from django.views import View
from .models import ReportAuto
# from .utils import make_report
from threading import Thread
from .tasks import add, make_report

# Create your views here.
class ReportView(View):
    template_name = "report/report.html"

    def get(self, request, *args, **kwargs):
        # print("Сейчас вызову celery task add")
        # add.apply_async(kwargs={'x': 6, 'y': 3})
        # print("Таск был вызван строкой выше")
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        rep = ReportAuto()
        excel_file = request.FILES["input_file"]
        rep.input_file = excel_file
        rep.save()
        # make_report(excel_file)
        # thread_object = Thread(target=make_report, args=(input_file, rep))
        # thread_object.start()
        print("Сейчас вызову celery task add")
        make_report.delay(report_object_id=rep.id)
        print("Таск был вызван строкой выше")

        return HttpResponse("Данные приняты, отчёт готовится...")
