import stripe
from django.conf import settings
from rest_framework.generics import get_object_or_404, ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from curses.models import Curs
from payments.models import StripeCheckoutSession
from payments.seriallizers import SessionSerializer
from users.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeCheckoutSessionCreateAPIView(CreateAPIView):
    serializer_class = SessionSerializer

    def post(self, request, *args, **kwargs):
        curs = get_object_or_404(Curs, pk=kwargs['pk'])

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': curs.stripe_price_data,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.DOMAIN + '/payments/' + 'success/',
            cancel_url=settings.DOMAIN + '/payments/' + 'cancel/'
        )

        obj = StripeCheckoutSession.objects.create(
            stripe_id=checkout_session.stripe_id,
            curs=curs,
            status=checkout_session['status'],
            customer_email=request.user.email,
            url=checkout_session.url,
        )
        return Response()


class StripeCheckoutSessionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SessionSerializer

    def get(self, request, *args, **kwargs):
        stripe_session = get_object_or_404(StripeCheckoutSession, stripe_id=kwargs['stripe_id'])
        session = stripe.checkout.Session.retrieve(stripe_session.stripe_id)

        stripe_session.customer_email = session['customer_email']
        stripe_session.status = session['status']
        stripe_session.save()
        return Response()


class StripeCheckoutSessionListAPIView(ListAPIView):
    serializer_class = SessionSerializer
    queryset = StripeCheckoutSession.objects.all()


class StripeCheckoutSessionDestroyAPIView(DestroyAPIView):
    queryset = StripeCheckoutSession.objects.all()