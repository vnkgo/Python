class Clock():
    cloak_id = None
    Cloak_price = None

    def Rr(self):
        import winsound
        winsound.Beep(2000, 3000)


clock1 = Clock()
clock1.cloak_id = "00032"
clock1.Cloak_price = 19.99
print(clock1.Cloak_price, clock1.cloak_id)

clock1.Rr()
