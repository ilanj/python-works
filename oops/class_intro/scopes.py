def scope_test():
    def do_local():
        spam = "local spam"

    def do_global():
        global spam
        spam = "global spam"

    def do_nonlocal(): #nonlocal overrides local priority
        nonlocal spam
        spam = "nonlocal spam"


    spam = "test spam"    #local gets first priority
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

"""
<<<<<<< HEAD
The global statement is a declaration which holds for the entire current code block. It means that the listed 
identifiers are to be interpreted as globals.

The nonlocal statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing 
scope excluding globals. 
This is important because the default behaviour for binding is to search the local namespace first. The statement
 allows encapsulated code to rebind variables outside of the local scope besides the global (module) scope."""
=======
The global statement is a declaration which holds for the entire current code block. It means that the listed identifiers are to be interpreted as globals.

The nonlocal statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals. This is important
 because the default behavior for binding is to search the local namespace first. The statement allows encapsulated code to rebind variables outside of the local
  scope besides the global (module) scope."""
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
