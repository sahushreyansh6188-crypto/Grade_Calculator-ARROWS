def startup():
    print("""
    ╔═════════════════════════════════════════════════════╗
    ║                                                     ║
    ║              STUDENT GRADE CALCULATOR               ║
    ║                                                     ║
    ║          Welcome to the Grade Calculator!           ║
    ║                                                     ║
    ╚═════════════════════════════════════════════════════╝

    """)
    input("                Press ENTER to continue...")
    print("1. Login")
    print("2. Register \n")
    choice=int(input("Enter the required num: "))
    return choice