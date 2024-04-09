# Mantendo estados dentro da classe
class Camera:
    def __init__(self, name, filming=False):
        self.name = name
        self.filming = filming

    def film(self):
        if self.filming:
            print(f"{self.name} já está filmando ...")
            return
        print(f"{self.name} está filmando ...")
        self.filming = True

    def stop_film(self):
        if not self.filming:
            print(f"{self.name} não está filmando ...")
            return
        print(f"{self.name} está parando de filmar ...")
        self.filming = False

    def photograph(self):
        if self.filming:
            print(f"{self.name} não pode fotografar enquanto está filmando ...")
            return
        print(f"{self.name} está fotografando ...")

c1 = Camera('Cannon')
c2 = Camera('Sony')
c1.film()
c1.film()
c1.photograph()
c1.stop_film()
c1.photograph()
print()
c2.stop_film()
c2.photograph()
c2.film()
