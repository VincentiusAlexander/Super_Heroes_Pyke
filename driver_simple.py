import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

def test_questions():

    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('sp_questions') #STUDENTS: you will need to edit the name of your rule file here

    print("doing proof")
    
    try:
        with engine.prove_goal('sp_questions.($answer)') as gen: #STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("It is: %s" % (vars['answer'])) #STUDENTS: you will need to edit this line

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")