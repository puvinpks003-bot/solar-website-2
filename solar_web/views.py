from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Lead

def home_view(request):
    """
    Serves the primary comprehensive page architecture.
    Passes filtered high-tension megawatt scale data into the UI shell.
    """
    # Fetching the premium high-capacity installations for visual proof
    mw_projects = Project.objects.filter(category='MW').order_by('-created_at')[:3]
    all_projects = Project.objects.all().order_by('-created_at')[:6]
    
    context = {
        'mw_projects': mw_projects,
        'all_projects': all_projects,
        
    }
    return render(request, 'solar_web/home.html', context)


def submit_lead_view(request):
    """
    Handles form collection endpoints cleanly with safe redirect fallbacks.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        location = request.POST.get('location')
        monthly_bill = request.POST.get('monthly_bill')
        project_scale = request.POST.get('project_scale')
        financial_assistance = request.POST.get('financial_assistance') or None
        print(name, phone, email, location, monthly_bill, project_scale, financial_assistance)
        if not name or not phone or not location:
            messages.error(request, "Error: Please provide all required site audit parameters.")
            return redirect('home')
            
        Lead.objects.create(
            name=name, phone=phone, email=email, location=location,
            monthly_bill=monthly_bill, project_scale=project_scale,
            financial_assistance=financial_assistance
        )
        print("Lead submitted successfully!")
        
        messages.success(request, "Success! The SIP INFRA engineering team has received your audit parameters.")
        return redirect('home')
        
    return redirect('home')


def industrial_view(request):
    return render(request, 'solar_web/industrial.html')

def commercial_view(request):
    return render(request, 'solar_web/commercial.html')

def residential_view(request):
    return render(request, 'solar_web/residential.html')

def subsidy_view(request):
    return render(request, 'solar_web/subsidy.html')

def engineering_epc_view(request):
    return render(request, 'solar_web/engineering_epc.html')

def operation_maintenance_view(request):
    return render(request, 'solar_web/operation_maintenance.html')

def projects_portfolio_view(request):
    # Dummy structure for template looping matching your project requirement
    context = {
        'mw_projects': [
            {'title': '1.2 MW Rooftop Array', 'location': 'Erode', 'capacity_kw': 1200, 'description': 'Engineered to offset structural utility loads while safely handling intense local building machinery vibrations.', 'get_category_display': 'Industrial MW Scale'},
            {'title': '600 kW High-Yield Array', 'location': 'Madurai', 'capacity_kw': 600, 'description': 'Configured to buffer daytime cooling surges, protecting industrial compressors against high-demand grid penalties.', 'get_category_display': 'Commercial Setup'},
            {'title': '15 kW Hybrid Configuration', 'location': 'Chennai', 'capacity_kw': 15, 'description': 'Integrated alongside high-cycle lithium backup banks to provide complete self-sufficiency during coastal monsoon seasons.', 'get_category_display': 'Residential Rooftop'},
            {'title': '1.2 MW Rooftop Array', 'location': 'Erode', 'capacity_kw': 1200, 'description': 'Engineered to offset structural utility loads while safely handling intense local building machinery vibrations.', 'get_category_display': 'Industrial MW Scale'},
            {'title': '600 kW High-Yield Array', 'location': 'Madurai', 'capacity_kw': 600, 'description': 'Configured to buffer daytime cooling surges, protecting industrial compressors against high-demand grid penalties.', 'get_category_display': 'Commercial Setup'},
            {'title': '15 kW Hybrid Configuration', 'location': 'Chennai', 'capacity_kw': 15, 'description': 'Integrated alongside high-cycle lithium backup banks to provide complete self-sufficiency during coastal monsoon seasons.', 'get_category_display': 'Residential Rooftop'},
            {'title': '1.2 MW Rooftop Array', 'location': 'Erode', 'capacity_kw': 1200, 'description': 'Engineered to offset structural utility loads while safely handling intense local building machinery vibrations.', 'get_category_display': 'Industrial MW Scale'},
            {'title': '600 kW High-Yield Array', 'location': 'Madurai', 'capacity_kw': 600, 'description': 'Configured to buffer daytime cooling surges, protecting industrial compressors against high-demand grid penalties.', 'get_category_display': 'Commercial Setup'},
            {'title': '15 kW Hybrid Configuration', 'location': 'Chennai', 'capacity_kw': 15, 'description': 'Integrated alongside high-cycle lithium backup banks to provide complete self-sufficiency during coastal monsoon seasons.', 'get_category_display': 'Residential Rooftop'},
            {'title': '1.2 MW Rooftop Array', 'location': 'Erode', 'capacity_kw': 1200, 'description': 'Engineered to offset structural utility loads while safely handling intense local building machinery vibrations.', 'get_category_display': 'Industrial MW Scale'},
            {'title': '600 kW High-Yield Array', 'location': 'Madurai', 'capacity_kw': 600, 'description': 'Configured to buffer daytime cooling surges, protecting industrial compressors against high-demand grid penalties.', 'get_category_display': 'Commercial Setup'},
            {'title': '15 kW Hybrid Configuration', 'location': 'Chennai', 'capacity_kw': 15, 'description': 'Integrated alongside high-cycle lithium backup banks to provide complete self-sufficiency during coastal monsoon seasons.', 'get_category_display': 'Residential Rooftop'}
        
        ]
    }
    return render(request, 'solar_web/projects_portfolio.html', context)

def investor_relations_view(request):
    return render(request, 'solar_web/investor_relations.html')

def contact_desk_view(request):
    return render(request, 'solar_web/contact_desk.html')

