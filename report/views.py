from django.shortcuts import render, HttpResponse
from django.views import View
from .models import ReportAuto
from .utils import make_report
from threading import Thread

# Create your views here.
class ReportView(View):
    template_name = "report/report.html"

    def get(self, request, *agrs, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        rep = ReportAuto()
        excel_file = request.FILES["input_file"]
        rep.input_file = excel_file
        rep.save()
        input_file = rep.input_file
        # make_report(excel_file)
        thread_object = Thread(target=make_report, args=(input_file, rep))
        thread_object.start()

        return HttpResponse("Данные приняты, отчёт готовится...")
