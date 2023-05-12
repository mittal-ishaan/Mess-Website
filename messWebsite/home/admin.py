"""
File-name: admin.py
This file is registers the models on the adming page and customizes the admin page
For more information please see: https://docs.djangoproject.com/en/4.1/ref/contrib/admin/
"""
from django.contrib import admin
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from home.models import (
    About,
    Update,
    Rule,
    Carousel,
    Photos,
    Penalty,
    ShortRebate,
    LongRebate,
    Caterer,
    Form,
    Cafeteria,
    Contact,
    Student,
    Allocation,
    Scan,
    Rebate,
    RebateSpringSem,
    RebateAutumnSem
)
from import_export.admin import ImportExportModelAdmin, ImportExportMixin

from .resources import StudentResource, AllocationResource, RebateResource, RebateSpringResource, RebateAutumnResource

# Customising the heading and title of the admin page
admin.site.site_header = 'Dining Website Admin Page'
admin.site.site_title = 'Admin Page'
admin.site.index_title = 'Website Admin panel'


# Text of description content of each model
ABOUT_DESC_TEXT = "This contains the content that will show up in the about section of the home page. Add all of the About us Content in one field itself."
CAROUSEL_DESC_TEXT = "This contains the images that will show up in the carousel of the home page. Add new field for each new image."
UPDATE_DESC_TEXT = "This contains the content that will show up in the update section of the home page. Add new field for each new update."
PHOTOS_DESC_TEXT = "This contains the photographs that will show up in the bottom section of the home page. Add new field for each new image."
RULE_DESC_TEXT = "This contains the content that will show up in the rule section of the Rules page. Add new field for each new rule."
PENALTY_DESC_TEXT = "This contains the content that will show up in the penalty section of the Rules page. Add new field for each new penalty."
SHORT_REBATE_DESC_TEXT = "This contains the content that will show up in the short rebate section of the rules page. Add all of the short term rebate Content in one field itself."
LONG_REBATE_DESC_TEXT = "This contains the content that will show up in the rule section of the Rules page. Add new field for each new rule."
CATERER_DESC_TEXT = "This contains the content that will show up in the respective caterers page. Add new field for each new caterer."
FORM_DESC_TEXT = "This contains the content that will show up in the forms page. Add new field for each new form data."
CAFETERIA_DESC_TEXT = "This contains the content that will show up in the cafeteria page. Add new field for each new cafeteria."
CONTACT_DESC_TEXT = "This contains the content that will show up in the contact page. Add new field for each new contact."
ALLOCATION_DESC_TEXT = "This contains the Allocation details of the students. First import data through /allocation/ url then export"
STUDENT_DESC_TEXT = "This contains the Basic details of each students."
REBATE_DESC_TEXT = "This contains the rebate details of each rebate applied by the students."
REBATE_BILLS_DESC_TEXT = "This contains the rebate bills of each students."

# Register your models here


@admin.register(About)
class about_Admin(admin.ModelAdmin):
    model = About
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "description",
                ),
                "description": "%s" % ABOUT_DESC_TEXT,
            },
        ),
    )


@admin.register(Carousel)
class about_Admin(admin.ModelAdmin):
    model = Carousel
#    ordering=("image",)
#    search_fields = ("image")
#    list_display = ("image")
#    list_filter = ("image",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "image",
                ),
                "description": "%s" % CAROUSEL_DESC_TEXT,
            },
        ),
    )


@admin.register(Update)
class about_Admin(admin.ModelAdmin):
    model = Update
    ordering = ("-time_stamp",)
    search_fields = ("update", "time_stamp")
    list_filter = ("time_stamp",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "update",
                ),
                "description": "%s" % UPDATE_DESC_TEXT,
            },
        ),
    )


@admin.register(Photos)
class about_Admin(admin.ModelAdmin):
    model = Photos
    search_fields = ("poc", "occupation",)
    list_display = ("poc",)
    list_filter = ("poc", "occupation",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "image",
                    "poc",
                    "occupation"
                ),
                "description": "%s" % PHOTOS_DESC_TEXT,
            },
        ),
    )


@admin.register(Rule)
class about_Admin(admin.ModelAdmin):
    model = Rule
    ordering = ("rule",)
    search_fields = ("rule",)
    list_display = ("rule",)
    list_filter = ("rule",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "rule",
                ),
                "description": "%s" % RULE_DESC_TEXT,
            },
        ),
    )


@admin.register(Penalty)
class about_Admin(admin.ModelAdmin):
    model = Penalty
    ordering = ("penalty",)
    search_fields = ("penalty",)
    list_display = ("penalty",)
    list_filter = ("penalty",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "penalty",
                ),
                "description": "%s" % PENALTY_DESC_TEXT,
            },
        ),
    )


@admin.register(ShortRebate)
class about_Admin(admin.ModelAdmin):
    model = ShortRebate
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "desc",
                    "link",
                    'policy',
                    'circulation',
                    'infoToCaterer',
                    'note',
                    'Memebers',
                    'biling',
                ),
                "description": "%s" % SHORT_REBATE_DESC_TEXT,
            },
        ),
    )


@admin.register(LongRebate)
class about_Admin(admin.ModelAdmin):
    model = LongRebate
    ordering = ("rule",)
    search_fields = ("rule",)
    list_display = ("rule",)
    list_filter = ("rule",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "rule",
                ),
                "description": "%s" % LONG_REBATE_DESC_TEXT,
            },
        ),
    )


@admin.register(Caterer)
class about_Admin(admin.ModelAdmin):
    model = Caterer
    search_fields = ("name",)
    list_filter = ("name",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "upper_description",
                    "sheet_url",
                    "lower_description",
                    "student_limit"
                ),
                "description": "%s" % CATERER_DESC_TEXT,
            },
        ),
    )


@admin.register(Form)
class about_Admin(admin.ModelAdmin):
    model = Form
    search_fields = ("heading", "description")
    list_filter = ("heading",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "heading",
                    "url",
                    "description",
                ),
                "description": "%s" % FORM_DESC_TEXT,
            },
        ),
    )


@admin.register(Cafeteria)
class about_Admin(admin.ModelAdmin):
    model = Cafeteria
    search_fields = ("name", "poc")
    list_filter = ("name",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "poc",
                    "contact",
                    "image",
                ),
                "description": "%s" % CAFETERIA_DESC_TEXT,
            },
        ),
    )


@admin.register(Contact)
class about_Admin(admin.ModelAdmin):
    model = Contact
    search_fields = ("occupation", "name", "hostel_sec")
    list_filter = ("occupation", "hostel_sec")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("occupation", "hostel_sec"),
                    "name",
                    "contact",
                    "email",
                ),
                "description": "%s" % CONTACT_DESC_TEXT,
            },
        ),
    )


@admin.register(Allocation)
class about_Admin(ImportExportMixin, admin.ModelAdmin):
    resource_class = AllocationResource
    model = Allocation
    search_fields = ("student_id", "month", "caterer_name", "high_tea")
    list_filter = ("month", "caterer_name", "high_tea")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "roll_no",
                    "month",
                    "student_id",
                    "caterer_name",
                    "high_tea",
                    "first_pref",
                    "second_pref",
                    "third_pref"
                ),
                "description": "%s" %ALLOCATION_DESC_TEXT,
            },
        ),
    )
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = AllocationResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="allocation.csv"'
        return response

    export_as_csv.short_description = "Export Allocation details to CSV"

#  # Define the import action
#     def import_csv(self, request, queryset):
#         # Get the selected file from the request
#         file = request.FILES['file']

#         # Read the CSV file
#         reader = csv.DictReader(file)

#         # Loop over each row in the CSV file
#         for row in reader:
#             # Create a new Book object and save it
#             a = Allocatio(
#               )
#             book.save()

#         # Return a success message
#         self.message_user(request, 'CSV file imported successfully.')

#     import_csv.short_description = 'Import CSV'

#     # Override the default actions to include the import action
#     actions = [import_csv] + ModelAdmin.actions


@admin.register(Student)
class about_Admin(ImportExportMixin, admin.ModelAdmin):
    resource_class = StudentResource
    model = Student
    search_fields = ("student_id", "name", "roll_no",
                     "hostel", "degree", "department")
    list_filter = ("hostel", "degree", "department")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "email",
                    "roll_no",
                    "hostel",
                    "room_no",
                    "degree",
                    "department"
                ),
                "description": "%s" %STUDENT_DESC_TEXT,
            },
        ),
    )
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = StudentResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Student.csv"'
        return response

    export_as_csv.short_description = "Export Student details to CSV"


@admin.register(Scan)
class about_Admin(admin.ModelAdmin):
    model = Scan
    search_fields = ("student_id", "date")
    list_filter = ("date",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "student_id",
                    "date",
                    "breakfast",
                    "lunch",
                    "high_tea",
                    "dinner"
                ),
                #                "description": "%s" %_DESC_TEXT,
            },
        ),
    )


@admin.register(Rebate)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RebateResource
    model = Rebate
    search_fields = ("allocation_id__student_id", "approved",
                     "date_applied", "start_date", "end_date")
    list_filter = ("approved", "date_applied",
                   "allocation_id", "start_date", "end_date")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "allocation_id",
                    "date_applied",
                    "start_date",
                    "end_date",
                    "approved",
                ),
                "description": "%s" %REBATE_DESC_TEXT,
            },
        ),
    )
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = RebateResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Rebate.csv"'
        return response

    export_as_csv.short_description = "Export Rebate details to CSV"


@admin.register(RebateAutumnSem)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RebateAutumnResource
    model = RebateAutumnSem
    search_fields = ("email",)
    list_filter = ("email",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "july",
                    "highTeaJuly",
                    "august",
                    "highTeaAugust",
                    "september",
                    "highTeaSeptember",
                    "october",
                    "highTeaOctober",
                    "november",
                    "highTeaNovember",
                    "december",
                    "highTeaDecember",
                ),
                "description": "%s" %REBATE_BILLS_DESC_TEXT,
            },
        ),
    )
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = RebateAutumnResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="RebateAutumn.csv"'
        return response

    export_as_csv.short_description = "Export Rebate details to CSV"


@admin.register(RebateSpringSem)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RebateSpringResource
    model = RebateSpringSem
    search_fields = ("email",)
    list_filter = ("email",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "january",
                    "highTeaJanuary",
                    "feburary",
                    "highTeaFeburary",
                    "march",
                    "highTeaMarch",
                    "april",
                    "highTeaApril",
                    "may",
                    "highTeaMay",
                    "june",
                    "highTeaJune",
                ),
                "description": "%s" %REBATE_BILLS_DESC_TEXT,
            },
        ),
    )
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = RebateSpringResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="RebateSpring.csv"'
        return response

    export_as_csv.short_description = "Export Rebate details to CSV"