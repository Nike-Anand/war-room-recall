class StripeV1Client:
    def capture_payment(self, amount, currency):
        return {
            "provider": "stripe_v1",
            "status": "captured",
            "amount": amount,
            "currency": currency
        }


class CheckoutService:
    def __init__(self):
        self.gateway = StripeV1Client()

    def checkout(self, amount, currency):
        return self.gateway.capture_payment(amount, currency)


if __name__ == "__main__":
    checkout = CheckoutService()
    print(checkout.checkout(100, "USD"))