birthyear = int(input("Enter a year of birth (It should not be earlier than 1900):"))

if birthyear >= 1900:
    birthyear = birthyear
else:
    print("Invalid Year, it should not be earlier than 1900")
    
zodiacs = [Rat (鼠 / Shǔ), Ox (牛 / Niú), Tiger (虎 / Hǔ), Rabbit (兔 / Tù), Dragon (龙 / Lóng), Snake (蛇 / Shé), Horse (马 / Mǎ), Goat (羊 / Yáng), Monkey (猴 / Hóu), Rooster (鸡 / Jī), Dog (狗 / Gǒu), Pig (猪 / Zhū)]

zodiacsign = birthyear % 12

print("Your Chinese Zodiac sign is:", zodiacs[zodiacsign-4])