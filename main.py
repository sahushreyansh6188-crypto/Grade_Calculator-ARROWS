import startup as st
import register as rt

choice = st.startup()

if choice == 1:
    #login page
    pass
elif choice == 2:
    rt.register()
else:
    print("Invalid choice, please enter 1 or 2")