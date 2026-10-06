from playwright.sync_api import Page,expect


class CompletePage:
    def __init__(self,page:Page):
        self.page = page
        self.text = page.locator(".complete-header")


    def text_assert(self):
        expect(self.text).to_have_text("Thank you for your order!")