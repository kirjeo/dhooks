from dhooks import Webhook
if __name__ == '__main__':
    hook = Webhook("https://discord.com/api/webhooks/962767080086704168/c3JDrcktljYC2F-LfKEbOjBbAmkO3Raf5BTimGJ8x43owU69_d5BmhmP-JudJmT6sm8b")

    data = input("Enter something: ")

    hook.send(data)
