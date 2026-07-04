class PaymentGateway:
    def charge(self, amount, currency):
        return {
            "status": "success",
            "amount": amount,
            "currency": currency
        }


if __name__ == "__main__":
    gateway = PaymentGateway()
    print(gateway.charge(100, "USD"))