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
    Link [shape=box]
    Classifier [shape=box]
    Classification [shape=box]
    Effort [shape=box]
    Executor [shape=box]
    Schedule [shape=box]
    Slot [shape=box]

    // Relations
    ////////////

    Task -> estimate [label=list]
    
    estimate -> Schedule
    estimate -> Slot

    Task -> Executor [arrowhead=vee, label=Nullable]
    Link -> Task [arrowhead=vee]
    Link -> Task [arrowhead=vee]
    Classifier -> Effort [arrowhead=vee]
    
    Slot -> Task [arrowhead=vee]
    Slot -> Executor [arrowhead=vee]
    Slot -> Schedule [arrowhead=vee]

    Classification -> Task [arrowhead=vee]
    Classification -> Classifier [arrowhead=vee]

    }
