Structure
---------


.. graphviz::

   digraph {
    graph [pad="0.5", nodesep="0.5", ranksep="2"];
    node [shape=plain]
    rankdir=LR;

    Task [label=<
    <table border="0" cellborder="1" cellspacing="0">
    <tr><td><i>Task</i></td></tr>
    <tr><td port="id">id</td></tr>
    </table>>];

    Classification [label=<
    <table border="0" cellborder="1" cellspacing="0">
    <tr><td><i>Classification</i></td></tr>
    <tr><td port="id">id</td></tr>
    <tr><td port="task_id">task_id</td></tr>
    <tr><td port="classifier_id">classifier_id</td></tr>
    </table>>];

    Link [label=<
    <table border="0" cellborder="1" cellspacing="0">
    <tr><td><i>Link</i></td></tr>
    <tr><td port="id">id</td></tr>
    <tr><td port="source">source</td></tr>
    <tr><td port="target">target</td></tr>
    </table>>];

    Classifier [label=<
    <table border="0" cellborder="1" cellspacing="0">
    <tr><td><i>Classifier</i></td></tr>
    <tr><td port="id">id</td></tr>
    </table>>];

    Classification:task_id -> Task:id;
    Classification:classifier_id -> Classifier:id;

    Link:source -> Task:id;
    Link:target -> Task:id;
    
    }


**Tasks** are the central component of the estimation process. They have a
"state" and an "owner" responsible for their completion.

**Links** represent the dependencies between **Tasks**, declaring their
predecessors and successors.

Instead of being estimated directly, **Tasks** are assigned one or multiple
**Classifiers** which represent certain value of effort/time for completion.
