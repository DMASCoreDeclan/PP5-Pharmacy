from django.http import HttpResponse    


class StripeWH_Handler:
    """
    Handle Stripe Web hooks
    https://docs.stripe.com/webhooks
    """

    def __init(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a reneric/unknown or unexpected webhook event
        """
        return HttpResponse(
            content = f'Unhandled Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        return HttpResponse(
            content = f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intnet_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content = f'Webhook recieved: {event["type"]}',
            status=200)