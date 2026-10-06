from faker import Faker
import random
import string
from playwright.sync_api import Page


class RandomDataClass:
    def __init__(self):
        self.faker = Faker()

    def first_name(self):
        return self.faker.first_name()

    def last_name(self):
        return self.faker.last_name()

    def get_zipcode(self):
        return self.faker.zipcode()
