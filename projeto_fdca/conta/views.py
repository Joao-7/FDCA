from django.shortcuts import render

def login_view(request):
    return render(request, "conta/login.html")

from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        matricula = request.POST.get("matricula", "")
        # PROVISÓRIO: matrícula que começa com "P" vai para professor, qualquer outra para aluno
        if matricula.upper().startswith("P"):
            return redirect("grade_professor")
        return redirect("grade_aluno")
    return render(request, "conta/login.html")