from uuid import uuid4
from django.core.management.base import BaseCommand
from django.conf import settings
from django.urls import reverse
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
import qrcode


def _generate_uuid() -> str:
    """
    Internal function to generate a UUID.
    :return: UUID
    """
    return str(uuid4())


def _generate_qr_code():
    """
    Internal function to generate QR-code for the UUID.
    :return:
    """
    qr = qrcode.QRCode(version=1)

    # Generate the URL
    fqdn = settings.INSTANCE_FQDN
    path = reverse('ims:scanned_uuid', args={_generate_uuid()})
    uri = ''.join([fqdn, path])

    # Combine uri in QR
    qr.add_data(uri)
    qr.make(fit=True)

    # Return QR code as an in-memory obj
    return qr.make_image(fill_color="black", back_color="white").convert('RGB')


class Command(BaseCommand):
    """
    Management command for generating labels.
    """
    help = 'Generate labels for IMS-identifiers'

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help='Number of labels to '
                                                     'generate.')
        parser.add_argument('start_num', type=int, help='The first ID-number '
                                                        'to annotate.')
        parser.add_argument('logo_file', type=str, help='path to logo-file.')

    def handle(self, *args, **options):
        # Get args
        amount = options['amount']
        start_num = options['start_num']
        logo_file = options['logo_file']

        self.stdout.write(f'Generating a pdf with {amount} label(s).')

        # Set up the canvas
        papersize = (settings.INSTANCE_LABEL_WIDTH*mm,
                     settings.INSTANCE_LABEL_HEIGHT*mm)
        c = canvas.Canvas('labels.pdf', pagesize=papersize)

        # Generate one label per page
        first = True
        for i in range(start_num, start_num + amount):
            # If not first, then create a new page
            if first:
                first = False
            else:
                c.showPage()

            # Pad the ID number to 6 chars
            id_num = str(i)
            id_num = id_num.zfill(6)

            # Set font and start drawing on canvas
            c.setFont('Helvetica-Bold', 2.5*mm)
            c.drawString(4*mm, 6.5*mm, settings.INSTANCE_LABEL_TEXT)
            c.drawString(4*mm, 2.5*mm, f'#{id_num}')
            c.drawImage(ImageReader(_generate_qr_code()),
                        19*mm, 0.6*mm, 19*mm, 19*mm)
            c.drawImage(logo_file, 6*mm, 9.5*mm, 8.5*mm, 8*mm)

        # Save file
        c.save()
        self.stdout.write(self.style.SUCCESS(
            f'Successfully generated labels.pdf with {amount} labels.'))
