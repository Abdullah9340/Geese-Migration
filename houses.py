

class House:
    def __init__(self, listing_name, price, desc, beds, location, link, image):
        self.listing_name = listing_name
        self.price = price
        self.desc = desc
        self.beds = beds
        self.location = location
        self.link = link
        self.image = image

    def __str__(self):
        a = f"{self.listing_name} {self.price} {self.beds} {self.location}\n{self.desc}"
        return a
