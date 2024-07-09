from abc import ABC, abstractmethod

class Subscription(ABC):
    def __init__(self, monthly_fee, min_period, channels):
        self.monthly_fee = monthly_fee
        self.min_period = min_period
        self.channels = channels

    def __str__(self):
        return f"{self.__class__.__name__}: ${self.monthly_fee}/month, Min Period: {self.min_period} months, Channels: {', '.join(self.channels)}"

class DomesticSubscription(Subscription):
    def __init__(self):
        super().__init__(10, 12, ["Local News", "Sports", "Entertainment"])

class EducationalSubscription(Subscription):
    def __init__(self):
        super().__init__(15, 6, ["Documentaries", "Science", "History"])

class PremiumSubscription(Subscription):
    def __init__(self):
        super().__init__(30, 1, ["Movies", "Premium Sports", "International News"])
