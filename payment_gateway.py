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