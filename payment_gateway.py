import time


class StripeV1Client:
    deprecated = True

    def capture_payment(self, amount, currency):
        max_retries = 3

        for attempt in range(max_retries):
            response = self._send_capture_request(amount, currency)

            if response["status"] == "captured":
                return response

            if response["reason"] == "rate_limited":
                time.sleep(2)
            else:
                time.sleep(1)

        return self._fallback_payment_record(amount, currency)

    def _send_capture_request(self, amount, currency):
        return {
            "provider": "stripe_v1",
            "status": "failed",
            "reason": "rate_limited",
            "amount": amount,
            "currency": currency
        }

    def _fallback_payment_record(self, amount, currency):
        return {
            "provider": "stripe_v1",
            "status": "queued_for_manual_retry",
            "reason": "stripe_v1_rate_limited",
            "amount": amount,
            "currency": currency
        }


class AdyenGateway:
    def capture_payment(self, amount, currency):
        return {
            "provider": "adyen",
            "status": "captured",
            "amount": amount,
            "currency": currency,
            "compliance": "pci_dss_ready"
        }


class CheckoutService:
    def __init__(self):
        self.gateway = AdyenGateway()

    def checkout(self, amount, currency):
        return self.gateway.capture_payment(amount, currency)


if __name__ == "__main__":
    checkout = CheckoutService()
    print(checkout.checkout(100, "USD"))