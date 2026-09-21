import startup as st
import register as rt
import login as lt

choice = st.startup()

if choice == 1:
    lt.login()
    
    pass
elif choice == 2:
    rt.register()
else:
    print("Invalid choice, please enter 1 or 2")