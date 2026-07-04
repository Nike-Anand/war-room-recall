import time


class StripeV1Client:
    def capture_payment(self, amount, currency):
        max_retries = 3

        for attempt in range(max_retries):
            response = self._send_capture_request(amount, currency)

            if response["status"] == "captured":
                return response

            time.sleep(1)

        return {
            "provider": "stripe_v1",
            "status": "failed",
            "reason": "timeout_after_retries",
            "amount": amount,
            "currency": currency
        }

    def _send_capture_request(self, amount, currency):
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