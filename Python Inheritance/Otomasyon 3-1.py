class WebPush:
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = bool(optin)
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def sendpush(self):
        print("Push gönderildi: ", self.push_type)


class TriggerPush(WebPush):
    def __init__(self, trigger_page, platform, optin, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page

class BulkPush(WebPush):
    def __init__(self, send_date, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_date = send_date

class SegmentPush(WebPush):
    def __init__(self, segment_name, platform, optin, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name

class PriceAlertPush(WebPush):
    def __init__(self, price_info, discount_rate, platform, optin, global_frequency_capping, start_date, end_date,
                 language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.price_info = price_info
        self.Discount_rate = float(discount_rate)

    def discountprice(self):
        discountamount = self.price_info - (self.price_info * self.Discount_rate / 100)
        return discountamount

class InstockPush(WebPush):
    def __init__(self, stock_info, platform, optin, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = bool(stock_info)

    def stockupdate(self):
        if self.stock_info:
            self.stock_info = False
        else:
            self.stock_info = True



Trigger1 = TriggerPush("www.asdasd.com", "Web", True, 5, "12/07/2020", "15/07/2020", "TRY", "Trigger")
Bulk1 = BulkPush(5, "Web", True, 4, "12/07/2020", "15/07/2020", "All language", "Bulk")
Segment1 = SegmentPush("Purchase History", "Web", True, 3, "12/07/2020", "15/07/2020", "TRY", "Segment")
PriceAlert1 = PriceAlertPush(55, 3, "web", False, 1, "12/07/2020", "15/07/2020", "TRY", "Price Alert")
Instock1 = InstockPush(True, "web", False, 4, "12/07/2020", "15/07/2020", "TRY", "InStock")

discount = PriceAlert1.discountprice()
Instock1.sendpush()
Segment1.sendpush()
PriceAlert1.sendpush()
Bulk1.sendpush()
Instock1.stockupdate()
Trigger1.sendpush()

print(discount)
print(Instock1.stock_info)