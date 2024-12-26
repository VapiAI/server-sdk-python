# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing_extensions
import datetime as dt
from ..core.serialization import FieldMetadata
from .subscription_type import SubscriptionType
from .subscription_status import SubscriptionStatus
import typing
from .auto_reload_plan import AutoReloadPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Subscription(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    This is the unique identifier for the subscription.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    This is the timestamp when the subscription was created.
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    This is the timestamp when the subscription was last updated.
    """

    type: SubscriptionType = pydantic.Field()
    """
    This is the type / tier of the subscription.
    """

    status: SubscriptionStatus = pydantic.Field()
    """
    This is the status of the subscription. Past due subscriptions are subscriptions
    with past due payments.
    """

    credits: str = pydantic.Field()
    """
    This is the number of credits the subscription currently has.
    
    Note: This is a string to avoid floating point precision issues.
    """

    concurrency_limit: typing_extensions.Annotated[float, FieldMetadata(alias="concurrencyLimit")] = pydantic.Field()
    """
    This is the total concurrency limit for the subscription.
    """

    concurrency_limit_included: typing_extensions.Annotated[float, FieldMetadata(alias="concurrencyLimitIncluded")] = (
        pydantic.Field()
    )
    """
    This is the default concurrency limit for the subscription.
    """

    concurrency_limit_purchased: typing_extensions.Annotated[
        float, FieldMetadata(alias="concurrencyLimitPurchased")
    ] = pydantic.Field()
    """
    This is the purchased add-on concurrency limit for the subscription.
    """

    monthly_charge_schedule_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="monthlyChargeScheduleId")
    ] = pydantic.Field(default=None)
    """
    This is the ID of the monthly job that charges for subscription add ons and phone numbers.
    """

    monthly_credit_check_schedule_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="monthlyCreditCheckScheduleId")
    ] = pydantic.Field(default=None)
    """
    This is the ID of the monthly job that checks whether the credit balance of the subscription
    is sufficient for the monthly charge.
    """

    stripe_customer_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="stripeCustomerId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the Stripe customer ID.
    """

    stripe_payment_method_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stripePaymentMethodId")
    ] = pydantic.Field(default=None)
    """
    This is the Stripe payment ID.
    """

    slack_support_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="slackSupportEnabled")
    ] = pydantic.Field(default=None)
    """
    If this flag is true, then the user has purchased slack support.
    """

    slack_channel_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="slackChannelId")] = (
        pydantic.Field(default=None)
    )
    """
    If this subscription has a slack support subscription, the slack channel's ID will be stored here.
    """

    hipaa_enabled: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="hipaaEnabled")] = (
        pydantic.Field(default=None)
    )
    """
    This is the HIPAA enabled flag for the subscription. It determines whether orgs under this
    subscription have the option to enable HIPAA compliance.
    """

    hipaa_common_paper_agreement_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hipaaCommonPaperAgreementId")
    ] = pydantic.Field(default=None)
    """
    This is the ID for the Common Paper agreement outlining the HIPAA contract.
    """

    stripe_payment_method_fingerprint: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stripePaymentMethodFingerprint")
    ] = pydantic.Field(default=None)
    """
    This is the Stripe fingerprint of the payment method (card). It allows us
    to detect users who try to abuse our system through multiple sign-ups.
    """

    stripe_customer_email: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stripeCustomerEmail")
    ] = pydantic.Field(default=None)
    """
    This is the stripe customer's email.
    """

    referred_by_email: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="referredByEmail")] = (
        pydantic.Field(default=None)
    )
    """
    This is the email of the referrer for the subscription.
    """

    auto_reload_plan: typing_extensions.Annotated[
        typing.Optional[AutoReloadPlan], FieldMetadata(alias="autoReloadPlan")
    ] = pydantic.Field(default=None)
    """
    This is the auto reload plan configured for the subscription.
    """

    minutes_included: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="minutesIncluded")] = (
        pydantic.Field(default=None)
    )
    """
    The number of minutes included in the subscription. Enterprise only.
    """

    minutes_used: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="minutesUsed")] = (
        pydantic.Field(default=None)
    )
    """
    The number of minutes used in the subscription. Enterprise only.
    """

    minutes_overage_cost: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="minutesOverageCost")
    ] = pydantic.Field(default=None)
    """
    The per minute charge on minutes that exceed the included minutes. Enterprise only.
    """

    providers_included: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="providersIncluded")
    ] = pydantic.Field(default=None)
    """
    The list of providers included in the subscription. Enterprise only.
    """

    outbound_calls_daily_limit: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="outboundCallsDailyLimit")
    ] = pydantic.Field(default=None)
    """
    The maximum number of outbound calls this subscription may make in a day. Resets every night.
    """

    outbound_calls_counter: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="outboundCallsCounter")
    ] = pydantic.Field(default=None)
    """
    The current number of outbound calls the subscription has made in the current day.
    """

    outbound_calls_counter_next_reset_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="outboundCallsCounterNextResetAt")
    ] = pydantic.Field(default=None)
    """
    This is the timestamp at which the outbound calls counter is scheduled to reset at.
    """

    coupon_ids: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="couponIds")] = (
        pydantic.Field(default=None)
    )
    """
    This is the IDs of the coupons applicable to this subscription.
    """

    coupon_usage_left: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="couponUsageLeft")] = (
        pydantic.Field(default=None)
    )
    """
    This is the number of credits left obtained from a coupon.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow