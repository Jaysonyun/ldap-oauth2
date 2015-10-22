from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from application.models import Application


def validate_join_year(value):
    current_year = timezone.now().year
    if value < 1958:
        raise ValidationError(_('%d! Are you kidding me? IITB was not even there back then!' % value))
    if value > current_year:
        raise ValidationError(_('Welcome kiddo, welcome to IITB in future!'))


def validate_graduation_year(value):
    current_year = timezone.now().year
    if value < 1958:
        raise ValidationError(_('%d! Are you kidding me? IITB was not even there back then!' % value))
    if value > (current_year + 6):
        raise ValidationError(_('Please enter your expected graduation year'))


class InstituteAddress(models.Model):
    HOSTEL_CHOICES = [
        ['1', 'Hostel 1'],
        ['2', 'Hostel 2'],
        ['3', 'Hostel 3'],
        ['4', 'Hostel 4'],
        ['5', 'Hostel 5'],
        ['6', 'Hostel 6'],
        ['7', 'Hostel 7'],
        ['8', 'Hostel 8'],
        ['9', 'Hostel 9'],
        ['10', 'Hostel 10'],
        ['10A', 'Hostel 10A'],
        ['11', 'Hostel 11'],
        ['12', 'Hostel 12'],
        ['13', 'Hostel 13'],
        ['14', 'Hostel 14'],
        ['15', 'Hostel 15'],
        ['16', 'Hostel 16'],
        ['tansa', 'Tansa'],
        ['qip', 'QIP'],
    ]

    user = models.OneToOneField(User, related_name='insti_address')
    room = models.CharField(max_length=8, null=True, blank=True)
    hostel = models.CharField(max_length=8, choices=HOSTEL_CHOICES, null=True, blank=True)

    def __unicode__(self):
        if self.hostel:
            if self.room:
                return "%s-%s" % (self.hostel, self.room)
            return self.hostel
        return ''


class Program(models.Model):
    DEPARTMENT_CHOICES = [
        # Departments
        ['AE', 'Aerospace Engineering'],
        ['BB', 'Biosciences and Bioengineering'],
        ['CHE', 'Chemical Engineering'],
        ['CH', 'Chemistry'],
        ['CLE', 'Civil Engineering'],
        ['CSE', 'Computer Science & Engineering'],
        ['ES', 'Earth Sciences'],
        ['EE', 'Electrical Engineering'],
        ['ESE', 'Energy Science and Engineering'],
        ['HSS', 'Humanities & Social Science'],
        ['IDC', 'Industrial Design Centre'],
        ['MM', 'Mathematics'],
        ['ME', 'Mechanical Engineering'],
        ['MEMS', 'Metallurgical Engineering & Materials Science'],
        ['PH', 'Physics'],
        ['MS', 'Material Science'],
        ['PHE', 'Physical Education'],
        ['PMS', 'Physics, Material Science'],
        ['PC', 'Preparatory Course'],
        ['RE', 'Reliability Engineering'],

        # Centers
        ['ASC', 'Application Software Centre'],
        ['CRNTS', 'Centre for Research in Nanotechnology and Science'],
        ['CASDE', 'Centre for Aerospace Systems Design and Engineering'],
        ['CC', 'Computer Centre'],
        ['CDEEP', 'Centre for Distance Engineering Education Programme'],
        ['CESE', 'Centre for Environmental Science and Engineering'],
        ['CSRE', 'Centre of Studies in Resources Engineering'],
        ['CTARA', 'Centre for Technology Alternatives for Rural Areas'],
        ['CFDVS', 'Centre for Formal Design and Verification of Software'],
        ['CUSE', 'Centre for Urban Science and Engineering'],
        ['DSCE', 'Desai Sethi Centre for Entrepreneurship'],
        ['IITBMRA', 'IITB-Monash Research Academy'],
        ['NCAIR', 'National Centre for Aerospace Innovation and Research'],
        ['NCM', 'National Centre for Mathematics'],
        ['SAIF', 'Sophisticated Analytical Instrument Facility'],
        ['TCTD', 'Tata Center for Technology and Design'],
        ['WRCB', 'Wadhwani Research Centre for Bioengineering'],
        ['BIOTECH', 'Biotechnology'],

        # School
        ['SJMSOM', 'Shailesh J. Mehta School of Management'],
        ['KReSIT', 'Kanwal Rekhi School of Information Technology'],

        # Interdisciplinary Programs
        ['CLS', 'Climate Studies'],
        ['ET', 'Educational Technology'],
        ['IEOR', 'Industrial Engineering and Operations Research'],
        ['SCE', 'Systems and Control Engineering'],

        # IDC
        ['ANIM', 'Animation'],
        ['IDC', 'Industrial Design Centre'],
        ['IxD', 'Interaction Design'],
        ['MVD', 'Mobility and Vehicle Design'],
        ['VISCOM', 'Visual Communication'],

        # Others
        ['IM', 'Industrial Management'],
        ['MMM', 'Materials, Manufacturing and Modelling'],
        ['CORRSCI', 'Corrosion Science and Engineering'],
        ['CEP', 'Continuing Education Programme'],
        ['AppGP', 'Applied Geophysics'],
        ['ASI', 'Applied Statistics and Informatics'],
        ['BME', 'Biomedical Engineering'],

    ]

    DEGREES = [
        ['BTECH', 'Bachelor of Technology'],
        ['MTECH', 'Master of Technology'],
        ['DD', 'B.Tech. + M.Tech. Dual Degree'],
        ['MSC', 'Master of Science'],
        ['PHD', 'Doctor of Philosophy'],
        ['BDES', 'Bachelor of Design'],
        ['MDES', 'Master of Design'],
        ['MPHIL', 'Master of Philosophy'],
        ['MMG', 'Master of Management'],
        ['MSEx', 'M.S. (Exit Degree)'],
        ['MtechEx', 'Master of Technology (Exit Degree)'],
        ['MtechPhDDD', 'M.Tech. + Ph.D. Dual Degree'],
        ['PC', 'Preparatory Course'],
        ['VS', 'Visiting Student'],
        ['MPhilEx', 'Master of Philosophy (Exit Degree)'],
        ['MScEx', 'Master of Science (Exit Degree)'],
        ['MScMTechDD', 'M.Sc. + M.Tech. Dual Degree'],
        ['MScPhDDD', 'M.Sc. + Ph.D. Dual Degree'],
        ['MPhilPhDDD', 'M.Phil. + Ph.D. Dual Degree'],
        ['EMBA', 'Executive MBA'],
        ['FYBS', 'Four Year BS'],
        ['IMTECH', 'Integrated M.Tech.'],
        ['MSCBR', 'Master of Science By Research'],
        ['TYMSC', 'Two Year M.Sc.'],
        ['FYIMSC', 'Five Year Integrated M.Sc.'],
        ['DIIT', 'D.I.I.T.'],
        ['DIITEx', 'D.I.T.T. (Exit Degree)'],
    ]

    user = models.OneToOneField(User, related_name='program')
    department = models.CharField(max_length=8, choices=sorted(DEPARTMENT_CHOICES, key=lambda x: x[1]), null=True,
                                  blank=True)
    join_year = models.PositiveSmallIntegerField(null=True, blank=True, validators=[validate_join_year])
    graduation_year = models.PositiveSmallIntegerField(null=True, blank=True, validators=[validate_graduation_year])
    degree = models.CharField(max_length=6, choices=DEGREES)

    def __unicode__(self):
        return "%s, %s" % (self.degree, self.department)


class ContactNumber(models.Model):
    user = models.ForeignKey(User, related_name='contacts')
    number = models.CharField(max_length=16)

    def __unicode__(self):
        return self.number


class SecondaryEmail(models.Model):
    user = models.ForeignKey(User, related_name='secondary_emails')
    email = models.EmailField()

    def __unicode__(self):
        return self.email


class SentMessage(models.Model):
    message_id = models.CharField(max_length=256)
    sender = models.ForeignKey(Application)
    user = models.ForeignKey(User)
    status = models.BooleanField(default=True)
    error_message = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.message_id
