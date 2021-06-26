from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Student
from .filters import StudentFilter
from django.contrib.auth.mixins import LoginRequiredMixin
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


class StudentListView(ListView):
    model = Student
    template_name = 'studentInformationSystem/index.html'
    queryset = model.objects.all()
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = StudentFilter(self.request.GET, queryset=self.get_queryset())
        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'studentInformationSystem/student_form.html'
    model = Student
    fields = ['studentID', 'firstname', 'lastname', 'gender', 'email', 'grade', 'house', 'birthday', 'country', 'motherTongue', 'religion', 'guardian', 'guardianContactNumber', 'relationship', 'guardianEmail', 'owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StudentDetailView(DetailView):
    template_name = 'studentInformationSystem/student_detail.html'
    model = Student


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'studentInformationSystem/student_form.html'
    model = Student
    fields = ['firstname', 'lastname', 'gender', 'studentID', 'email', 'grade', 'house', 'birthday', 'gender',
              'country', 'motherTongue', 'religion', 'guardian', 'guardianContactNumber',
              'relationship', 'guardianEmail']


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = '/'


def generate_report(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')