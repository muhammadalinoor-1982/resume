from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import os

# Noor Dashboard.
def dashboard(request):
    pers = Personal.objects.all()
    we = Work_Experience.objects.all()
    edu = Education.objects.all()
    pt = Training.objects.all()
    skl = Skills.objects.all()
    port = Portfolio.objects.all()
    plat = Platform.objects.all()
    lang = Language.objects.all()
    ref = Reference.objects.all()
    return render(request, 'dashboard/dashboard.html', locals())

# Personal Information
def personal(request):
    pers = Personal.objects.all()
    return render(request, 'personal/personal.html', locals())

def pers_create(request):
    if request.method == 'POST':
        name        =request.POST.get('name')
        email       =request.POST.get('email')
        phone       =request.POST.get('phone')
        address     =request.POST.get('address')
        github      =request.POST.get('github')
        linkedin    =request.POST.get('linkedin')
        instagram   =request.POST.get('instagram')
        facebook    =request.POST.get('facebook')
        tag_line    =request.POST.get('tag_line')
        heading     =request.POST.get('heading')
        description =request.POST.get('description')
        image       =request.FILES.get('image')

        if name:
            if image:
                pers = Personal.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    address=address,
                    github=github,
                    linkedin=linkedin,
                    instagram=instagram,
                    facebook=facebook,
                    tag_line=tag_line,
                    heading=heading,
                    description=description,
                    image=image
                )
                pers.save()
                messages.success(request, 'Personal information has been saved successfully')
                return redirect('personal')
            else:
                pers = Personal.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    address=address,
                    github=github,
                    linkedin=linkedin,
                    instagram=instagram,
                    facebook=facebook,
                    tag_line=tag_line,
                    heading=heading,
                    description=description,
                )
                pers.save()
                messages.success(request, 'Personal information has been saved successfully')
                return redirect('personal')
        else:
            messages.error(request, 'Something went wrong..!!')
    return render(request, 'personal/pers_create.html', locals())

def pers_update(request, id):
    pers = Personal.objects.get(id=id)
    if request.method == 'POST':
        if request.FILES.get('image') != None:
            if pers.image != 'noImg/no_img.jpg':
                os.remove(pers.image.path)

            pers.name = request.POST.get('name')
            pers.email = request.POST.get('email')
            pers.phone = request.POST.get('phone')
            pers.address = request.POST.get('address')
            pers.github = request.POST.get('github')
            pers.linkedin = request.POST.get('linkedin')
            pers.instagram = request.POST.get('instagram')
            pers.facebook = request.POST.get('facebook')
            pers.tag_line = request.POST.get('tag_line')
            pers.heading = request.POST.get('heading')
            pers.description = request.POST.get('description')
            pers.image = request.FILES.get('image')
            pers.save()
            messages.success(request, 'Personal Information has been updated successfully')
            return redirect('personal')
        else:
            pers.name = request.POST.get('name')
            pers.email = request.POST.get('email')
            pers.phone = request.POST.get('phone')
            pers.address = request.POST.get('address')
            pers.github = request.POST.get('github')
            pers.linkedin = request.POST.get('linkedin')
            pers.instagram = request.POST.get('instagram')
            pers.facebook = request.POST.get('facebook')
            pers.tag_line = request.POST.get('tag_line')
            pers.heading = request.POST.get('heading')
            pers.description = request.POST.get('description')
            pers.save()
            messages.success(request, 'Personal Information has been updated successfully')
            return redirect('personal')
    return render(request, 'personal/pers_update.html', locals())

def pers_delete(request, id):
    pers = Personal.objects.get(id=id)
    if pers.image != 'noImg/no_img.jpg':
        os.remove(pers.image.path)
    pers.delete()
    messages.error(request, 'Personal Information has been deleted successfully')
    return redirect('personal')

# Work Experience
def we(request):
    we = Work_Experience.objects.all()
    return render(request, 'work_experience/we.html', locals())

def we_create(request):
    if request.method == 'POST':
        name            =request.POST.get('name')
        position        =request.POST.get('position')
        job_description =request.POST.get('job_description')
        joining_date    =request.POST.get('joining_date')
        resigning_date  =request.POST.get('resigning_date')
        image           =request.FILES.get('image')

        if name:
            if image:
                we = Work_Experience.objects.create(
                    name            =name,
                    position        =position,
                    job_description =job_description,
                    joining_date    =joining_date,
                    resigning_date  =resigning_date,
                    image=image
                )
                we.save()
                messages.success(request, 'Work Experience has been saved successfully')
                return redirect('we')
            else:
                we = Work_Experience.objects.create(
                    name            =name,
                    position        =position,
                    job_description =job_description,
                    joining_date    =joining_date,
                    resigning_date  =resigning_date,
                )
                we.save()
                messages.success(request, 'Work Experience has been saved successfully')
                return redirect('we')
        else:
            messages.error(request, 'Something went wrong..!!')
    return render(request, 'work_experience/we_create.html', locals())

def we_update(request, id):
    we = Work_Experience.objects.get(id=id)
    if request.method == 'POST':
        if request.FILES.get('image') != None:
            if we.image != 'noImg/no_img.jpg':
                os.remove(we.image.path)

            we.name             = request.POST.get('name')
            we.position         = request.POST.get('position')
            we.job_description  = request.POST.get('job_description')
            we.joining_date     = request.POST.get('joining_date')
            we.resigning_date   = request.POST.get('resigning_date')
            we.image            = request.FILES.get('image')
            we.save()
            messages.success(request, 'Work Experience has been updated successfully')
            return redirect('we')
        else:
            we.name = request.POST.get('name')
            we.position = request.POST.get('position')
            we.job_description = request.POST.get('job_description')
            we.joining_date = request.POST.get('joining_date')
            we.resigning_date = request.POST.get('resigning_date')
            we.save()
            messages.success(request, 'Work Experience has been updated successfully')
            return redirect('we')
    return render(request, 'work_experience/we_update.html', locals())

def we_delete(request, id):
    we = Work_Experience.objects.get(id=id)
    if we.image != 'noImg/no_img.jpg':
        os.remove(we.image.path)
    we.delete()
    messages.error(request, 'Work Experience has been deleted successfully')
    return redirect('we')

# Education
def edu(request):
    edu = Education.objects.all()
    return render(request, 'education/edu.html', locals())

def edu_create(request):
    if request.method == 'POST':
        name        =request.POST.get('name')
        degree      =request.POST.get('degree')
        major       =request.POST.get('major')
        location    =request.POST.get('location')
        logo        =request.FILES.get('logo')
        image       =request.FILES.get('image')

        if name:
            if image:
                edu = Education.objects.create(
                    name         =name,
                    degree       =degree,
                    major        =major,
                    location     =location,
                    logo         =logo,
                    image        =image
                )
                edu.save()
                messages.success(request, 'Education has been saved successfully')
                return redirect('edu')
            else:
                edu = Education.objects.create(
                    name=name,
                    degree=degree,
                    major=major,
                    location=location,
                    logo=logo,
                )
                edu.save()
                messages.success(request, 'Education has been saved successfully')
                return redirect('edu')
        else:
            messages.error(request, 'Something went wrong..!!')
    return render(request, 'education/edu_create.html', locals())

def edu_update(request, id):
    edu = Education.objects.get(id=id)
    if request.method == 'POST':
        if request.FILES.get('image') != None and request.FILES.get('logo') != None:
            if edu.image != 'noImg/no_img.jpg':
                os.remove(edu.image.path)
                os.remove(edu.logo.path)

            edu.name       = request.POST.get('name')
            edu.degree     = request.POST.get('degree')
            edu.major      = request.POST.get('major')
            edu.location   = request.POST.get('location')
            edu.logo       = request.FILES.get('logo')
            edu.image      = request.FILES.get('image')
            edu.save()
            messages.success(request, 'Education has been updated successfully')
            return redirect('edu')
        else:
            edu.name = request.POST.get('name')
            edu.degree = request.POST.get('degree')
            edu.major = request.POST.get('major')
            edu.location = request.POST.get('location')
            edu.save()
            messages.success(request, 'Education has been updated successfully')
            return redirect('edu')
    return render(request, 'education/edu_update.html', locals())

def edu_delete(request, id):
    edu = Education.objects.get(id=id)
    if edu.image != 'noImg/no_img.jpg':
        os.remove(edu.image.path)
        os.remove(edu.logo.path)
    edu.delete()
    messages.error(request, 'Education has been deleted successfully')
    return redirect('edu')

# Professional Training
def pt(request):
    pt = Training.objects.all()
    return render(request, 'training/pt.html', locals())

def pt_create(request):
    if request.method == 'POST':
        name        =request.POST.get('name')
        institute   =request.POST.get('institute')
        description =request.POST.get('description')
        image       =request.FILES.get('image')

        if name:
            if image:
                pt = Training.objects.create(
                    name            =name,
                    institute       =institute,
                    description     =description,
                    image           =image
                )
                pt.save()
                messages.success(request, 'Training has been saved successfully')
                return redirect('pt')
            else:
                pt = Training.objects.create(
                    name        =name,
                    institute   =institute,
                    description =description,

                )
                pt.save()
                messages.success(request, 'Training has been saved successfully')
                return redirect('pt')
        else:
            messages.error(request, 'Something went wrong..!!')
    return render(request, 'training/pt_create.html', locals())

def pt_update(request, id):
    pt = Training.objects.get(id=id)
    if request.method == 'POST':
        if request.FILES.get('image') != None:
            if pt.image != 'noImg/no_img.jpg':
                os.remove(pt.image.path)

            pt.name             = request.POST.get('name')
            pt.institute        = request.POST.get('institute')
            pt.description      = request.POST.get('description')
            pt.image            = request.FILES.get('image')
            pt.save()
            messages.success(request, 'Training has been updated successfully')
            return redirect('pt')
        else:
            pt.name = request.POST.get('name')
            pt.institute = request.POST.get('institute')
            pt.description = request.POST.get('description')
            pt.save()
            messages.success(request, 'Training has been updated successfully')
            return redirect('pt')
    return render(request, 'training/pt_update.html', locals())

def pt_delete(request, id):
    pt = Training.objects.get(id=id)
    if pt.image != 'noImg/no_img.jpg':
        os.remove(pt.image.path)
    pt.delete()
    messages.error(request, 'Training has been deleted successfully')
    return redirect('pt')

# Skills
def skl(request):
    skl = Skills.objects.all()
    return render(request, 'skill/skl.html', locals())

def skl_create(request):
    if request.method == 'POST':
        name        =request.POST.get('name')
        potentials  =request.POST.get('potentials')
        image       =request.FILES.get('image')

        if name:
            if image:
                skl = Skills.objects.create(
                    name            =name,
                    potentials      =potentials,
                    image           =image
                )
                skl.save()
                messages.success(request, 'Skills has been saved successfully')
                return redirect('skl')
            else:
                skl = Skills.objects.create(
                    name        =name,
                    potentials  =potentials,

                )
                skl.save()
                messages.success(request, 'Skills has been saved successfully')
                return redirect('skl')
        else:
            messages.error(request, 'Something went wrong..!!')
    return render(request, 'skill/skl_create.html', locals())

def skl_update(request, id):
    skl = Skills.objects.get(id=id)
    if request.method == 'POST':
        if request.FILES.get('image') != None:
            if skl.image != 'noImg/no_img.jpg':
                os.remove(skl.image.path)

            skl.name             = request.POST.get('name')
            skl.potentials       = request.POST.get('potentials')
            skl.image            = request.FILES.get('image')
            skl.save()
            messages.success(request, 'Skills has been updated successfully')
            return redirect('skl')
        else:
            skl.name       = request.POST.get('name')
            skl.potentials = request.POST.get('potentials')
            skl.save()
            messages.success(request, 'Skills has been updated successfully')
            return redirect('skl')
    return render(request, 'skill/skl_update.html', locals())

def skl_delete(request, id):
    skl = Skills.objects.get(id=id)
    if skl.image != 'noImg/no_img.jpg':
        os.remove(skl.image.path)
    skl.delete()
    messages.error(request, 'Skills has been deleted successfully')
    return redirect('skl')

# Portfolio
def port(request):
    port = Portfolio.objects.all()
    return render(request, 'portfolio/port.html', locals())

def port_create(request):
    if request.method == 'POST':
        name        =request.POST.get('name')
        description =request.POST.get('description')
        gitlink     =request.POST.get('gitlink')
        projectURL  =request.POST.get('projectURL')
        image       =request.FILES.get('image')

        if name:
            if image:
                port = Portfolio.objects.create(
                    name            =name,
                    description     =description,
                    gitlink         =gitlink,
                    projectURL      =projectURL,
                    image           =image
                )
                port.save()
                messages.success(request, 'Portfolio has been saved successfully')
                return redirect('port')
            else:
                port = Portfolio.objects.create(
                    name=name,
                    description=description,
                    gitlink=gitlink,
                    projectURL=projectURL,
                )
                port.save()
                messages.success(request, 'Portfolio has been saved successfully')
                return redirect('port')
        else:
            messages.error(request, 'Something went wrong..!!')
    return render(request, 'portfolio/port_create.html', locals())

def port_update(request, id):
    port = Portfolio.objects.get(id=id)
    if request.method == 'POST':
        if request.FILES.get('image') != None:
            if port.image != 'noImg/no_img.jpg':
                os.remove(port.image.path)

            port.name             = request.POST.get('name')
            port.description      = request.POST.get('description')
            port.gitlink          = request.POST.get('gitlink')
            port.projectURL       = request.POST.get('projectURL')
            port.image            = request.FILES.get('image')
            port.save()
            messages.success(request, 'Portfolio has been updated successfully')
            return redirect('port')
        else:
            port.name = request.POST.get('name')
            port.description = request.POST.get('description')
            port.gitlink = request.POST.get('gitlink')
            port.projectURL = request.POST.get('projectURL')
            port.save()
            messages.success(request, 'Portfolio has been updated successfully')
            return redirect('port')
    return render(request, 'portfolio/port_update.html', locals())

def port_delete(request, id):
    port = Portfolio.objects.get(id=id)
    if port.image != 'noImg/no_img.jpg':
        os.remove(port.image.path)
    port.delete()
    messages.error(request, 'Portfolio has been deleted successfully')
    return redirect('port')

# Platform
def plat(request):
    plat = Platform.objects.all()
    return render(request, 'platform/plat.html', locals())

def plat_create(request):
    if request.method == 'POST':
        name        =request.POST.get('name')
        image       =request.FILES.get('image')

        if name:
            if image:
                plat = Platform.objects.create(
                    name            =name,
                    image           =image
                )
                plat.save()
                messages.success(request, 'Platform has been saved successfully')
                return redirect('plat')
            else:
                plat = Platform.objects.create(
                    name=name,
                )
                plat.save()
                messages.success(request, 'Platform has been saved successfully')
                return redirect('plat')
        else:
            messages.error(request, 'Something went wrong..!!')
    return render(request, 'platform/plat_create.html', locals())

def plat_update(request, id):
    plat = Platform.objects.get(id=id)
    if request.method == 'POST':
        if request.FILES.get('image') != None:
            if plat.image != 'noImg/no_img.jpg':
                os.remove(plat.image.path)

            plat.name             = request.POST.get('name')
            plat.image            = request.FILES.get('image')
            plat.save()
            messages.success(request, 'Platform has been updated successfully')
            return redirect('plat')
        else:
            plat.name = request.POST.get('name')
            plat.save()
            messages.success(request, 'Platform has been updated successfully')
            return redirect('plat')
    return render(request, 'platform/plat_update.html', locals())

def plat_delete(request, id):
    plat = Platform.objects.get(id=id)
    if plat.image != 'noImg/no_img.jpg':
        os.remove(plat.image.path)
    plat.delete()
    messages.error(request, 'Platform has been deleted successfully')
    return redirect('plat')

# Language
def lang(request):
    lang = Language.objects.all()
    return render(request, 'language/lang.html', locals())

def lang_create(request):
    if request.method == 'POST':
        name        =request.POST.get('name')
        potentials  =request.POST.get('potentials')

        if name:
            lang = Language.objects.create(
                name=name,
                potentials=potentials
            )
            lang.save()
            messages.success(request, 'Language has been saved successfully')
            return redirect('lang')
        else:
            messages.error(request, 'Something went wrong..!!')
    return render(request, 'language/lang_create.html', locals())

def lang_update(request, id):
    lang = Language.objects.get(id=id)
    if request.method == 'POST':
        lang.name       = request.POST.get('name')
        lang.potentials = request.POST.get('potentials')
        lang.save()
        messages.success(request, 'Language has been updated successfully')
        return redirect('lang')
    return render(request, 'language/lang_update.html', locals())

def lang_delete(request, id):
    lang = Language.objects.get(id=id)
    lang.delete()
    messages.error(request, 'Language has been deleted successfully')
    return redirect('lang')

# Reference
def ref(request):
    ref = Reference.objects.all()
    return render(request, 'reference/ref.html', locals())

def ref_create(request):
    if request.method == 'POST':
        name        =request.POST.get('name')
        designation =request.POST.get('designation')
        relation    =request.POST.get('relation')
        email       =request.POST.get('email')
        phone       =request.POST.get('phone')

        if name:
            ref = Reference.objects.create(
                name        =name,
                designation =designation,
                relation    =relation,
                email       =email,
                phone       =phone
            )
            ref.save()
            messages.success(request, 'Reference has been saved successfully')
            return redirect('ref')
        else:
            messages.error(request, 'Something went wrong..!!')
    return render(request, 'reference/ref_create.html', locals())

def ref_update(request, id):
    ref = Reference.objects.get(id=id)
    if request.method == 'POST':
        ref.name        = request.POST.get('name')
        ref.designation = request.POST.get('designation')
        ref.relation    = request.POST.get('relation')
        ref.email       = request.POST.get('email')
        ref.phone       = request.POST.get('phone')
        ref.save()
        messages.success(request, 'Reference has been updated successfully')
        return redirect('ref')
    return render(request, 'reference/ref_update.html', locals())

def ref_delete(request, id):
    ref = Reference.objects.get(id=id)
    ref.delete()
    messages.error(request, 'Reference has been deleted successfully')
    return redirect('ref')





