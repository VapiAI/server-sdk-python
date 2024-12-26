# This file was auto-generated by Fern from our API Definition.

import typing
from .byo_phone_number import ByoPhoneNumber
from .twilio_phone_number import TwilioPhoneNumber
from .vonage_phone_number import VonagePhoneNumber
from .vapi_phone_number import VapiPhoneNumber

PhoneNumberPaginatedResponseResultsItem = typing.Union[
    ByoPhoneNumber, TwilioPhoneNumber, VonagePhoneNumber, VapiPhoneNumber
]
