class House:
    def __init__(self, listing_name, price, desc, beds, location, link, image, id=-1):
        self.listing_name = listing_name
        self.price = price
        self.desc = desc
        self.beds = beds
        self.location = location
        self.link = link
        self.image = image
        self.id = id

    def __str__(self):
        a = f"{self.listing_name} {self.price} {self.beds} {self.location}\n{self.desc}"
        return a
