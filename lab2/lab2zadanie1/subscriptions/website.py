from subscriptions.subscription import DomesticSubscription, EducationalSubscription, PremiumSubscription

class WebSite:
    @staticmethod
    def create_subscription(subscription_type):
        if subscription_type == "domestic":
            return DomesticSubscription()
        elif subscription_type == "educational":
            return EducationalSubscription()
        elif subscription_type == "premium":
            return PremiumSubscription()
        else:
            raise ValueError("Unknown subscription type")
