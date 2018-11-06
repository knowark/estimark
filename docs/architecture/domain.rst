Domain
======


.. graphviz::

   digraph {

    // Processes
    ////////////

    estimate [color=green]
   
    // Objects
    //////////

    Task [shape=box]
    Classifier [shape=box]
    Effort [shape=box]
    Executor [shape=box]
    Schedule [shape=box]
    Slot [shape=box]

    // Relations
    ////////////

    Task -> estimate [label=list]
    
    estimate -> Schedule

    Task -> Executor [arrowhead=vee]
    Classifier -> Effort [arrowhead=vee]
    Schedule -> Slot [arrowhead=crow]

    Slot -> Task [arrowhead=vee]
    Slot -> Executor [arrowhead=vee]

    Task -> Classifier [arrowhead=vee]
    Classifier -> Task [arrowhead=vee]

    }
