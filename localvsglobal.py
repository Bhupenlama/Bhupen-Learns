#Global - VIsible everywhere
def show_scope():
    y=200
    print(f"Inside:y=(y)")

    def modfiy_global():
        global x
        x=300
        print(f"Inside modify_global:x={x}")
        show_scope()
        modify_global()
        print ("outside:x=(x)")


