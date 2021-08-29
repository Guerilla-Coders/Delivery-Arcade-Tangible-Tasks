from mouth import DeliveryArcadeAgentMouth
ENGLISH = 0

if __name__ == "__main__":
    mouth = DeliveryArcadeAgentMouth()
    hello_world = "hello world!"
    mouth.universal_talk(hello_world, ENGLISH)