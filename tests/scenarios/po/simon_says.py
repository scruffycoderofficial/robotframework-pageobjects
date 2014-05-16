from robotpageobjects import Page, robot_alias
from robot.utils import asserts

class MyBasePage(Page):
    uri = "/site/index.html"
    def footer_text_should_be(self, text):
        pass


class SubA(MyBasePage):
    def search_for(self, term):
        self.input_text("q", "search term")
        self.click_element("go")
        return SubB()


class SubB(MyBasePage):
    pass


class A(Page):
    uri = "/site/index.html"
    def footer_text_should_be(self, text):
        pass

    def search_for(self, term):
        self.input_text("q", "search term")
        self.click_element("go")
        return B()


class B(Page):
    uri = "/site/index.html"
    def footer_text_should_be(self, text):
        pass


class C(Page):
    uri = "/site/index.html"
    def input_text(self, text):
        super(C, self).input_text("q", text)

    def search_input_text_should_be(self, text):
        self.textfield_value_should_be("q", text)

    def footer_text_should_be(self, text):
        pass