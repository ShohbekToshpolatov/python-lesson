
class Hotel:
    def __init__(self):
#xotirada faqat bo'sh Hotel obyektining atributlari (self.rooms va self.bookings) yaratiladi.
        self.rooms = {}  # Xonalar ro'yxati: {xona_raqami: {'narx': int, 'holat': 'bo'sh/band'}}
        self.bookings = {}  # Bronlash ma'lumotlari: {xona_raqami: {'mijoz': str, 'telefon': str}}

    def add_room(self, room_number, price):
# Qo'shilgan xonalar yoki bronlar soniga qarab, xotira ishlatishi ortib boradi.
        if room_number in self.rooms:
            print(f"{room_number}-xona allaqachon mavjud.")
        else:
            self.rooms[room_number] = {'narx': price, 'holat': 'bo\'sh'}
            print(f"{room_number}-xona qo'shildi. Narxi: ${price}")

    def view_rooms(self):
        print("\nXonalar ro'yxati:")
        for room, info in self.rooms.items():
            status = info['holat']
            print(f"Xona {room}: Narxi - ${info['narx']}, Holati - {status}")

    def book_room(self, room_number, customer_name, phone_number):
        if room_number not in self.rooms:
            print("Bunday xona mavjud emas.")
        elif self.rooms[room_number]['holat'] == 'band':
            print(f"{room_number}-xona allaqachon band qilingan.")
        else:
            self.rooms[room_number]['holat'] = 'band'
            self.bookings[room_number] = {'mijoz': customer_name, 'telefon': phone_number}
            print(f"{room_number}-xona {customer_name} tomonidan bron qilindi.")

    def cancel_booking(self, room_number):
        if room_number not in self.rooms:
            print("Bunday xona mavjud emas.")
        elif self.rooms[room_number]['holat'] == 'bo\'sh':
            print(f"{room_number}-xona band qilinmagan.")
        else:
            self.rooms[room_number]['holat'] = 'bo\'sh'
#Xona bronini bekor qilganda, tegishli element lug'atdan o'chiriladi va Python avtomatik ravishda xotiradagi bo'sh joyni qayta ishlatadi.
            self.bookings.pop(room_number, None)  
            print(f"{room_number}-xona bandligi bekor qilindi.")


def main():
    hotel = Hotel()

    while True:
        print("\nMehmonxona boshqaruv tizimi:")
        print("1. Xona qo'shish")
        print("2. Xonalar ro'yxatini ko'rish")
        print("3. Xonani bron qilish")
        print("4. Bronni bekor qilish")
        print("5. Chiqish")

        choice = input("Tanlovni kiriting (1/2/3/4/5): ")

        if choice == '1':
            room_number = input("Xona raqamini kiriting: ")
            price = int(input("Xonaning narxini kiriting: "))
            hotel.add_room(room_number, price)
        elif choice == '2':
            hotel.view_rooms()
        elif choice == '3':
            room_number = input("Bron qilmoqchi bo'lgan xona raqamini kiriting: ")
            customer_name = input("Mijozning ismini kiriting: ")
            phone_number = input("Mijozning telefon raqamini kiriting: ")
            hotel.book_room(room_number, customer_name, phone_number)
        elif choice == '4':
            room_number = input("Bekor qilmoqchi bo'lgan xona raqamini kiriting: ")
            hotel.cancel_booking(room_number)
        elif choice == '5':
# Dastur tugagandan so'ng, barcha xotiradagi ma'lumotlar yo'qotiladi (agar faylga yozib qo'yilmagan bo'lsa)
            print("Tizimdan chiqyapman...")
            break
        else:
            print("Noto'g'ri tanlov. Iltimos, yana urinib ko'ring.")

if __name__ == "__main__":
    main()
