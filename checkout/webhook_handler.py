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
            content = f'Wbhook recieved: {event["type"]}', status=200)