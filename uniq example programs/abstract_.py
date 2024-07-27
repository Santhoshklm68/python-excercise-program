from abc import *

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
    @abstractmethod
    def get_status(self):
        pass

class Email_Notification(Notification):

    def send(self):
        message = input("enter the message: ")

        if message.strip():
            print(f"sending email,{message}")
            print("email send successfully")

        else:
            print("email not sent")

    def get_status(self):
        print("getting status of your email")

# class Sms_Notification(Notification):
#     def send(self):
#         print("sms send successfully")

#     def get_status(self):
#         print("get sms status")

# class Push_Notification(Notification):
#     def send(self):
#         print("push notification")

#     def get_status(self):
#         print("status of your push motification")

obj = Email_Notification()
obj.send()
obj.get_status()

# obj2 = Sms_Notification()
# obj2.get_status()

# obj3 = Push_Notification()
# obj3.get_status()