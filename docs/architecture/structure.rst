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
    <tr><td port="executor_id">executor_id</td></tr>
    <tr><td port="predecessor_id">predecessor_id</td></tr>
    </table>>];

    TaskClassifier [label=<
    <table border="0" cellborder="1" cellspacing="0">
    <tr><td><i>TaskClassifier</i></td></tr>
    <tr><td port="id">id</td></tr>
    <tr><td port="task_id">task_id</td></tr>
    <tr><td port="classifier_id">classifier_id</td></tr>
    </table>>];

    Classifier [label=<
    <table border="0" cellborder="1" cellspacing="0">
    <tr><td><i>Classifier</i></td></tr>
    <tr><td port="id">id</td></tr>
    </table>>];

    ClassifierEffort [label=<
    <table border="0" cellborder="1" cellspacing="0">
    <tr><td><i>ClassifierEffort</i></td></tr>
    <tr><td port="id">id</td></tr>
    <tr><td port="classifier_id">classifier_id</td></tr>
    <tr><td port="effort_id">effort_id</td></tr>
    </table>>];

    Effort [label=<
    <table border="0" cellborder="1" cellspacing="0">
    <tr><td><i>Effort</i></td></tr>
    <tr><td port="id">id</td></tr>
    <tr><td port="type">type</td></tr>
    <tr><td port="computation">computation</td></tr>
    </table>>];

    Executor [label=<
    <table border="0" cellborder="1" cellspacing="0">
    <tr><td><i>Executor</i></td></tr>
    <tr><td port="id">id</td></tr>
    </table>>];

    Task:executor_id -> Executor:id;
    Task:predecessor_id -> Task:id;

    ClassifierEffort:classifier_id -> Classifier:id;
    ClassifierEffort:effort_id -> Effort:id;

    TaskClassifier:task_id -> Task:id;
    TaskClassifier:classifier_id -> Classifier:id;
   
    }


**Tasks** are the central component of the estimation process. In the other
hand we have **Executors** which are those responsible of fulfilling the work
to be done, impacting directly the overall calculation.

Instead of being estimated directly, **Tasks** are assigned one or multiple
**Classifiers** which have been assigned certain set of **Efforts** such as
time, cost, etc (*type*).

An **Effort** may be either an absolute *amount* or a *multiplier*
(*computation*). When multiple efforts are indirectly associated with a
**Task**, amounts are added first and then the multipliers are applied to
the result.
