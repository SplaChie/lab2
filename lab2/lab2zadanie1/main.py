from subscriptions.website import WebSite
from subscriptions.mobile_app import MobileApp
from subscriptions.manager_call import ManagerCall

def main():
    # Створення підписки через WebSite
    subscription1 = WebSite.create_subscription("domestic")
    print(subscription1)

    # Створення підписки через MobileApp
    subscription2 = MobileApp.create_subscription("educational")
    print(subscription2)

    # Створення підписки через ManagerCall
    subscription3 = ManagerCall.create_subscription("premium")
    print(subscription3)

if __name__ == "__main__":
    main()
