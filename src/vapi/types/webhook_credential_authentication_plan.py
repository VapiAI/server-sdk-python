# This file was auto-generated by Fern from our API Definition.

import typing

from .hmac_authentication_plan import HmacAuthenticationPlan
from .o_auth_2_authentication_plan import OAuth2AuthenticationPlan

WebhookCredentialAuthenticationPlan = typing.Union[OAuth2AuthenticationPlan, HmacAuthenticationPlan]
