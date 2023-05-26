from django.db import models
from django.utils.translation import gettext as _
from django.utils.timezone import now
from ..students import Student
from ..caterer import Caterer

class PeriodSpring23(models.Model):
    Sno = models.IntegerField(_("Sno"),default=0,help_text="This contains the serial number of the Period")
    start_date = models.DateField(help_text="This contains the start date of this Period for this semester",null=True,blank=True)
    end_date = models.DateField(help_text="This contains the end date of this Period of this semester",null=True,blank=True)
    
    def __str__(self):
        return "Period :" + str(self.Sno)

    class Meta:
        verbose_name = "Period Details for Spring 2023"
        verbose_name_plural = "Period Details for Spring 2023"


class AllocationSpring23(models.Model):
    """
    Stores the Allocation details
    """

    roll_no = models.ForeignKey(
        Student, default=0, on_delete=models.SET_NULL, null=True
    )
    student_id = models.CharField(
        _("Allocation Id"),
        default=None,
        max_length=30,
        help_text="This contains the Allocation Id",
        null=True,
        blank=True,
    )
    month = models.ForeignKey(
        PeriodSpring23, default=0, on_delete=models.SET_NULL, null=True
    )
    caterer_name = models.CharField(
        _("Caterer Name"),
        max_length=50,
        help_text="The text in this text field contains the caterer name.",
        default="",null=True,blank=True
    )
    high_tea = models.BooleanField(
        _("High Tea"), help_text="This contains the info if high tea is taken or not",
        default=False,null=True,blank=True
    )
    first_pref = models.CharField(
        _("First Preference"),
        default=None,
        max_length=10,
        help_text="This contians the first preference caterer of the student",
        null=True,blank=True
    )
    second_pref = models.CharField(
        _("Second Preference"),
        default=None,
        max_length=10,
        help_text="This contians the first preference caterer of the student",
        null=True,blank=True
    )
    third_pref = models.CharField(
        _("Third Preference"),
        default=None,
        max_length=10,
        help_text="This contians the first preference caterer of the student",
        null=True,blank=True
    )

    def __str__(self):
        return self.student_id

    class Meta:
        verbose_name = "Allocation Details for Spring 2023"
        verbose_name_plural = "Allocation Details for Spring 2023"


class RebateSpring23(models.Model):
    """
    Storing the Rebate Bills of the Students for the Spring Semester
    """
    email = models.ForeignKey(Student, on_delete=models.SET_NULL, default="", null=True)

    period1_short = models.IntegerField(_("January Short"),default=0, null=True)
    period1_long = models.IntegerField(_("January Long"),default=0,null=True)
    period1_high_tea = models.BooleanField(_("January High Tea"),default=True)
    period1_bill = models.IntegerField(_("January Rebate Amount"),default=0,null=True)

    period2_short = models.IntegerField(_("Feburary Short"),default=0, null=True)
    period2_long = models.IntegerField(_("Feburary Long"),default=0,null=True)
    period2_high_tea = models.BooleanField(_("Feburary High Tea"),default=True)
    period2_bill = models.IntegerField(_("Feburary Rebate Amount"),default=0,null=True)

    period3_short = models.IntegerField(_("March Short"),default=0, null=True)
    period3_long = models.IntegerField(_("March Long"),default=0,null=True)
    period3_high_tea = models.BooleanField(_("March High Tea"),default=True)
    period3_bill = models.IntegerField(_("March Rebate Amount"),default=0,null=True)

    period4_short = models.IntegerField(_("April Short"),default=0, null=True)
    period4_long = models.IntegerField(_("April Long"),default=0,null=True)
    period4_high_tea = models.BooleanField(_("April High Tea"),default=True)
    period4_bill = models.IntegerField(_("April Rebate Amount"),default=0,null=True)

    period5_short = models.IntegerField(_("May Short"),default=0, null=True)
    period5_long = models.IntegerField(_("May Long"),default=0,null=True)
    period5_high_tea = models.BooleanField(_("May High Tea"),default=True)
    period5_bill = models.IntegerField(_("May Rebate Amount"),default=0,null=True)

    period6_short = models.IntegerField(_("June Short"),default=0, null=True)
    period6_long = models.IntegerField(_("June Long"),default=0,null=True)
    period6_high_tea = models.BooleanField(_("June High Tea"),default=True)
    period6_bill = models.IntegerField(_("June Rebate Amount"),default=0,null=True)

    def __str__(self):
        return str(self.email.email)

    class Meta:
        verbose_name = "Rebate Bill Spring 2023"
        verbose_name_plural = "Rebate Bills Spring 2023"

class CatererBillsSpring23(models.Model):
    """
    Storing the Bills of the Caterers for the Spring Semester
    """
    caterer = models.ForeignKey(Caterer, on_delete=models.SET_NULL, null=True)

    period1_bills = models.IntegerField(_("January Bill"),default=0, null=True)
    period2_bills = models.IntegerField(_("Feburary Bill"),default=0, null=True)
    period3_bills = models.IntegerField(_("March Bill"),default=0, null=True)
    period4_bills = models.IntegerField(_("April Bill"),default=0, null=True)
    period5_bills = models.IntegerField(_("May Bill"),default=0, null=True)
    period6_bills = models.IntegerField(_("June Bill"),default=0, null=True)

    def __str__(self):
        return str(self.caterer.name)

    class Meta:
        verbose_name = "Caterer Bill Spring 2023"
        verbose_name_plural = "Caterer Bills Spring 2023"